import os
from numpy import False_
import pandas as pd
from TwitchRecoder.core.constants import Constants , Err ,Data
from TwitchRecoder.common.logger import Logger as Log
import time

TAG ='CSV'

class CsvManager:
    def __init__(self, csv_path):
        super(CsvManager, self).__init__()
        self.path = csv_path
        self.df_csv =''
        self.csv_header = [name.name for name in Data]
        self.is_init = self.__init()
        

    def __is_csv_file_exist(self, path):
        if os.path.exists(path):  #파일이 있는지 검사
            return True   
        return False
    
    def __check_csv_header(self, header):
        """
        STEP1. Check header names
        """
        ret = Err.SUCCESS
        if header != self.csv_header:
            ret =  Err.UNMATCH_HEADER
            for item in Data:
                if not item.name in header: 
                    ret = Err.INVALID_HEADER
        return ret 

    def __set_datatype(self):
        for i, col in enumerate(self.csv_header) :
            self.df_csv[col].astype(str)

    def __get_csv(self):
        df_csv = pd.read_csv(self.path, header=0)

        header_list = df_csv.columns.values.tolist()
        ret = self.__check_csv_header(header_list)
        if ret is not Err.SUCCESS:
            return False
        else:
            self.df_csv = df_csv
            return True

    def __make_csv(self):
        # TODO: make csv file
        print("DO MAKE CSV!")
        df_csv_w = pd.DataFrame(columns=self.csv_header)
        print(df_csv_w)
        df_csv_w.to_csv(self.path, mode='w', index=False)
        if self.__is_csv_file_exist(self.path):
            self.df_csv = df_csv_w
            self.__set_datatype()
            return True
        return False

    def __init(self):
        if self.__is_csv_file_exist(self.path):
            ret = self.__get_csv()
        else:
            ret = self.__make_csv()

        self.is_init = ret

        return self.is_init

    def __save_to_csv(self):
        self.df_csv.to_csv(self.path, mode='w', index=False)


    def append(self, _list):
        if len(_list) != len(self.csv_header):
            Log.e(TAG, 'Failed add row, invalid length')
            return False
        self.df_csv = self.df_csv.append(pd.Series(_list, index=self.df_csv.columns), ignore_index=True)
        self.__save_to_csv()
        return True

    def read(self, index, to_list=True):
        if to_list:
            data=self.df_csv.loc[index].to_list()
        else:
            data=self.df_csv.loc[index].to_dict()
        self.__save_to_csv()
        return data

    def update(self,row,_list):
       self.df_csv.iloc[row] = _list
       self.__save_to_csv()
       return self.df_csv.iloc[row]




# def main():
#     # csv_manager = CsvManager( Constants.USER_INFO_CSV_PATH )
#     csv_manager = CsvManager( 'haha.csv' )
#     print(csv_manager.init())
#     csv_manager.save_csv()

# if __name__ == "__main__":
#     main()