import h5py as h5
import numpy as np
from matplotlib import pyplot as plt
# import silx as sx
from silx.math import medfilt1d
from silx.math.fit import savitsky_golay
from silx.math.fit import smooth1d
import os
from scipy.fft import fft, fftfreq
from bisect import bisect_left


class Signal:
    def __init__(self):
        self.date = None  # dd.mm.yy
        self.time = None  # hh:mm:ss
        self.shot = None  # int, number
        self.period = None  # us
        self.bit = None  # int, precision
        self.volt_range = None  # [min, max] float
        self.regime = None  # OH, RF, ...
        self.duration = None  # ms of the shot
        self.comment = None  # str
        self.name = None  # str
        self.ch_number = None  # int
        self.units = None  # str
        self.data = None  # np.array
        self.times = None


def copy_signal(sig: Signal) -> Signal:
    new_sig = Signal()
    new_sig.date = sig.date  # dd.mm.yy
    new_sig.time = sig.time  # hh:mm:ss
    new_sig.shot = sig.shot  # int, number
    new_sig.period = sig.period  # ms
    new_sig.bit = sig.bit  # int, precision
    new_sig.volt_range = sig.volt_range  # [min, max] float
    new_sig.regime = sig.regime  # OH, RF, ...
    new_sig.duration = sig.duration  # ms of the shot
    new_sig.comment = sig.comment  # str
    new_sig.name = sig.name  # str
    new_sig.ch_number = sig.ch_number  # int
    new_sig.units = sig.units  # str
    new_sig.data = np.copy(sig.data)  # np.array
    return new_sig


def get_signals_from_hdf5(path: str) -> dict:
    with h5.File(path, 'r') as f:
        diags = {}
        for diag in f['diagnostics'].keys():
            sig = Signal()
            sig.data = np.array(f['diagnostics'][diag]['data'])[:1762]
            sig.name = diag
            # sig.units =
            sig.time = str(int(f['shot']['time']['hour'][0])) + ':' + str(int(f['shot']['time']['minutes'][0])) + ':' + str(int(f['shot']['time']['seconds'][0]))
            sig.shot = int(f['shot']['shotnum'][0])
            # sig.comment =
            sig.date = str(int(f['shot']['date']['day'][0])) + '.' + str(int(f['shot']['date']['month'][0])) + '.' + str(int(f['shot']['date']['year'][0]))
            sig.duration = int(f['shot']['intime'][0])
            sig.period = int(f['shot']['rate'][0])
            diags[diag] = sig
        return diags


def get_sxr_table(path: str) -> list:
    data = []
    with open(path, 'r') as f:
        for line in f.readlines():
            data_line = np.array([float(line[0:8].strip())] + [float(i) for i in line[8:-1].split(' ')])
            data.append(data_line)
    data = np.array(data).T
    return data


def get_passing_table(path: str) -> [list, list]:
    energy = []
    passing = []
    with open(path, 'r') as f:
        f.readline()
        f.readline()
        for line in f.readlines():
            energy.append(eval(line[4:10]))
            passing.append(eval(line[16:27]))
    return np.array(energy), np.array(passing)


def filter_signal(signal: Signal, filter_size: int):
    signal = copy_signal(signal)
    data = medfilt1d(signal.data, kernel_size=15)
    win = np.ones(filter_size) / filter_size
    data = np.convolve(data, win, mode='same')
    # data = smooth1d(smooth1d(smooth1d(data)))
    data = savitsky_golay(data, npoints=filter_size)
    signal.data = data
    return signal


def shift2zero(signal: Signal, zero_diap: list[2]):
    signal = copy_signal(signal)
    mean = np.median(signal.data[zero_diap[0]:zero_diap[1]])
    # mean = 0
    signal.data = signal.data - mean
    return signal


def clean_threshold(signal: Signal, threshold: float) -> Signal:
    signal = copy_signal(signal)
    data = []
    for i in signal.data:
        data.append(0 if i < threshold else i)
    data = np.array(data)
    signal.data = data
    return signal


def get_temp_from_signals(high_signal: Signal, low_signal: Signal, filter_size: int, zero_diap: list[2], threshold: float, coef12: float, foil1: int, foil2: int) -> (Signal, Signal, Signal):
    cwd = os.getcwd()
    tab_dir = os.path.join(cwd, os.path.normpath('tables'))
    foils = (100, 200, 300, 400, 500, 700)
    tables = ('table_be_100um.txt', 'table_be_200um.txt', 'table_be_300um.txt', 'table_be_400um.txt', 'table_be_500um.txt', 'table_be_700um.txt')
    sigh = copy_signal(high_signal)
    sigl = copy_signal(low_signal)

    sigh = shift2zero(sigh, zero_diap=zero_diap)
    sigh = filter_signal(sigh, filter_size=filter_size)
    sigl = shift2zero(sigl, zero_diap=zero_diap)
    sigl = filter_signal(sigl, filter_size=filter_size)

    for_relh = clean_threshold(sigh, threshold=threshold).data
    for_rell = clean_threshold(sigl, threshold=threshold).data

    rel = np.nan_to_num(for_relh * coef12 / for_rell, nan=0.0, neginf=0.0, posinf=0.0)

    foil1_num = foils.index(foil1) + 1
    foil2_num = foils.index(foil2) + 1

    table_path = os.path.join(tab_dir, tables[foil1_num-1])
    # table_path = r'D:\home\projects\SXR\add_codes\readFT2\sxr_table.dat'
    sxrt = get_sxr_table(table_path)

    data = []
    for r in rel:
        if r == 0.0:
            data.append(0.0)
        elif sxrt[foil2_num][-1] <= r <= sxrt[foil2_num][0]:
            bottom_ind = 0
            top_ind = 0
            for i, rt in enumerate(sxrt[foil2_num][:-1]):
                if sxrt[foil2_num][i] >= r >= sxrt[foil2_num][i+1]:
                    bottom_ind = i
                    top_ind = i+1
                    break
            part = (r - sxrt[foil2_num][top_ind]) / (sxrt[foil2_num][bottom_ind] - sxrt[foil2_num][top_ind])
            t = sxrt[0][bottom_ind] + (sxrt[0][top_ind] - sxrt[0][bottom_ind]) * part
            data.append(t)
        else:
            data.append(0.0)

    data = smooth1d(np.array(data))
    signal = Signal()
    signal.data = data

    return signal, sigh, sigl


def make_fourier(signal: Signal) -> Signal:
    signal = copy_signal(signal)
    N = len(signal.data)
    T = signal.period / 1e6

    yf = np.abs(fft(signal.data))
    xf = fftfreq(N, T)

    signal.data = yf
    signal.times = xf
    signal.units = 'Hz'
    return signal


def make_clb(high_signal: Signal, low_signal: Signal, filter_size: int, threshold: float, zero_diap: list[2], mean_diap: list[2]) -> (Signal, float):
    sigh = copy_signal(high_signal)
    sigl = copy_signal(low_signal)

    sigh = shift2zero(sigh, zero_diap=zero_diap)
    sigh = filter_signal(sigh, filter_size=filter_size)
    sigl = shift2zero(sigl, zero_diap=zero_diap)
    sigl = filter_signal(sigl, filter_size=filter_size)

    sigh = clean_threshold(sigh, threshold=threshold)
    sigl = clean_threshold(sigl, threshold=threshold)

    rel = np.nan_to_num(sigh.data / sigl.data, nan=0.0, neginf=0.0, posinf=0.0)

    mean = np.mean(rel[mean_diap[0]:mean_diap[1]])

    sigr = Signal()
    sigr.data = rel

    return sigr, mean


def read_txt(path: str):
    times = []
    temps = []
    with open(path, 'r') as f:
        f.readline()
        for line in f:
            line = line.split(' ')
            while '' in line:
                line.remove('')
            times.append(float(line[0]))
            temps.append(int(line[2][:-1]))
    return times, temps


def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before


if __name__ == '__main__':
    diags1 = get_signals_from_hdf5(r"D:\home\projects\SXR\add_codes\readFT2\A230302_009.h5")
    time = np.array([i*0.034 for i in range(2048)])
    plt.subplot(2, 1, 1)
    first = 7
    second = 8
    plt.plot(time, diags1[f'SXR{first}'].data)
    plt.plot(time, diags1[f'SXR{second}'].data)
    sigma = max(np.std(diags1[f'SXR{first}'].data[0:290]), np.std(diags1[f'SXR{second}'].data[0:290]))
    print(sigma, 'from 0 to', time[290], 'ms')
    t, sigh, sigl = get_temp_from_signals(diags1[f'SXR{first}'], diags1[f'SXR{second}'], filter_size=50, zero_diap=[0, 290], threshold=3*sigma, foil1=100, foil2=200, coef12=1)
    plt.plot(time, sigh.data)
    plt.plot(time, sigl.data)
    # rel, mean = make_clb(diags['SXR5'], diags['SXR6'], filter_size=150, zero_diap=[150, 300], mean_diap=[700, 1000], threshold=30)
    # plt.plot(rel.data)
    # print(mean)
    plt.grid()
    plt.legend([f'Row channel {first}, mV', f'Row channel {second}, mV', f'Filtered channel {first}, mV', f'Filtered channel {second}, mV'])
    plt.title('Row signals, shot 230302_009 (be00, be100)')

    plt.subplot(2, 1, 2)
    plt.plot(time, t.data)
    times_old, temps_old = read_txt(os.path.abspath(f"D:\home\projects\SXR\\add_codes\\readFT2\{first}_{second}.txt"))
    plt.plot(times_old, temps_old)

    plt.grid()
    plt.legend(['Temperature, keV', 'Old program, keV'])
    plt.title('Electron temperature')
    plt.show()
