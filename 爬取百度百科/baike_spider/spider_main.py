# _*_coding:utf-8_*_
import url_manager, html_downloader, html_parser, html_outputer, time


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPsrser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print
                'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                self.outputer.output_html()

                if count == 100000000000000000:
                    break
                count = count + 1
                time.sleep(2)

            except:
                print
                'craw fail'


if __name__ == "__main__":
    # 爬虫入口页面
    root_url = 'https://baike.baidu.com/item/%E8%85%BE%E8%AE%AF'
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)