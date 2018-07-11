key:
    del key                                #删除
    keys adc*                              #查找key
    get key                                #获取value
    type key                               #用来获取键值的类型
    exist key                              #是否存在
    ttl key                                #查看剩余生存时间
    rename old_key new_key                 #重命名
    expire key time_len                    #设置key生存时间

string:
    set key value                          #set name 'xinghang'
    setnx key value                        #只有当键值不存在时设置key_value
    mset key1 value1 key2 value2           #批量设置:mset name 'xinghang' addr 'beijing'
    msetnx key1 value2 key1 value2         #批量同上
    get key                                #获得键值
    mget key1 key2                         #获取所有键的值
    srtlen key                             #value的长度
    getrange key num num                   #getrange name 0 -1  (输出:xinghang)

list:
    lpush:  #将一个或多个值插入列表头部，key: 不存在，空列表1会被创建并执行lpush，
            #当key存在但不是列表类型是，返回错误
    rpush key_name value1 value2           #将一个或多个值插入列表尾部，新建一个list并且加入值
    lpop key_name       #从列表头部删除元素， 并返回删除元素
    rpop key_name                          #移除并获取列表最后一个元素
    rpoplpush key_name_1 key_name_2    # 从第一个list的尾部移除元素并添加到第二个list的头部
    lindex key_name index  # 返回list中index位置的元素
    lrange key_name 0 -1                   #输出一个list
    lrange key_name start end   # 返回list指定区间内的元素， 区间以偏移量start end指定
    llen key_name                          #key对应的长度
    lset key index value                   #指定位置的设置list
    ltrim key_name start end  #对一个列表进行修剪，让列表只保留指定区间内的元素，不在区间内的元素将被删除

hash: # 非常适合存储对象
    hset key name "xinghang"
    hsetnx key name "xinghang"
    hmset key filde1 value1 filed1 value2
    hdel key filed1
    hget key filed1
    hmget key filed1 filed2
    hgetall key                            #输出一个对象
    hkeys key                              #获取key对应的所有的哈希字段
    hvals key                              #获取key所对应的所有的哈希值
    hlen  key                              #key所对应的hash字段的个数

set:
    sadd key value
    srem key value1                        #删除
    smemembers key                         #查看一个集合
    scard key                              #长度
    sinter key1 key2                       #交集
    sunion key1 key2                       #并集

zset:
    zadd  key [score name]                 #新建一个zset并且插入值: zadd test_zset  10 xinghagn; zadd test_zset 1 lifeifei
    zrem key name                          #删除
    zcard key                              #长度
    zrange key index1 index2               #输出指定排名区间的name: zrange test_zset 0 1 (输出 lifeifei xinghang)
    zrange key index1 index2  withscores   #同上,带权值
    zscore key name                        #返回这个name的score
    zrank key name                         #返回score排名的index
    zcount key min_score max_score         #返回在权值范围内的name个数


关闭: ./redis-cli shutdown
指定配置文件启动: ./redis-server ../redis-conf
远端连接: redis-cli -h 10.9.36.222

删除指定前缀的key:  redis-cli keys "song_rank_*_99_*" | xargs redis-cli DEL

setnx： 指定的key不存在， 为key设置制定值， 设置成功， 返回1， 失败， 返回0，
redis> EXISTS job        # job 不存在
redis> SETNX job "programmer"      # job 设置成功
redis> SETNX job "code-farmer"     # 尝试覆盖 job ，失败
redis> GET job         # 没有被覆盖