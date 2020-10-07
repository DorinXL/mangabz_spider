import re
import execjs
import requests
import urllib.parse
import os

# os.environ["EXECJS_RUNTIME"] = ‘Phantomjs‘
node = execjs.get()
"""
代码来源于：
https://blog.csdn.net/weixin_40352715/article/details/106588609
学习了js逆向，万分感谢
"""

urllist = []
class Mangabz:
    """
    日本漫画漫画章节图片下载
    """
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                        "Referer": self.url,
                        "Cookie": "image_time_cookie=17115|637270678077155170|2",
                        }

    def get_chapter_argv(self):
        res = requests.get(self.url, headers=self.headers, timeout=10)
        mangabz_cid = re.findall("MANGABZ_CID=(.*?);", res.text)[0]
        mangabz_mid = re.findall("MANGABZ_MID=(.*?);", res.text)[0]
        page_total = re.findall("MANGABZ_IMAGE_COUNT=(.*?);", res.text)[0]
        mangabz_viewsign_dt = re.findall("MANGABZ_VIEWSIGN_DT=\"(.*?)\";", res.text)[0]
        mangabz_viewsign = re.findall("MANGABZ_VIEWSIGN=\"(.*?)\";", res.text)[0]
        return (mangabz_cid, mangabz_mid, mangabz_viewsign_dt, mangabz_viewsign, page_total)

    def get_images_js(self, page, mangabz_cid, mangabz_mid, mangabz_viewsign_dt, mangabz_viewsign):
        url = self.url + "chapterimage.ashx?" + "cid=%s&page=%s&key=&_cid=%s&_mid=%s&_dt=%s&_sign=%s" % (mangabz_cid, page, mangabz_cid, mangabz_mid, urllib.parse.quote(mangabz_viewsign_dt), mangabz_viewsign)
        res = self.session.get(url, headers=self.headers, timeout=10)
        self.headers["Referer"] = res.url
        return res.text

    def run(self):
        mangabz_cid, mangabz_mid, mangabz_viewsign_dt, mangabz_viewsign, page_total = self.get_chapter_argv()

        for i in range(int(page_total)):
            i += 1
            js_str = self.get_images_js(i, mangabz_cid, mangabz_mid, mangabz_viewsign_dt, mangabz_viewsign)
            imagesList = execjs.eval(js_str)
            # print(imagesList[0])
            urllist.append(imagesList[0])


# if __name__ == '__main__':
#     # mangabz = Mangabz("http://www.mangabz.com/m17115/")
#     mangabz = Mangabz("http://www.mangabz.com/m43328/")
#     mangabz.run()
#     print(urllist)

