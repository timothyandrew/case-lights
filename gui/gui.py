import sys

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow, QAction, QDialog)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication, QThread, QObject, pyqtSignal
from ui_case_lights import Ui_CaseLights
from functools import partial

from strategy.rgb import RGBStrategy
from strategy.white import WhiteStrategy
from strategy.pulse import PulseStrategy
from strategy.clear import ClearStrategy

from util import log
from worker import Worker
import comm

class CaseLightsWindow(QMainWindow):
    def __init__(self):
        super(CaseLightsWindow, self).__init__()
        self.ui = Ui_CaseLights()
        self.ui.setupUi(self)
        self.setupButtons()
        self.workers = set()
        self.connection = comm.setup()

    def setupButtons(self):
        self.ui.rgbButton.clicked.connect(partial(self.startWorker, RGBStrategy))
        self.ui.pulseButton.clicked.connect(partial(self.startWorker, PulseStrategy))
        self.ui.whiteButton.clicked.connect(partial(self.startWorker, WhiteStrategy))
        self.ui.clearButton.clicked.connect(partial(self.startWorker, ClearStrategy))

    def startWorker(self, strategy):
        worker = Worker()
        worker.run_in_thread(strategy, self.connection, self.backgroundProcessDone)
        self.workers.add(worker)

    def backgroundProcessDone(self, worker):
        log("Done!")
        self.workers.remove(worker)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = CaseLightsWindow()
  window.show()
  sys.exit(app.exec_())

