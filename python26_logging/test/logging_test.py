#coding:utf-8
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='test.log')

class HelloFilter(logging.Filter):

    #overwrite filter method, 最好先看看LogRecord这个类
    def filter(self, record):
        if record.msg.find('hello') > -1:
            return 0
        return 1

logger.addFilter(HelloFilter())

logger.info("hello")
logger.info("hello boy")
logger.info("hi girl")


#how record error
try:
    print err
except Exception as e:
    logging.exception("")
