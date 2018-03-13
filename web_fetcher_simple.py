import requests

TIMEOUT = 10
RET_OK = 0
RET_ERR = -1
TYPE_KAIYUAN = "KAIYUAN"
TYPE_DEGUOREXIAN = "DEGUOREXIAN"
TYPE_HUARENJIE = "HUARENJIE"
Kai_Yuan_link = "http://www.kaiyuan.info/forum.php?mod=forumdisplay&fid=92&filter=sortid&sortid=262"
Deguorexian_link = "https://www.dolc.de/forum.php?mod=forumdisplay&fid=14&page=1&filter=typeid&typeid=32"
Huarenjie_link = "https://www.huarenjie.net/deguo/category-122-12-1.html?&areaid=63"


class web_fetcher_simple:
    def __init__(self, type):
        self.type = type
        if self.type == TYPE_KAIYUAN:
            self.link = Kai_Yuan_link
        if self.type == TYPE_DEGUOREXIAN:
            self.link = Deguorexian_link
        if self.type == TYPE_HUARENJIE:
            self.link = Huarenjie_link

    def init_driver(self):
        return RET_OK


    def get_link(self):
        try:
            self.r = requests.get(self.link)
        except:
            return RET_ERR
        return RET_OK

    def get_src(self):
        try:
            self.pg_src = self.r.text
        except:
            return RET_ERR

        return RET_OK

    def close_driver(self):
        return RET_OK

    def process(self):
        ret = self.init_driver()
        if ret != RET_OK:
            return ret

        ret = self.get_link()
        if ret != RET_OK:
            self.close_driver()
            return ret

        ret = self.get_src()
        if ret != RET_OK:
            self.close_driver()
            return ret

        ret = self.close_driver()
        if ret != RET_OK:
            return ret

        return RET_OK
