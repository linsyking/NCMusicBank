# Netease Cloud Music Bank

Automatically save the daily recommended songs to a playlist.

---

## Getting Started

Install [NeteaseCloudMusicAPI](https://github.com/Binaryify/NeteaseCloudMusicApi).

Run it on your server:

```bash
node app.js
```

Also install `python3` and `schedule` module.

```bash
pip3 install schedule
```

Now clone this repository on your server:

```bash
git clone https://github.com/linsyking/NCMusicBank
```

Set your account in `main.py`.

You can also change the time to do the job by modifying `SAVE_TIME`. The default time is 12:00 AM.
