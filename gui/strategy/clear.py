from base import BaseStrategy
from util import log
import comm

class ClearStrategy(BaseStrategy):
    def execute(self, connection):
        comm.sendToArduino(connection, 'clear')
        self.finished.emit()
