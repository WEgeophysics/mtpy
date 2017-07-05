# -*- coding: utf-8 -*-
"""
    Description:
        define the object to initialize the plot option subwindow

    Author: YingzhiGou
    Date: 20/06/2017
"""
from PyQt4 import QtGui, QtCore

from mtpy.gui.SmartMT.ui_asset.plot_options import Ui_PlotOption
from mtpy.gui.SmartMT.visualization.visualization_base import VisualizationBase


class PlotOption(QtGui.QWidget):
    def __init__(self, parent, file_handler, selected_files):
        """

        :param parent:
        :type parent: StartQt4
        :param file_handler:
        :type file_handler: FileHandler
        :param selected_files:
        :type selected_files: set
        """
        QtGui.QWidget.__init__(self, parent)
        self.file_handler = file_handler
        self.selected_stations = selected_files
        self.ui = Ui_PlotOption()
        self.ui.setupUi(self)
        # populate dropdown menu
        self.plotOptions = dict()

        print eval(VisualizationBase.__name__).__subclasses__()

        for child in _find_all_subclasses(VisualizationBase):
            name = child.get_plot_name()
            if name not in self.plotOptions:
                self.plotOptions[name] = child
                self.ui.comboBoxSelect_Plot.addItem(name)
            else:
                raise Exception("Duplicated Plot Name: %s in class %s" % (name, child.__name__))

        self.ui.comboBoxSelect_Plot.currentIndexChanged.connect(self._selection_changed)

    def _selection_changed(self, *args, **kwargs):
        print "selection changed"


def _find_all_subclasses(cls):
    return eval(cls.__name__).__subclasses__() + [g for s in eval(cls.__name__).__subclasses__() for g in _find_all_subclasses(s)]
