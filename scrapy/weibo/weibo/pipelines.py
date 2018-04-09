import codecs
import json
from weibo.items import TitleSpiderItem
import threading
import sys
import imp
imp.reload(sys)
sys.path.append("..")
import weibo.tools.Global as Global
from scrapy import log
class WeiboPipeline(object):
    lock = threading.Lock()
    file = open(Global.content_dir,'a')
    
    def __init__(self):
        pass

    def process_item(self,item,spider):
        line = json.dumps(dict(item))+'\n'
        log.msg("Yagr", log.INFO)
        log.msg(line, log.INFO)
        try:
            WeiboPipeline.lock.acquire()    
            WeiboPipeline.file.write(line)
        except:
            pass
        finally:
             WeiboPipeline.lock.release()
        return item
    def spider_closed(self,spider):
        pass

class TitlePipeline(object):
    lock = threading.Lock()
    file = open(Global.title_dir,'a')

    def __init__(self):
        pass

    def process_item(self,item,spider):
        title_item = TitleSpiderItem()
        title_item['title'] = item['title']
        title_item['time'] = item['time']
        title_item['url'] = item['url']
        line = json.dumps(dict(title_item))+'\n'
        print("Yagr", log.INFO)
        print(line, log.INFO)
        try:
            TitlePipeline.lock.acquire()
            TitlePipeline.file_title.write(line)
        except:
            pass
        finally:
            TitlePipeline.lock.release()
        return item

    def spider_closed(self,spider):
        pass
