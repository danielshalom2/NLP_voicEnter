# configuration module

import socket

nb=1 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=['80','1883']
usernames = ['',''] # should be modified for HIT
passwords = ['',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
mzs=['matzi/','']
sub_topics =[mzs[nb]+'#','#']
pub_topics = [mzs[nb]+'test', 'test']
ext_man = mzs[nb]+'system/command'
sub_topic = [mzs[nb]+'bearer/accel/status', mzs[nb]+'bearer/belt/status']
pub_topic = mzs[nb]+'system/state'
msg_system = ['normal', 'issue','No issue']
wait_time = 3

broker_ip=brokers[nb]
broker_port=ports[nb]
username = usernames[nb]
password = passwords[nb]
sub_topic = sub_topics[nb]
pub_topic = pub_topics[nb]


# DB init data 
db_name = 'data\\users.db' # SQLite
db_init =  True   #False # True if we need reinit smart home setup
