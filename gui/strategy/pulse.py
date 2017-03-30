from base import BaseStrategy
from util import log
import comm

class PulseStrategy(BaseStrategy):
    def execute(self, connection):
        comm.sendToArduino(connection, 'pulse')
        self.finished.emit()
