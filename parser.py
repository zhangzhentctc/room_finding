from bs4 import BeautifulSoup


TYPE_KAIYUAN = "KAIYUAN"
TYPE_DEGUOREXIAN = "DEGUOREXIAN"
TYPE_HUARENJIE = "HUARENJIE"

XML_PARSER = "html.parser"
RET_OK = 0
RET_ERR = -1
key_words=['慕尼黑', 'Garching']

item_type_ask_dgrx = '出租房屋'
item_type_ask_hrj = '供房'

class parser:
    def __init__(self, type, pg_src):
        self.pg_src = pg_src
        self.type = type

    def init(self):
        self.items = []
        try:
            self.soup = BeautifulSoup(self.pg_src, XML_PARSER)
        except:
            return RET_ERR
        return RET_OK

    def extract(self):
        ## Kai Yuan
        if self.type == TYPE_KAIYUAN:
            columns = self.soup.find_all("a", "s xst")
            for column in columns:
                item = column.string.strip()
                self.items.append(item)

        # De Guo Re Xian
        if self.type == TYPE_DEGUOREXIAN:
            vice_columns = self.soup.find_all("em")
            unit_str_list = []
            for vice_column in vice_columns:
                unit = vice_column.find_all("a")
                if len(unit) != 0:
                    unit_str = unit[0].string
                    unit_str_list.append(unit_str)
            cnt = 0
            vice_items = []
            for unit in unit_str_list:
                if cnt % 3 == 0:
                    state = unit
                if cnt % 3 == 1:
                    type = unit
                if cnt % 3 == 2:
                    time = unit
                    vice_items.append([state, type, time])
                cnt += 1

            columns = self.soup.find_all("a", "s xst")
            main_items = []
            for column in columns:
                main_item = column.string.strip()
                main_items.append(main_item)

            for i in range(0, len(main_items)):
                if vice_items[i][1] == item_type_ask_dgrx:
                    self.items.append(main_items[i])


        # Hua Ren Jie
        if self.type == TYPE_HUARENJIE:
            columns = self.soup.find_all("div", "li_dian hover ")
            for column in columns:
                type_ = column.find_all("font", "xx2")
                type = type_[0].string
                item_ = column.find_all("a")
                item = item_[0].string
                if type == item_type_ask_hrj:
                    self.items.append(item)

        return RET_OK

    def filt(self):
        self.results = []
        for item in self.items:
            matched = False
            for key_word in key_words:
                item_upper = item.upper()
                key_word_upper = key_word.upper()
                if item_upper.find(key_word_upper) == -1:
                    matched = False
                    break
                else:
                    matched = True
            if matched == True:
                self.results.append(item)
        return RET_OK

    def process(self):
        ret = self.init()
        if ret != RET_OK:
            return ret

        ret = self.extract()
        if ret != RET_OK:
            return ret

        ret = self.filt()
        if ret != RET_OK:
            return ret

        return RET_OK

