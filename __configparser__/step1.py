# encoding:utf-8
#pip install configparser进行安装
import configparser

#创建ConfigParser实例  
cf = configparser.ConfigParser()

#读取配置文件
cf.read("config.conf")

#返回配置文件中节序列  '[]'标识的部分
print cf.sections()

#返回某个section中的所有键的序列  
print cf.options('book')

#返回section节中，option的键值  
print cf.get('book','title')  

#返回配置文件某个section的全部配置
print cf.items('book')










