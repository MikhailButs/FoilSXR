from PyQt6 import QtWidgets, QtCore
import sys
import os
import numpy as np
import gc
import time
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from calibrationWindowUiDesign import Ui_calibrationWidgetUIDesign
import configparser
import datetime
from dataCore import dataCore
from FT2Signal import take_closest


class calibrationWindow(QtWidgets.QWidget, Ui_calibrationWidgetUIDesign):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = data

        self.plot = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.plot.figure.dpi = 80.0
        self.plot_verticalLayout.addWidget(self.plot)

        self._fill_comboBox()
        self._plot_graphs()

        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.last_date_label.setText(self.config['DATE']['last_clibration_date'])

        self.first_comboBox.currentIndexChanged.connect(self._plot_graphs)
        self.second_comboBox.currentIndexChanged.connect(self._plot_graphs)
        self.pair_comboBox.currentIndexChanged.connect(self._select_pair)

    def _select_pair(self):
        ind = self.pair_comboBox.currentIndex()
        first = f'SXR{2*ind-1}'
        second = f'SXR{2*ind}'

        keys = list(self.data.signals.keys())

        if first in keys:
            self.first_comboBox.blockSignals(True)
            self.first_comboBox.setCurrentText(first)
            self.first_comboBox.blockSignals(False)
        if second in keys:
            self.second_comboBox.blockSignals(True)
            self.second_comboBox.setCurrentText(second)
            self.second_comboBox.blockSignals(False)

        self._plot_graphs()

    def _fill_comboBox(self):
        keys = list(self.data.signals.keys())
        for type in ('first', 'second'):
            exec(f'self.{type}_comboBox.blockSignals(True)')
            exec(f'self.{type}_comboBox.clear()')
            exec(f'self.{type}_comboBox.addItem("-")')
            if len(self.data.signals.keys()) != 0:
                for key in keys:
                    exec(f'self.{type}_comboBox.addItem(key)')
            exec(f'self.{type}_comboBox.blockSignals(False)')

    def _plot_graphs(self):
        self.plot.figure.clear()

        ax1 = self.plot.figure.add_subplot(2, 1, 1)
        ax1.set_title('Row and preprocessed signals')
        first = self.first_comboBox.currentText()
        second = self.second_comboBox.currentText()

        if first != '-':
            num = len(self.data.signals[f'{first}'].data)
            ax1.plot(np.linspace(0, num * self.data.signals[f'{first}'].period / 1000, num),
                self.data.signals[f'{first}'].data, label=f'{first}')
        if second != '-':
            num = len(self.data.signals[f'{second}'].data)
            ax1.plot(np.linspace(0, num * self.data.signals[f'{second}'].period / 1000, num),
                self.data.signals[f'{second}'].data, label=f'{second}')

        ax1.grid()
        ax1.legend()

        ax2 = self.plot.figure.add_subplot(2, 1, 2)
        ax2.set_title('Quotient of the signals')
        if first != '-' and second != '-':
            ax2.plot(self.data.signals[f'{first}'].data/self.data.signals[f'{second}'].data, label=f'{first}/{second}')

        ax2.grid()
        ax2.legend()

        self.plot.figure.tight_layout()

        self.plot.draw()
        gc.collect(generation=2)

    def refresh_slot(self):
        self._fill_comboBox()
        self._plot_graphs()