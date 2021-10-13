from enum import Enum
from TwitchRecoder.common.architecture import Architecture, OSType
import time
from time import strftime, localtime

class Data(Enum):
    USER_ID = 0     #유저id
    UNIQ_ID = 1     #고유id 
    INFO = 2        #반환된info,
    STATUS = 3      #on/off,
    PATH = 4        #저장경로,
    PID = 5         #pid,
    ERR_DETAIL = 6  #에러코드

class Err(Enum):
    SUCCESS = 0x00

    BASE_STREAMINFO = 0x0100
    UNKNOWN = BASE_STREAMINFO + 0x01
    HTTPStatus = BASE_STREAMINFO + 0x02
    NO_USERINFO = BASE_STREAMINFO + 0x03
    NO_UNIQ_ID = BASE_STREAMINFO + 0x04
    NO_STREAM = BASE_STREAMINFO + 0x05
    NO_CAHNNEL_INFO = BASE_STREAMINFO + 0x06

    BASE_CSV = 0x0200
    UNVALID_CSV_PATH = BASE_CSV + 0x01
    UNMATCH_HEADER = BASE_CSV + 0x02
    INVALID_HEADER = BASE_CSV + 0x03

class Ret:
    CHK  = 0 
    DATA = 1

class Constants:

    # program info
    app_title = 'Twitch Recorder - made by JinHwan'
    app_version = '0.9.9'

    # Log parameters #
    log_export_path = "logged_data"
    log_filename = "{}.log".format(app_title)
    log_max_bytes = 5120
    log_default_level = 1
    log_default_console_log = False
    

    # File parameters for exporting data #
    # sets the slash depending on the OS types
    if Architecture.get_os() is (OSType.macosx or OSType.linux):
       slash="/"
    else:
       slash="\\"
       
    csv_delimiter = "," # for splitting data of the serial port and CSV file storage
    csv_default_prefix = "%Y-%b-%d_%H-%M-%S"#"%H-%M-%S-%d-%b-%Y" # Hour-Minute-Second-month-day-Year
    csv_extension = "csv"
    txt_extension = "txt"
    csv_export_path = "logged_data"
    csv_filename = "UserData" + '.' + csv_extension
    # csv_filename = (strftime(csv_default_prefix, localtime()))#+'_DataLog')
    csv_sweeps_export_path = "{}{}{}".format(csv_export_path,slash,csv_filename)
    # csv_sweeps_filename = "sweep"


    # stream_info
    client_id = "jzkbprff40iqj646a697cyrvl0zt2m6"  # don't change this
    header = {"Client-ID": client_id, "Accept": "application/vnd.twitchtv.v5+json"}
    user_info_url = 'https://api.twitch.tv/kraken/users?login='
    uniq_id_url = 'https://api.twitch.tv/kraken/streams/'
    timeout = 5
    USER_INFO_CSV_PATH ='streamerinfo.csv'

class MinimalPython:
    major = 3
    minor = 2
    release = 0    

def APP_ERROR(ret):
    if ret != Err.SUCCESS:
        print("APP_ERROR = ",ret)
        return False
    else:
        return True