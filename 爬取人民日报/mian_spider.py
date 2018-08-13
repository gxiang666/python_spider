import requests
from bs4 import BeautifulSoup
import io
import time


def get_response(url):
    s = requests.session()
    s.keep_alive = False
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36"
    }
    res = s.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    return res


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("div", class_="box_con")
    if tag is not None:
        content = tag.get_text()
        return content


def main():
    while True:
        t = time.time()
        start_url = "http://news.people.com.cn/210801/211150/index.js?_=%s" % int(round(t * 1000))
        res = get_response(start_url)
        items = res.json()["items"][::2]
        # print(items)
        for item in items:
            url = item["url"]
            html = get_response(url).text
            content = get_content(html)
            # print(content)
            if content is not None:
                with io.open("content.txt", "a", encoding="utf-8") as f:
                    f.write(content)


if __name__ == '__main__':

    main()
