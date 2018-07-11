本机mysql用户密码:
mysql -uroot -pxinghang
使用brew安装:
mysql路径: /usr/local/Cellar/mysql/5.7.17/
mysql默认配置文件路径:/usr/local/Cellar/mysql/5.7.17/support-files/my-default.conf
mysql默认data路径: /usr/local/var/mysql


ubuntu14.04
安装mysql5.7
wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
sudo dpkg -i mysql-apt-config_0.6.0-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server

# 创建数据库
CREATE DATABASE 数据库名称
# 删除数据库
DROP DATABASE 数据库名称
# 查看当前所有数据库
SHOW DATABASES
# 查看表字段详情
desc tablename;
# 修改字段名称
alter table tb_name change 修改前字段 修改后字段 NOT NULL DEFAULT ''
# 修改字段属性
alter table 表名 modify 字段 修改的属性；
alter table help_advert modify addr varchar(255) NOT NULL DEFAULT '';

alter table [表名] add 字段名 single default 0 增加数字字段，单精度型，缺省值为0

# 表的导出与导入
mysqldump:
mysqldump  -u ktvsky -p098f6bcd4621d373cade4e832627b4f6 -P 3306 -h 10.10.146.167 myktv archive_order > archive_order.sql
-u: 用户名， -p: 密码  -P: 端口  -h: 远程服务IP 

scp work@120.132.55.163:/home/work/archive_order.sql archive_order.sql
(scp -p 3026 stage@101.254.157.124:/home/stage/o2o_spider_song.sql o2o_spider_song.sql)
!my
# 导入
use myktv
source /home/xinghang/archive_order.sql
# 导出一个表
mysqldump -uroot -h10.9.138.23 -p098f6bcd4621d373cade4e832627b4f6 kugou singer < qq_singer2.sql
# mysqldump -u 用户名 -p 数据库名 > 导出的文件名

select ktv_id, sum(total_fee)/100 as sum_total_fee from archive_order \
where state=2 and channel in (0, 1) and tp not in (1, 2, 7) and  \
finish_time >= '2016-02-16 00:00:00' and finish_time <= '2016-02-16 23:59:59' \
group by ktv_id order by sum_total_fee desc limit 10;

select ktv_id, MIN(finish_time) as first_order_time from archive_order group by ktv_id order by first_order_time desc limit 10;

select sum(total_fee)/100 as sum_total_fee from archive_order where ktv_id = 87603 and state = 2 and channel in (0, 1) and tp not in (1, 2, 7) and finish_time >= '2017-02-19 00:00:00' and finish_time <= '2017-02-19 23:59:59'

select sum(total_fee)/100 as sum_total_fee, count(*) as cnt from archive_order where tp in (1, 2, 7) group by tp

# 导出mysql数据:
# -e : 执行各种sql操作
mysql -e中 v的作用: 显示语句本身：-v; 增加查询结果行数：-vv ; 增加执行时间：-vvv; (http://blog.csdn.net/feeltouch/article/details/46643065)
mysql -u ktvsky -p098f6bcd4621d373cade4e832627b4f6 -P 3306 -h 10.9.192.10 ktv_bar -e 'select * from music_order where sp_id != 6 and state =1' > o.txt
mysql -uroot -pthunder5166 songs -e 'select thunder_id, name, artist1, ori_ks_url, bt_ks_url, krc_ks_url state from thunder_song where ori_ks_url !=''' > o.txt


关于offset:
select * from kugou_singer limit 10 offset 0  #从1开始
select * from kugou_singer limit 10 offset 10 #从11开始
以上的效率极差, 对于大表而言, 应该先where, 在limit
eg:
select * from o2o_spider_song where id>1000000 limit 100;
它的效率远远高于:
select * from o2o_spider_song limit 1000 offset 1000000;

# 查看创建表的结构
show create table 表名;

# \G: 将查到的结构旋转90度， 变成纵向；
explain select * from music_order 
where create_time > '2018-05-14' 
and create_time < '2018-05-15' 
and tp in (1, 2, 6) 
and mac_id='00E07E016962'\G;
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: music_order
         type: range
possible_keys: idx_macid_ct,idx_tp_ct
          key: idx_macid_ct
      key_len: 103
          ref: NULL
         rows: 1
        Extra: Using index condition; Using where
1 row in set (0.03 sec)


#查看mysql所有进程:
show processlist

#未完成事务导致locktable:
select * from information_schema.innodb_trx\G
kill sid

#关于表连接:
http://huaxia524151.iteye.com/blog/1423614
两个表R, S
select * from R,S #笛卡尔积, 相乘
select * from R cross join S 同上

# 分析表
explain

# 索引:

# 建立索引
# create index <索引名> on tableName(列)
create index o2o_spider_song_artist on o2o_spider_song(artist)
create unique index hash on o2o_spider_song(hash) (效果等同于建表时候的UNIQUE KEY `hash` (`hash`))
create index o2o_spider_song_artist_bthash on o2o_spider_song(artist, bthash)
查看表的索引:
show index from o2o_spider_song
删除表的索引:
drop index index_name on table_name

清空表:
delete from tablename
truncate table tablename

查看当前mysql所在端口号:
show global variables like 'port'

update多字段!妈的这你都不会
update o2o_spider_song set bthash = '', btname = '' where bthash != ''

mysql版本
mysql -V

mysql的初步.http://blog.csdn.net/javazejian/article/details/61614366
# NULL条件检索时不能使用=号，必须使用 is 指明查询条件的值为空
# between 1 and 15: 包含1和15;

# 对分组进行数据过滤, 从而指定包括那些分组,排除那些分组,可以用having;
# having: having是进行分组数据的过滤; where: 进行数据过滤是进行行数据的过滤，也就是说在分组前where已过滤了数据;
mysql> select sex, count(id) from user group by sex;
+------+-----------+
| sex  | count(id) |
+------+-----------+
| NULL |         1 |
| 1    |         3 |
| 2    |         1 |
+------+-----------+
3 rows in set (0.00 sec)

mysql> select sex, count(id) from user group by sex having sex is not null;
+------+-----------+
| sex  | count(id) |
+------+-----------+
| 1    |         3 |
| 2    |         1 |
+------+-----------+
# concat(): 函数可以把字符串拼接成一个长字符串,(注意如有任何一个参数为NULL ，则返回值为 NULL。)
# COUNT(*)对表中的行数进行统计，不管列中包含的是NULL值还是非NULL值，都可正常统计出数量
# COUNT(column)对特定列中的具有值的行进行统计，忽略NULL值，
# describe tablename; # 显示标的详细结构;

desc <table_name>
定义浮点类型:
float(6, 1) 最大长度6位, 小数点位1位
group by and having:
select sex ,count(id) from user group by sex having sex is not null
关于concat:
select Concat(username,'(',birthday,')') AS name_birthday  from user where birthday is not null;
一次内连接:
select tm.name, tm.price, od.items_num, (tm.price * od.items_num) AS sum_price from orderdetail AS od inner join items AS tm on od.items_id = tm.id;

#关于index的关键字:
mysql的字段名字竟然不能用index!我真是的醉了.!

关于表连接的一次实例
关于表连接的一次实例
关于表连接的一次实例
关于表连接的一次实例

select * from table1
+------+-------+
| id   | name  |
+------+-------+
|    1 | lee   |
|    2 | zhang |
|    3 | steve |
|    4 | wang  |
+------+-------+
select * from table2;
+------+-------+
| id   | score |
+------+-------+
|    1 |    90 |
|    2 |   100 |
|    3 |    70 |
|    5 |    80 |
+------+-------+
传统连接: 结果集只显示两个表满足查询条件的部分
select * from table1 t1, table2 t2 where t1.id = t2.id;
+------+-------+------+-------+
| id   | name  | id   | score |
+------+-------+------+-------+
|    1 | lee   |    1 |    90 |
|    2 | zhang |    2 |   100 |
|    3 | steve |    3 |    70 |
+------+-------+------+-------+
内连接: 效果等同于传统链接, 这里用on子句指定连接条件，用where子句指定其他限定条件
select * from table1 t1 inner join table2 t2 on t1.id = t2.id;
+------+-------+------+-------+
| id   | name  | id   | score |
+------+-------+------+-------+
|    1 | lee   |    1 |    90 |
|    2 | zhang |    2 |   100 |
|    3 | steve |    3 |    70 |
+------+-------+------+-------+
select * from table1 t1 inner join table2 t2 on t1.id = t2.id where t2.score = 90;
+------+------+------+-------+
| id   | name | id   | score |
+------+------+------+-------+
|    1 | lee  |    1 |    90 |
+------+------+------+-------+
外连接:
左连接:
结果集包括语句中指定的左表的所有行，而不仅仅是满足连接条件的行
如果左表的某行在右表中没有匹配行，在结果集中此行的右表的所有的字段值均为空值null
select * from from table1 t1 left join table2 t2 on t1.id = t2.id;
+------+-------+------+-------+
| id   | name  | id   | score |
+------+-------+------+-------+
|    1 | lee   |    1 |    90 |
|    2 | zhang |    2 |   100 |
|    3 | steve |    3 |    70 |
|    4 | wang  | NULL |  NULL |
+------+-------+------+-------+
左连接查看差别:
select * from table1 t1 left join table2 t2 on t1.id = t2.id WHERE t2.id is null
select count(*) from table1 t1 left join table2 t2 on t1.id = t2.id where t2.id is null (注意是is而不是=)
+------+------+------+-------+
| id   | name | id   | score |
+------+------+------+-------+
|    4 | wang | NULL |  NULL |
+------+------+------+-------+
右连接:
结果集包括语句中指定的右表的所有行, 而不仅仅是满足连接条件的行
如果右表的某行在左表中没有匹配行,在结果集中此行的左表的所有的字段值均为空值null
select * from table1 t1 right join table2 t2 on t1.id = t2.id
+------+-------+------+-------+
| id   | name  | id   | score |
+------+-------+------+-------+
|    1 | lee   |    1 |    90 |
|    2 | zhang |    2 |   100 |
|    3 | steve |    3 |    70 |
| NULL | NULL  |    5 |    80 |
+------+-------+------+-------+
select * from table1 t1 right join table2 t2 on t1.id = t2.id order by t2.score;
+------+-------+------+-------+
| id   | name  | id   | score |
+------+-------+------+-------+
|    3 | steve |    3 |    70 |
| NULL | NULL  |    5 |    80 |
|    1 | lee   |    1 |    90 |
|    2 | zhang |    2 |   100 |
+------+-------+------+-------+
全连接:
包含左右表的所有行
select * from table1 t1 full join table2 t2 on t1.id = t2.id
记忆方式就是左连接左表全, 右连接右表全, 全连接全部全

eg1.左连接的查询操作:
select count(*) from kugou_by_cat k1 left join o2o_spider_song o1 on k1.hash = o1.hash where o1.hash is null;
+----------+
| count(*) |
+----------+
|   204813 |
+----------+
eg2.左连接的更新操作:
update kugou_by_cat k1 left join o2o_spider_song o1 on k1.hash = o1.hash set k1.is_exist = 1 where o1.hash is not null;

关于mysql增删改字段:
添加字段: alter table kugou_by_cat add column is_exist int(11) not null default 0 comment '附加信息'
添加多字段: alter table o2o_spider_song add album_id int(11) not null default 0 , add language int(11) not null default 0
删除字段: alter table kugou_by_cat drop column is_exist;
修改字段名称: alter table kugou_by_cat change re5 is_exist int(11);

一次实例:
o2o_spider_song这个表, 建表时, 我为了避免重复爬取, 将hash值设定成了unique key
后来制定hash进行查询时候, 发现速度缓慢, 然后用create index o2o_spider_song_artist on o2o_spider_song(hash)的方式建立了索引
查询速度果然大增, 可是当我接下show createtable的时候, hash的unique_key的表示没有了, 取而代之的是一个key(KEY `o2o_spider_song_artist_bthash` (`bthash`), o2o_spider_song_hash这个名字是我起的)的标识
这是不是意味着, key和index中间的某种关联呢?
1.建表的时候, key会自动建立index, 无论是PRIMARY KEY, 试试UNIQUE KEY, 还是KEY, index的名字都是定义, 比如
PRIMARY KEY (`id`),
UNIQUE KEY `hash` (`hash`),
KEY `o2o_spider_song_bthash` (`bthash`)
--说道这里为什么刚开始的时候, hash查询会缓慢, 我并不清楚.
2.而当你建立index时, 如果跟建表时候的key的名称发生冲突, 则key类型会被index类型覆盖

#查询:
select count(distinct(hash)) from kugou_by_cat

#mysql插入date类型的数据:
insert into table (name,date,value) values ('魂牵梦萦','2009-06-08 23:53:17','朝秦暮楚');

#mysql导入csv文件
load data infile '/var/lib/mysql-files/30W.csv' into table thunder_song set utf8
fields terminated by '\t' lines terminated by '\n'
(thunder_id, name, artist1, artist2, artist3, artist4, @duration, has_krc, download_link)
set duration=NULLif(@duration,0)
#mysql导入csv文件
load data infile '/var/lib/mysql-files/3333.csv' into table thunder_song character set utf8
fields terminated by '\t' lines terminated by '\n'
(thunder_id, name, artist1, artist2, artist3, artist4, duration, has_krc, download_link)
#mysql导入csv文件
load data infile '/var/lib/mysql-files/179W.csv' into table kugou_krc_song character set utf8
fields terminated by '\t' lines terminated by '\n'
(o2o_id, krc_link, download_link)
#mysql导入csv文件
load data infile '/var/lib/mysql-files/match-all-time.txt' into table thunder_match character set utf8
fields terminated by ';' lines terminated by '\n'
(thunder_id, name, artist, o2o_id, t_duration, o_duration, d_duration)
#将本地的txt文件导入远端远端远端远端的存储, 加上local...
load data local infile '/home/work/all_singer.txt' into table test character set utf8
fields terminated by ',' lines terminated by '\n'
(thunder_id, name)
#将本地的txt文件导入远端远端远端远端的存储, 加上local..., 默认字段对齐
load data local infile '/home/work/o2omusicinfo.txt' into table test character set utf8
fields terminated by '|' lines terminated by '\n'

关于alter的本质:
MySQL在被alter时是可以insert和update的，但是操作会被延迟。
ALTER TABLE运行时会对原表进行临时复制, 在副本上进行更改, 然后删除原表, 再对新表进行重命名
在执行ALTER TABLE时, 其它用户可以阅读原表, 但是对表的更新和修改的操作将被延迟, 直到新表生成为止
新表生成后, 这些更新和修改信息会自动转移到新表上

查看表大小:
mysql> use information_schema;
Database changed
mysql> select data_length, index_length from tables where table_schema='kugou' and table_name = 'o2o_spider_song';

一次工作中的实例查询:
select * from (select * from test order by age desc) as b group by class;

mysql批量执行命令:
mysql -h localhost -u root -p xinghang < /home/xinghang/test.sql
or source /home/xinghang/test.sql
(http://database.51cto.com/art/201107/277687.htm)




select st.store_id, st.sp_id, st.name as '门店', st.grade as '等级', st.province as '省', st.city as '市', st.district as '区', mc.m_c as '机器数' from sp_store as st
left join (select count(1) as m_c, store_id from machine group by store_id) as mc
on st.store_id = mc.store_id
where st.sp_id not in (6, 49, 72, 116, 118, 0)
and mc.m_c > 0
order by grade




        var password = $('input[name=password]').val();
        var account = $('input[name=account]').val();
        var tp = $('select').val();
        $.post(window.location.pathname, {
            password: password,
            account: account,
            tp:tp
        }, function(res) {
            if(res.redirect) {
                window.location.href = res.redirect;
            } else {
                $('input[name=password]').val('');
                $('.hint').css('display', '').text(res.errmsg);
            }
        })
