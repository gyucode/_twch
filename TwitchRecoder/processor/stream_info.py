import hashlib
import datetime
import requests
import json
from http import HTTPStatus
from TwitchRecoder.common.logger import Logger as Log
from TwitchRecoder.core.constants import Constants, Data, Err, Ret
from dateutil.parser import parse

TAG = 'stream_info'

class StreamInfo:
    """Check streamer, channel status.
    """
    def __init__(self):
        pass
    
    def do_request(self, _header, _url, _data, _timeout):
        # TODO : get_uniq_id와 get_channel_info의 request 중복처리
        pass
    
    def is_user_login(self, username, id=None):
        pass

    def get_user_info(self, username, id=None):
        pass
    
    def get_stream_info(self, username, id=None):
        pass


    def _get_uniq_id(self, _username):
        """Get unique ID from username
        Args:
            _username (str): streammer ID
        Returns:
            err (enum): return error code
            value (any): return data  
        """
        try:
            res = requests.get(f"https://api.twitch.tv/kraken/users?login={_username}", headers=Constants.header, timeout=Constants.timeout)
            # res = requests.get(f"https://api.twitch.tv/helix/users/extensions/list", headers=Constants.header, timeout=Constants.timeout)
            
            # check response status 
            if res.status_code != HTTPStatus.OK:
                return Err.HTTPStatus, res.status_code
            else:
                json_object = json.loads(res.content)
                return json_object
                user_info = json_object.get("users")
                #  check user data exist.
                if user_info:
                    ret = Err.NO_UNIQ_ID
                    for item in user_info:
                        if "_id" in item:
                            uniq_id = item.get("_id")
                            ret = Err.SUCCESS
                    return ret, uniq_id
                else:
                    return Err.NO_USERINFO, user_info
        except:
            return Err.UNKNOWN, ''

    def _get_channel_info(self, _uniq_id):
        """Get channel info from unique ID
        Args:
            _uniq_id (str): streamer unique ID

        Returns:
            err (enum): return error code
            value (any): return data  
        """
        res = requests.get(f"https://api.twitch.tv/kraken/streams/{_uniq_id}", headers=Constants.header, timeout=Constants.timeout)
        if res.status_code != HTTPStatus.OK:
            return Err.HTTPStatus, res.status_code
        else:
            json_object = json.loads(res.content)
            return json_object
            stream_value = json_object.get("stream")
            if stream_value:
                ret = Err.NO_CAHNNEL_INFO
                for item in stream_value:
                    if 'channel' in item:
                        ch_info = stream_value.get('channel')
                        ret =Err.SUCCESS
                return ret, ch_info
            else:
                return Err.NO_STREAM, stream_value

    def _make_url(self, username, uniq_id):
        ret, value  = self._get_channel_info(uniq_id)
        if ret is Err.SUCCESS:
            date = value.get('created_at')
            url = self.makem3u8(date, username, uniq_id)
            return url
        else:
            msg = self._make_url.__name__ + ':' + ret.name
            Log.e(TAG, msg)
            return None


    def check_info(self, _username, uniq_id=None):
        if uniq_id is None:
            ret, _uniq_id = self._get_uniq_id(_username)
            if ret is Err.SUCCESS:
                url= self._make_url(_username, _uniq_id)
                if url is not None:
                    return url
            else:
                Log.e(TAG, ret.name)
        else:
            url= self._make_url(_username, uniq_id)
            if url is not None:
                return url

        return None

stream_info = StreamInfo()
# info = stream_info._get_uniq_id('ronaronakr')
info = stream_info._get_uniq_id('mmange2')

print(info)
# 38060540
# info = stream_info._get_channel_info(38060540)
# print(info)
# stream_info._get_channel_info()