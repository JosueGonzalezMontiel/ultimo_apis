from peewee import *

database= MySQLDatabase(
    'infoapi',
    user='josueweb', password='1234',
    host='192.168.227.130', port=3306
)