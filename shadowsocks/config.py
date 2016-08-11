import logging

#Config
MYSQL_HOST = 'db.shadowsocks.org'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_DB = 'sspanel'

# Pro node 1 true , others false
PRO_NODE = 1

# comno , transfer diff * 5
COMBO = 1
# Panel Server.
SERVER_HOST = '127.0.0.1'

MANAGE_PASS = 'passwd'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 23333
#BIND IP
#if you want bind ipv4 and ipv6 '[::]'
#if you want bind all of ipv4 if '0.0.0.0'
#if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'rc4-md5'

#LOG CONFIG
LOG_ENABLE = False
LOG_LEVEL = logging.ERROR
LOG_FILE = '/var/log/shadowsocks.log'
