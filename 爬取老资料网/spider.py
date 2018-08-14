# _*_coding:utf-8_*_

import requests
from bs4 import BeautifulSoup
import io


def get_res(url):
    s = requests.session()
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36"
    }
    r = s.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    return r.text


def get_month_urls(html):

    soup = BeautifulSoup(html, "html.parser")
    urls_list = soup.find("div", id="box").find_all("a")
    # print(urls_list)
    for i in urls_list:
        # 某一月的url
        url = i.get("href")
        # print(url)
        resp = get_res(url)
        get_day_urls(resp)
        # break


def get_day_urls(html):

    soup = BeautifulSoup(html, "html.parser")
    urls_list = soup.find("div", class_="c_m").find_all("a")
    for i in urls_list:
        # 某一天的url
        real_url = i.get("href")
        print(real_url)
        # break
        response = get_res(real_url)
        bs = BeautifulSoup(response, "html.parser")
        page_urls_list = bs.find("div", id="box").find_all("a")
        for page_urls in page_urls_list:
            # print(page_urls)
            page_url = page_urls.get("href")
            # print(page_url)
            # break
            page_html = get_res(page_url)
            bsp = BeautifulSoup(page_html, "html.parser")
            content = bsp.find("div", class_="main").get_text()
            # print(content)
            with io.open("ribao.txt", "a", encoding="utf-8") as f:
                f.write(content)
                # break
        # break

def main():
    start_url = 'http://www.laoziliao.net/rmrb/'
    res = get_res(start_url)
    get_month_urls(res)


if __name__ == '__main__':
    main()
