#coding:utf-8
import sys
sys.path.append("../../")

import python26_logging as logging

logger = logging.getLogger("X")
logging.basicConfig(level=logging.INFO, filename='test.log')

logger1 = logging.getLogger("X.A")
logger2 = logging.getLogger("X.B")

class HelloFilter(logging.Filter):

    #overwrite filter method, 最好先看看LogRecord这个类
    def filter(self, record):
        if record.getMessage().find('hello') > -1:
            return 0
        return 1

logger.addFilter(HelloFilter())

logger.info("hello")
logger.info("hello boy")
logger.info("hi girl")

# print logger.handlers
# print logger.name
# print logger.parent
# print logger.propagate

#how record error
try:
    print err
except Exception as e:
    logger.exception("")
