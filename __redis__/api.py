# encoding:utf-8
#pip install redis进行安装
import redis
'''
python连接redis示例
'''

r = redis.StrictRedis(host='192.168.231.162', port=6379) 

r.set('foo', 0)
print(r.get('foo').decode('UTF-8'))
r.incr('foo')
print(r.get('foo').decode('UTF-8'))

# r.delete("list")
# 
# print(r.rpush("list","aaa"))
# r.rpush("list","bbb")
# r.rpush("list","ccc")
# print(r.lpop("list"))
# r.rpush("list","ddd")
# print(r.lrange("list",0,10))

# r.delete("set")
# print(r.sadd("set","aaa"))
# r.sadd("set","bbb")
# r.sadd("set","ccc")
# print(r.sadd("set","ddd"))
# print(r.smembers("set"))
# print(r.scard("set"))
# 
# s=r.lpop("lissdt")
# print(type(s))
# print(str(s).strip(' '))
