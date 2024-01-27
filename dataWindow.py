import gc
from PyQt6 import QtWidgets, QtCore
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rcParams['path.simplify'] = True
matplotlib.rcParams['path.simplify_threshold'] = 1.0
matplotlib.rcParams['agg.path.chunksize'] = 50000
matplotlib.rcParams["legend.loc"] = 'upper right'
import numpy as np
from dataCore import dataCore
from dataWindowUiDesign import Ui_DataWidget
from dataCore import dataCore
from FT2Signal import *


class DataWindow(QtWidgets.QWidget, Ui_DataWidget):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.monitorData = data
        self.temperaturesData = dataCore()


        self.plot_widget = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.toolbar = NavigationToolbar2QT(self.plot_widget, self)
        self.plot_widget.figure.dpi = 80.0
        ax1 = self.plot_widget.figure.add_subplot(1, 1, 1)
        ax1.set_title("Temperature trace")
        ax1.set_xlabel('Time, ms')
        ax1.set_ylabel('Temperature eV')
        ax1.grid()
        self.plot_widget.draw()

        self.plot_profile_widget = FigureCanvasQTAgg(Figure(tight_layout=True))
        ax2 = self.plot_profile_widget.figure.add_subplot(1, 1, 1)
        ax2.set_title("Temperature profile")
        ax2.set_xlabel('Position, cm')
        ax2.set_ylabel('Temperature eV')
        ax2.grid()
        ax2.set_xlim((-8, 8))
        ax2.set_ylim((0, 1000))
        self.plot_profile_widget.draw()

        self.timeTrace_verticalLayout.addWidget(self.toolbar)
        self.timeTrace_verticalLayout.addWidget(self.plot_widget)
        self.timeTrace_verticalLayout.maximumSize()
        self.profile_verticalLayout.addWidget(self.plot_profile_widget)

        self.calculate_pushButton.clicked.connect(self.calculate_temperatures)
        self.time_horizontalSlider.valueChanged.connect(self.update_time)

    def calculate_temperatures(self):
        del self.temperaturesData
        self.temperaturesData = dataCore()
        signal_names = tuple(self.monitorData.signals.keys())
        if int(self.foil1_comboBox.currentText()) <= int(self.foil2_comboBox.currentText()):
            for i in range(7):
                if f'SXR{2 * i + 1}' in signal_names and f'SXR{2 * i + 2}' in signal_names and eval(
                        f'self.show{i + 1}_checkBox.isChecked()'):
                    noSignalTime = [
                        int(self.lowTime_spinBox.value() * 1000 / self.monitorData.signals[f'SXR{2 * i + 1}'].period),
                        int(self.highTime_spinBox.value() * 1000 / self.monitorData.signals[f'SXR{2 * i + 1}'].period)]
                    sigma = max(np.std(self.monitorData.signals[f'SXR{2 * i + 1}'].data[noSignalTime[0]: noSignalTime[1]]),
                                np.std(self.monitorData.signals[f'SXR{2 * i + 2}'].data[noSignalTime[0]: noSignalTime[1]]))
                    self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'], _, _ = get_temp_from_signals(
                        self.monitorData.signals[f'SXR{2 * i + 1}'], self.monitorData.signals[f'SXR{2 * i + 2}'],
                        filter_size=50,
                        zero_diap=noSignalTime,
                        threshold=self.threshold_doubleSpinBox.value() * sigma,
                        foil1=int(self.foil1_comboBox.currentText()),
                        foil2=int(self.foil2_comboBox.currentText()),
                        coef12=1
                    )
                    if self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].times is None:
                        self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].times = [
                            self.monitorData.signals[f'SXR{2 * i + 1}'].period / 1000 * j for j in
                            range(len(self.monitorData.signals[f'SXR{2 * i + 1}'].data))]
                    if self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].period is None:
                        self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].period = self.monitorData.signals[f'SXR{2 * i + 1}'].period
        else:
            for i in range(7):
                if f'SXR{2 * i + 2}' in signal_names and f'SXR{2 * i + 1}' in signal_names and eval(
                        f'self.show{i + 1}_checkBox.isChecked()'):
                    noSignalTime = [
                        int(self.lowTime_spinBox.value() * 1000 / self.monitorData.signals[f'SXR{2 * i + 1}'].period),
                        int(self.highTime_spinBox.value() * 1000 / self.monitorData.signals[f'SXR{2 * i + 1}'].period)]
                    sigma = max(np.std(self.monitorData.signals[f'SXR{2 * i + 1}'].data[noSignalTime[0]: noSignalTime[1]]),
                                np.std(self.monitorData.signals[f'SXR{2 * i + 2}'].data[noSignalTime[0]: noSignalTime[1]]))
                    self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'], _, _ = get_temp_from_signals(
                        self.monitorData.signals[f'SXR{2 * i + 2}'], self.monitorData.signals[f'SXR{2 * i + 1}'],
                        filter_size=self.smoothing_spinBox.value(),
                        zero_diap=noSignalTime,
                        threshold=self.threshold_doubleSpinBox.value() * sigma,
                        foil1=int(self.foil1_comboBox.currentText()),
                        foil2=int(self.foil2_comboBox.currentText()),
                        coef12=1
                    )
                    if self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].times is None:
                        self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].times = [
                            self.monitorData.signals[f'SXR{2 * i + 1}'].period / 1000 * j for j in
                            range(len(self.monitorData.signals[f'SXR{2 * i + 1}'].data))]
                    if self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].period is None:
                        self.temperaturesData.signals[f'SXR{2 * i + 1}-{2 * i + 2}'].period = self.monitorData.signals[f'SXR{2 * i + 1}'].period


        self.plot_timeTraced()
        self.plot_profile()

    def plot_timeTraced(self):
        signal_names = tuple(self.temperaturesData.signals.keys())
        if len(signal_names) != 0:
            self.plot_widget.figure.clear('all')
            ax1 = self.plot_widget.figure.add_subplot(1, 1, 1)
            for signal in signal_names:
                ax1.plot(self.temperaturesData.signals[signal].times, self.temperaturesData.signals[signal].data, label=signal)
            ax1.axvline(x=float(self.time_label.text()))
            ax1.set_title("Temperature trace")
            ax1.set_xlabel('Time, ms')
            ax1.set_ylabel('Temperature eV')
            ax1.legend()
            ax1.grid()
            self.plot_widget.draw()
            gc.collect(generation=2)

    def plot_profile(self):
        signal_names = tuple(self.temperaturesData.signals.keys())
        if len(signal_names) != 0:
            self.time_horizontalSlider.setMinimum(0)
            self.time_horizontalSlider.setValue(self.time_horizontalSlider.minimum())
            self.time_horizontalSlider.setMaximum(len(self.temperaturesData.signals[signal_names[0]].data)-1)
            self.update_profile()

    def update_profile(self):
        point = self.time_horizontalSlider.value()
        signal_names = tuple(self.temperaturesData.signals.keys())
        self.time_label.setText(f'{self.temperaturesData.signals[signal_names[0]].period / 1000 * point:5.3f}')
        self.plot_profile_widget.figure.clear('all')
        ax2 = self.plot_profile_widget.figure.add_subplot(1, 1, 1)
        r = []
        T = []
        for i in range(7):
            if f'SXR{2*i+1}-{2*i+2}' in signal_names and self.temperaturesData.signals[f'SXR{2*i+1}-{2*i+2}'].data[point] > 0:
                r.append(-7.5+i*2.5)
                T.append(self.temperaturesData.signals[f'SXR{2*i+1}-{2*i+2}'].data[point])
        ax2.plot(r, T, 'b*-')
        ax2.set_title("Temperature profile")
        ax2.set_xlabel('Position, cm')
        ax2.set_ylabel('Temperature eV')
        ax2.grid()
        ax2.set_xlim((-8, 8))
        ax2.set_ylim((0, 1000))
        self.plot_profile_widget.draw()
        gc.collect(generation=2)

    def update_time(self):
        self.update_profile()
        self.plot_timeTraced()


