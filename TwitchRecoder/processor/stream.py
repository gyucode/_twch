from streamlink import Streamlink
import subprocess

def stream(url):
    session = Streamlink()
    streams = session.streams(url)

# https://vod-secure.twitch.tv/8ed86bb20949caaad377_lck_korea_190835892_1515980409/chunked/index-dvr.m3u8

subprocess.call(["streamlink", "--twitch-disable-hosting", "--twitch-disable-ads", "twitch.tv/" + 'lck_korea','best', "-o", "foo.ts"]) 
