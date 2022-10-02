import sys
from validators.url import url


def get_valid_urls(urls={}):
    for url_candidate in urls:
        if not url(url_candidate):
            urls.remove(url_candidate)

    return urls


def main():
    valid_urls = get_valid_urls(sys.argv)
    print(valid_urls)


if __name__ == "__main__":
    main()
