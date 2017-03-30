from base import BaseStrategy
from util import log
import comm

class WhiteStrategy(BaseStrategy):
    def execute(self, connection):
        comm.sendToArduino(connection, 'white')
        self.finished.emit()
