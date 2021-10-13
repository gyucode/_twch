from TwitchRecoder.core.constants import Data
from logging import INFO
from TwitchRecoder.common.logger import Logger as Log
from TwitchRecoder.processor.csv_manager import CsvManager
from TwitchRecoder.processor.stream_info import StreamInfo
from TwitchRecoder.processor.stream import stream
from TwitchRecoder.core.constants import Constants
# import multiprocessing
import time

TAG ='Worker'

class Worker:
    def __init__(self):
        """
        :param parser_process: Reference to a ParserProcess instance.
        :type parser_process: ParserProcess.
        """
        # multiprocessing.Process.__init__(self)
        # self._exit = multiprocessing.Event()
        self.is_run = False


    def start(self):
        if self.is_run == False:
            self.is_run = True
            self.run()


    def stop(self):
        #Signals the process to stop acquiring data.
        if self.is_run:
            self.is_run = False

    def is_running(self):  
        return self.is_run

    def run(self):
        """[summary]
            # step1. Get user data from csv 
            # step2. check user info from twitch
            # step3. Update csv data
            # step4. Make m3u8 url
            # step5. Start Download
            # step6. Repeat step 1~ 4 
        """


        # tmp = 0
        # test_lst = ["ddahyoni",0,0,0,0,0,0] 
        # test_lst2 = ["c","c","c","c","c","c","c"]
        # csv_mngr = CsvManager(Constants.csv_sweeps_export_path)
        # if csv_mngr.is_init:
        #     strm_info = StreamInfo()
        #     while self.is_run:
        #         # step1. Get user data from csv 
        #         for i in range(1,7):
        #             test_lst[i] =str(tmp+i)
        #             # lst[i] =(tmp+i)

        #         # step2. check user info from twitch
        #         username = test_lst[Data.USER_ID.value]
        #         Log.d(TAG,username)
        #         url = strm_info.check_info(username)
        #         Log.d(TAG,url)

        #         # step3. Update csv data
        #         csv_mngr.append(test_lst)
        #         csv_mngr.update(tmp-1,test_lst2)
        #         # step4. Make m3u8 url
        strm_info = StreamInfo()
        url = strm_info.check_info('lck_korea')
        Log.i(TAG,url)
        # stream(url)

        #         # ======
        #         tmp+=1

        #         Log.i(TAG,tmp)
        #         time.sleep(1)
        # else:
        #     Log.e(TAG,"csv manager init error")


