#! /usr/bin/env python
# coding=utf-8

from IO import *

consoleCode = 'gbk'

def getCommand():
    print "Menu:"
    print "quit, import, query"
    command = raw_input(u"Please input your instructor（指令）: ".encode(consoleCode))
    if command == 'quit':
        return 0
    else:
        return command

def export(data, condition):
    command = raw_input("Would you like to export query result?[Y/N]")
    if command in ['Y', 'y']:
        path = raw_input("Please input the target file:").decode('utf-8')
        if len(path) == 0:
            path = u'result.xls'
        saveFile(path, data, condition)

def query(DB):
    key = raw_input(u'查询类型：'.encode(consoleCode))
    # Miss judgement of key.
    value = raw_input(u'查询数值：'.encode(consoleCode)).decode(consoleCode)
    result = queryRecord(key, value, DB)
    print str(len(result)) + ' result(s) found.'
    for record in result:
        record.show()
    export(result, value)
    pass
