# encoding:utf-8
from datetime import datetime, timedelta
import time
 
'''获取当前日期和时间'''
# dt = datetime.now()
# print dt
# print type(dt)

'''获取指定日期和时间'''
# dt = datetime(2015, 4, 19, 12, 20)
# print dt
# dt = datetime(2015, 4, 19, 12, 20, 38)
# print dt

'''datetime转换为timestamp'''
# dt = "2016-05-05 20:28:54"
# # 转换成时间数组
# timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# # 转换成时间戳
# timestamp = time.mktime(timeArray)
# print timestamp


'''timestamp转换为datetime'''
# t = 1429417200.0
# dt = datetime.fromtimestamp(t) 
# print dt

'''str转换为datetime'''
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print cday

'''datetime转换为str'''
# dt = datetime(2015, 4, 19, 12, 20, 38)
# print dt.strftime('%Y-%m-%d %H:%M:%S')
# print dt.strftime('%Y%m%d')
# print dt.strftime('%H:%M:%S')

'''datetime加减'''
# dt = datetime(2015, 4, 19, 12, 20, 38)
# dt = dt + timedelta(hours=10)
# print dt
# dt = dt + timedelta(days=2, hours=12)
# print dt



