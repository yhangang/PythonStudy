# -*- coding: utf-8 -*-  
import tushare as ts
'''
api详见官网http://tushare.org/index.html
'''
print ts.__version__

'''
获取历史K线数据
'''
df = ts.get_hist_data('600848')     #获取日k线数据
ts.get_hist_data('600848',ktype='W')     #获取周k线数据
ts.get_hist_data('600848',ktype='M')    #获取月k线数据
ts.get_hist_data('600848',ktype='5')    #获取5分钟k线数据
ts.get_hist_data('600848',ktype='15')   #获取15分钟k线数据
ts.get_hist_data('600848',ktype='30')   #获取30分钟k线数据
ts.get_hist_data('600848',ktype='60')    #获取60分钟k线数据
ts.get_hist_data('sh')   #获取上证指数k线数据,其它参数与个股一致,下同

ts.get_hist_data('sz')      #获取深圳成指k线数据 ts.get_hist_data('hs300'）#获取沪深300指数k线数据
ts.get_hist_data('sz50')    #获取上证50指数k线数据
ts.get_hist_data('zxb')     #获取中小板指数k线数据
ts.get_hist_data('cyb')     #获取创业板指数k线数据

'''
获取历史分笔数据
'''
df = ts.get_tick_data('000756','2015-03-27')
df.head(10)

'''
获取实时分笔数据
'''
df = ts.get_realtime_quotes('000581') 
df.head(10)
print df[['code','name','price','bid','ask','volume','amount','time']]

#保存为CSV格式
df = ts.get_hist_data('000875')#直接保存
df.to_csv('c:/day/000875.csv')#选择保存
df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])
#保存为Excel格式
df = ts.get_hist_data('000875')#直接保存
df.to_excel('c:/day/000875.xlsx')#设定数据位置（从第3行，第6列开始插入数据）
df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)
#保存为HDF5文件格式
df = ts.get_hist_data('000875')
df.to_hdf('c:/day/hdf.h5','000875')
#保存为JSON格式
df = ts.get_hist_data('000875')
df.to_json('c:/day/000875.json',orient='records')

'''
存入数据库
pandas提供了将数据便捷存入关系型数据库的方法，在新版的pandas中，
主要是已sqlalchemy方式与数据建立连接，支持MySQL、Postgresql、Oracle、MS SQLServer、SQLite等主流数据库。
本例以MySQL数据库为代表，展示将获取到的股票数据存入数据库的方法,
其他类型数据库请参考sqlalchemy官网文档的create_engine部分。
'''
from sqlalchemy import create_engine
df = ts.get_tick_data('600848',date='2014-12-22')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')
#存入数据库
df.to_sql('tick_data',engine)
#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')






'''
股票分数数据
行业分类
ts.get_industry_classified()
概念分类，所有股票炒作概念，比如苹果、特斯拉等
ts.get_concept_classified()
地域分类
ts.get_area_classified()
中小板分类
ts.get_sme_classified()
创业板分类
ts.get_gem_classified()
风险警示板分类
ts.get_st_classified()
沪深300成份股及权重
ts.get_hs300s()
上证50成份股
ts.get_sz50s()
'''


'''
基本面数据
沪深股票列表（基础数据，沪深所有股票情况）
ts.get_stock_basics()
业绩报告（主表）
#获取2014年第3季度的业绩报表数据
ts.get_report_data(2014,3)
盈利能力数据
#获取2014年第3季度的盈利能力数据
ts.get_profit_data(2014,3)
营运能力数据
#获取2014年第3季度的营运能力数据
ts.get_operation_data(2014,3)
成长能力数据
ts.get_growth_data(2014,3)
偿债能力数据
ts.get_debtpaying_data(2014,3)
现金流量数据
ts.get_cashflow_data(2014,3)
'''

'''
宏观经济数据
目前宏观经济数据主要包括以下方面：
金融信息数据
国民经济数据
价格指数数据
景气指数数据
对外经济贸易数据
'''



















