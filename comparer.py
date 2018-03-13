import threading
from web_fetcher import *
from web_fetcher_simple import *
from parser import *
import string
import time

cycle = 60

TYPE_KAIYUAN = "KAIYUAN"
TYPE_DEGUOREXIAN = "DEGUOREXIAN"
TYPE_HUARENJIE = "HUARENJIE"


class comparer(threading.Thread):
    def __init__(self, callback):
        super(comparer, self).__init__()
        self.type_l = [TYPE_KAIYUAN, TYPE_DEGUOREXIAN, TYPE_HUARENJIE]
        self.callback = callback

        self.rets=[[],[],[]]
        self.old_rets=[[],[],[]]

    def run(self):
        while True:
            for i in range(0, 3):
                fetch = web_fetcher_simple(self.type_l[i])
                ret = fetch.process()
                if ret != RET_OK:
                    continue

                psr = parser(self.type_l[i], fetch.pg_src)
                ret = psr.process()
                if ret != RET_OK:
                    continue

                if len(psr.results) == 0:
                    continue

                self.rets[i] = psr.results
                self.compare(i)
                self.old_rets[i] = self.rets[i]
                #time.sleep(1)

            print(self.rets)
            print(self.old_rets)
            time.sleep(cycle)


    def compare(self, index):
        #print(self.type_l[index])
        #print(self.rets[index])
        if len(self.old_rets[index]) == 0:
            if len(self.rets[index]) == 0:
                return RET_OK
            else:
                self.callback(self.type_l[index], self.rets[index][0])
                return RET_OK

        if self.old_rets[index][0] == self.rets[index][0]:
            return RET_OK
        else:
            self.callback(self.type_l[index], self.rets[index][0])
            return RET_OK
