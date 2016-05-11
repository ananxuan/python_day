#!/usr/bin/env python3
__author__ = 'DSOWASP'
import  logging

# logging 默认输出级别为WARNING,默认格式是日志级别:Logger名称:用户输出消息
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")
"""
输出：
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
"""

# 日志级别、格式、输出位配置

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
"""
输出：
Tue, 10 May 2016 22:40:13 Log.py[line:26] DEBUG debug message
Tue, 10 May 2016 22:40:13 Log.py[line:27] INFO info message
Tue, 10 May 2016 22:40:13 Log.py[line:28] WARNING warning message
Tue, 10 May 2016 22:40:13 Log.py[line:29] ERROR error message
Tue, 10 May 2016 22:40:13 Log.py[line:30] CRITICAL critical message
"""

# 日志格式自定义ke
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
a = "what"
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logging.warning('Protocol problem: %s', 'connection reset', extra=d)