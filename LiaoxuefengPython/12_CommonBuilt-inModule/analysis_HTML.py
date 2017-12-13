from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

def _attr(attrlist,attrname):
    if len(attrlist)==0:
        return None
    for attr in attrlist:
        if attr[0]==attrname:
            return attr[1]
    return None

class MyHTMLParser(HTMLParser):  

    def __init__(self):
        HTMLParser.__init__(self)
        self.__meeting=dict()
        self.meetinglist=[]
        self.__is_record_event=False
        self.__is_record_time=False
        self.__is_record_location=False
        self.__event_time_str=''

    def handle_starttag(self, tag, attrs):
        if tag=='a':
            if 'python-events' in (_attr(attrs,'href')):
                self.__is_record_event=True
        if tag=='time':
            self.__is_record_time=True
        if tag=='span':
            if _attr(attrs,'class')=='event-location':
                self.__is_record_location=True                

    def handle_endtag(self, tag):
        if tag=='time':
            if self.__is_record_time:
                self.__meeting['time']=self.__event_time_str
                self.__is_record_time=False
                self.__event_time_str=''

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.__is_record_event:
            self.__meeting['name']=data
            self.__is_record_event=False
        if self.__is_record_time:
            self.__event_time_str+=str(data)
        if self.__is_record_location:
            self.__meeting['location']=data
            self.meetinglist.append(self.__meeting)
            self.__meeting={}
            self.__is_record_location=False

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

#测试
URL='https://www.python.org/events/python-events/'

with request.urlopen(URL) as f:
    data=f.read()

parser=MyHTMLParser()
parser.feed(data.decode('UTF-8'))

for idx,event in enumerate(parser.meetinglist):
    print('---event%s---'%(idx+1))
    print('name: ',event['name'])
    print('time: ',event['time'])
    print('location: ',event['location'])
