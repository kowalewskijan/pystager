import time
import progressbar
from multiprocessing import Process


class Progress(object):
    def _infinity(self):
        val = 0
        while True:
            yield val
            val += 1

    def _progress_func(self):
        widget = [progressbar.BouncingBar()]
        bar = progressbar.ProgressBar(widgets=widget)
        while True:
            for i in bar(self._infinity()):
                time.sleep(0.1)

    def start(self):
        self.proc = Process(target=self._progress_func,)
        self.proc.start()

    def stop(self):
        self.proc.terminate()
