from base import BaseStrategy
from util import log
import comm

class RGBStrategy(BaseStrategy):
    def execute(self, connection):
        comm.sendToArduino(connection, 'rgb')
        self.finished.emit()
