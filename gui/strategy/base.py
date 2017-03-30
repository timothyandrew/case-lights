from PyQt5.QtCore import QObject, pyqtSignal

class BaseStrategy(QObject):
    finished = pyqtSignal()
