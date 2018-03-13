from comparer import *
import smtplib
from email.mime.text import MIMEText

TYPE_KAIYUAN = "KAIYUAN"
TYPE_DEGUOREXIAN = "DEGUOREXIAN"
TYPE_HUARENJIE = "HUARENJIE"
Kai_Yuan_link = "http://www.kaiyuan.info/forum.php?mod=forumdisplay&fid=92&filter=sortid&sortid=262"
Deguorexian_link = "https://www.dolc.de/forum.php?mod=forumdisplay&fid=14&page=1&filter=typeid&typeid=32"
Huarenjie_link = "https://www.huarenjie.net/deguo/category-122-12-1.html?&areaid=63"

RET_OK = 0
RET_ERR = -1

class send:
    def __init__(self, subject, content):
        self.host = 'smtp.163.com'
        self.username = 'zhangzhentctc@163.com'
        self.passwd = '45600123'
        self.to_list = ['aaronzhenzhang@gmail.com']
        self.subject = subject
        self.content = content

    def send_email(self):
        msg = MIMEText(self.content.encode('utf8'), _subtype='html', _charset='utf8')
        msg['From'] = self.username
        msg['Subject'] = u'%s' % self.subject
        msg['To'] = ",".join(self.to_list)

        try:
            s = smtplib.SMTP_SSL(self.host, 465)
        except:
            print('smtp init fail')
            return RET_ERR

        try:
            s.login(self.username, self.passwd)
        except:
            print('mail login fail')
            return RET_ERR

        try:
            s.sendmail(self.username, self.to_list, msg.as_string())
        except:
            print('mail send fail')
            return RET_ERR

        try:
            s.close()
        except:
            print('mail close fail')
            return RET_ERR

        return RET_OK




def find(type, item):
    if type == TYPE_KAIYUAN:
        place = '开元'
        link = Kai_Yuan_link
    elif type == TYPE_DEGUOREXIAN:
        place = '德国在线-萍聚'
        link = Deguorexian_link
    elif type == TYPE_HUARENJIE:
        place = '华人街'
        link = Huarenjie_link
    else:
        place = 'unknown'
        link = 'unknown'
    subject = "New Room " + str(place)
    content = str(item) + '\n' + link
    s = send(subject, content)
    ret = s.send_email()
    if ret != RET_OK:
        s2 = send(subject, content)
        ret2 = s2.send_email()
    return

comp = comparer(find)

comp.start()

