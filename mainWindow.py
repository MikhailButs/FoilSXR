import sys
import os
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
from mainWindowUiDesign import Ui_MainWindow
from dataCore import dataCore
from FT2Signal import get_signals_from_hdf5
from calibrationWondow import calibrationWindow
from dataWindow import DataWindow
from signalWindowUi import signalWindowWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.statusbar = self.statusBar()
        self.statusbar.show()

        self.data = dataCore()
        self.signals_dict = {}

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        Hlayout = QtWidgets.QHBoxLayout(self._main)

        self.plot_widget = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.plot_widget.figure.dpi = 80.0
        #self.addToolBar(NavigationToolbar2QT(self.plot_widget, self))
        self.toolbar = NavigationToolbar2QT(self.plot_widget, self)

        self.calibrationWindow = calibrationWindow(data=self.data)
        self.refresh_signal.connect(self.calibrationWindow.refresh_slot)

        self.dataWindow = DataWindow(data=self.data)

        self.verticalLayout_7.addWidget(self.toolbar)
        self.verticalLayout_7.addWidget(self.plot_widget)
        Hlayout.addWidget(self.frame_5)
        Hlayout.addWidget(self.frame_2)

        ax1 = self.plot_widget.figure.add_subplot(1, 1, 1)
        ax1.set_title("Nothing to plot")
        ax1.set_xlabel('Time, ms')
        ax1.set_ylabel('Arbitrary units')

        ax1.grid()
        self.plot_widget.draw()

        self.sig_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.select_pushButton.clicked.connect(self.select_shot)
        self.plot_pushButton.clicked.connect(self.make_plot)
        self.actionChannals_calibration.triggered.connect(self.show_calibrationWindow)
        self.actionCompute_temperatures.triggered.connect(self.show_dataWindow)
        self.temperatures_pushButton.clicked.connect(self.show_dataWindow)

    def _load_shot(self, filepath):
        self.statusbar.showMessage('Reading file...', msecs=3000)
        self.statusbar.show()
        self.data.filepath = filepath
        self.data.filename = os.path.split(self.data.filepath)[-1]
        for file in os.listdir():
            if file[-3:] == '.h5':
                os.remove(file)
        if self.data.filename[-3:] != '.h5':
            self.statusbar.show()
            os.system(".\\ft2toh5converter\\ft2_to_h5.exe " + self.data.filepath)
            real_file = self.data.filename[:-4] + '_' + self.data.filename[-3:] + '.h5'
        else:
            real_file = self.data.filepath
        self.statusbar.show()
        self.read_h5(filepath=real_file)
        self.statusbar.showMessage('Got the file!', msecs=3000)
        self.statusbar.show()
        self.refresh_ui()
        self.refresh_signal.emit()
        self.make_plot()

    def make_plot(self):
        self.plot_widget.figure.clear('all')
        ax1 = self.plot_widget.figure.add_subplot(1, 1, 1)
        ax1.set_title(f"Data from FT-2 file {self.data.filename}")

        if self.data.signals is not None and len(self.data.signals.keys()) != 0:
            for key in self.data.signals.keys():
                if self.signals_dict[key].is_checked():
                    k = self.signals_dict[key].mult_coef()
                    signal_shift = self.signals_dict[key].zero_signal()
                    time_shift = self.signals_dict[key].zero_time()
                    ax1.plot(np.array(
                        [self.data.signals[key].period / 1000 * i for i in range(len(self.data.signals[key].data))])
                             + time_shift, self.data.signals[key].data * k + signal_shift, label=key)
        ax1.legend()
        ax1.grid()
        ax1.set_xlabel('Time, ms')
        ax1.set_ylabel('Arbitrary units')
        self.plot_widget.draw()
        self.statusbar.showMessage('Plotted!', 3000)
        gc.collect(generation=2)

    def refresh_ui(self):
        self._fill_signals_box()
        self._fill_shot_metadata()

    def _fill_shot_metadata(self):
        signal = self.data.signals[f'{list(self.data.signals.keys())[0]}']
        self.filename_label.setText(self.data.filename)
        self.shotNo_label.setText(f'{signal.shot}')
        self.date_label.setText(f'{signal.date}')
        self.time_label.setText(f'{signal.time}')
        self.duration_label.setText(f'{signal.duration}')
        self.rate_label.setText(f'{signal.period}')
        self.mode_label.setText(f'{signal.regime}')
        self.comment_label.setText(f'{signal.comment}')

    def _fill_signals_box(self):
        if self.data.signals is not None and len(self.data.signals.keys()) > 0:
            for num, key in enumerate(self.data.signals.keys()):
                exec(f'win{num} = signalWindowWidget()')
                exec(f'self.signals_dict[key] = win{num}')
                exec(f'win{num}.set_name(key)')
                # zero_signal = np.mean(self.data.sht_data[key]['y'][0:100])
                # exec(f'win{num}.set_zero_signal(-zero_signal)')
                exec(f'self.sig_layout.addWidget(win{num})')

    def read_h5(self, filepath):
        self.data.signals = get_signals_from_hdf5(path=filepath)

    def select_shot(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'FT-2 shot file', ".", "A*.0* ; A*.h5")[0]
        if filepath != '':
            self._load_shot(filepath=filepath)

    def show_calibrationWindow(self):
        self.calibrationWindow.show()

    def show_dataWindow(self):
        self.dataWindow.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('Fusion')
    mv = MainWindow()
    mv.showMaximized()
    # mv.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
