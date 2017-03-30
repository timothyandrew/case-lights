from PyQt5.QtCore import QThread
from functools import partial

class Worker():
    def __init__(self):
        self.workThread = QThread()

    # Given a `strategy` class, instantiate it, and execute its `execute` method
    # in a thread. Call `done_fn` when finished.
    def run_in_thread(self, strategy, connection, done_fn):
        self.strategyInstance = strategy()
        self.strategyInstance.moveToThread(self.workThread)
        self.strategyInstance.finished.connect(self.workThread.quit)
        self.workThread.started.connect(partial(self.strategyInstance.execute, connection))
        self.workThread.finished.connect(partial(done_fn, self))
        self.workThread.start()
