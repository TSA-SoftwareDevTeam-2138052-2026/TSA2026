from PySide6.QtCore import QRunnable, Slot, QObject, Signal

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.thread_id = kwargs.get("thread_id", 0)
    
    @Slot()
    def run(self):
        try:
            result = self.fn(self.args, self.kwargs)
        except Exception as e:
            self.signals.error.emit(e)
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit(self.thread_id)

class WorkerSignals(QObject):
    finished = Signal(int) # Thread ID that finished
    error = Signal(object) # In case we error out
    result = Signal(object) # Return the result