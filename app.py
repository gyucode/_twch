from multiprocessing import freeze_support # 윈도우에서 멀티프로세스 쓸 때

import sys
import os
from TwitchRecoder.common.architecture import Architecture,OSType
# from TwitchRecoder.common.arguments import Arguments
from TwitchRecoder.core.worker import Worker
from TwitchRecoder.common.logger import Logger as Log
from TwitchRecoder.common.logger import LoggerLevel
from TwitchRecoder.core.constants import MinimalPython, Constants

TAG = "app"

class TwitchRecorder:
    def __init__(self, argv=sys.argv):
        freeze_support()
        Log(LoggerLevel.DEBUG,True)
        self._worker = Worker()
        if Architecture.get_os() is OSType.windows:
            pass        

    def run(self):
        if Architecture.is_python_version(MinimalPython.major, minor=MinimalPython.minor):
            Log.i(TAG,"Path:{}".format(os.path.dirname(__file__))) #add
            Log.i(TAG, "Application started")
            Log.d(TAG, "Application started")
            self._worker.start()

        else:
            self._fail()
        self.close()

    def close(self):
        Log.close()
        sys.exit()
               
    @staticmethod
    def _fail():
        txt = str("Application requires Python {}.{} to run".format(MinimalPython.major, MinimalPython.minor))
        Log.e(TAG, txt)


if __name__ == '__main__':
    TwitchRecorder().run()