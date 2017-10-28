# encoding: utf-8
from gmsdk.api import StrategyBase

'''
通过掘金量化本地api获取数据，需要安装掘金客户端已经对应的python模块，详见掘金量化官网http://www.myquant.cn/
由于掘金量化是本地运行，可以很方便的和其他模块结合使用
'''
class MyStrategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        super(MyStrategy, self).__init__(*args, **kwargs)
        
        
    def on_login(self):
        print('logined in')
    
    def on_error(self, err_code, msg):
        print('get error: %s - %s' % (err_code, msg))
        
    def on_tick(self, tick):
#         print(tick.strtime + "  price:" + str(tick.last_price))
        pass
    
    def on_bar(self, bar):
        
        print bar.strtime, bar.close,'你呀'
        pass


    def on_backtest_finish(self, indicator):
        # save_bar.replace_last_str("]", self.file_path)    
        pass
    


if __name__ == '__main__':
    strategy = MyStrategy(config_file='config.ini')
    ret = strategy.run()
    print ret
    err = strategy.get_strerror(ret)
    print err.decode('gb2312')
