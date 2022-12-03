#!/usr/bin/env python3
'''
@Author: King
@Date: 2022-12-03 10:45:04
@Email: linsy_king@sjtu.edu.cn
@Url: https://yydbxx.cn
'''

import schedule
import json
import requests
import time

PLAYLIST_ID = "<pid>"
EMAIL = "<email>"
PASSWORD = "<passwd>"

SAVE_TIME = "12:00"


def save():
    print("Start saving...")
    try:
        # First get COOKIE
        COOKIE = json.loads(requests.get(
            f"http://localhost:3000/login?email={EMAIL}&password={PASSWORD}").text)["cookie"]

        # Get the recommended songs
        url = f"http://localhost:3000/recommend/songs"
        songs = json.loads(requests.get(url, data={"cookie": COOKIE}).text)[
            "data"]["dailySongs"]
        songs_id = []
        for song in songs:
            songs_id.append(str(song["id"]))
        song_str = ",".join(songs_id)
        res = requests.get(
            f"http://localhost:3000/playlist/tracks?op=add&pid={PLAYLIST_ID}&tracks={song_str}", data={"cookie": COOKIE}).text
        assert(json.loads(res)["status"] == 200)
        print("Success")
    except Exception as e:
        print("error!", e)


if __name__ == "__main__":
    schedule.every().day.at(SAVE_TIME).do(save)
    while True:
    # Checks whether a scheduled task
    # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
