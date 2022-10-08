import sys
import youtube_dl
from validators.url import url


def extract(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'restrictfilenames': True,
        'outtmpl': 'out/%(title)s-%(id)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list={url})


def validate(url_candidate: str):
    if not url(url_candidate):
        raise Exception("The provided is not an url")
    return url_candidate


def main():
    valid_url = validate(sys.argv[1])
    extract(valid_url)


if __name__ == "__main__":
    main()
