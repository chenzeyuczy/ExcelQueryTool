#!/usr/bin/env python
# coding=utf-8

from database import *
import xlrd, xlwt

def numberToDate(date):
    date = str(date)
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    return (year, month, day)

def dictToUnicode(condition):
    result = u'筛选条件：\n '
    for key, value in condition.items():
        result += key + '=' + value + '\n'
    return result

def readCell(sheet, row, col, last = None):
    content = sheet.cell(row, col).value
    ctype = sheet.cell(row, col).ctype
    if ctype == xlrd.XL_CELL_EMPTY:
        return last
    elif ctype == xlrd.XL_CELL_TEXT:
        return content
    elif ctype == xlrd.XL_CELL_NUMBER:
        return content
    elif ctype == xlrd.XL_CELL_DATE:
        return xlrd.xldate_as_tuple(content, 0)
    return None

def readFile(fileName, DB = []):
    book = xlrd.open_workbook(fileName)
    db = DB
    for sheet in book.sheets():
        rows, cols = sheet.nrows, sheet.ncols
        record = None
        
        policy = sheet.cell(0, 0).value[4:]
        accept = sheet.cell(1, 2).value[4:]
        unit = sheet.cell(1, 14).value

        submitDate = claimID = memberID = employer = relative = None
        IDCard = bankAccount = accountBank = contact = scheme = None
        inspectionFee = outpatientFee = diagnoisisDate = None
        receiptNumber = claimAmount = claimItem = claimMoney = None
        compensationRate = compensationMoney = compensationAmount = None

        for line in range(rows)[4:-2]:
            if sheet.cell(line, 1).ctype != xlrd.XL_CELL_EMPTY:
                submitDate = readCell(sheet, line, 0, submitDate)
                claimID = readCell(sheet, line, 1, claimID)
                memberID = readCell(sheet, line, 2, memberID)
                employer = readCell(sheet, line, 3, employer)
                relative = readCell(sheet, line, 4)
                IDCard = readCell(sheet, line, 5, IDCard)
                bankAccount = readCell(sheet, line, 6, bankAccount)
                accountBank = readCell(sheet, line, 7, accountBank)
                contact = readCell(sheet, line, 8)
                scheme = readCell(sheet, line, 9, scheme)
                compensationAmount = readCell(sheet, line, 20, compensationAmount)
                if record is not None:
                    db.append(record)
                record = Record()
                record['policyID'] = policy
                record['acceptID'] = accept
                record['insureUnit'] = unit
                record['submitDate'] = Date(numberToDate(submitDate))
                record['claimID'] = unicode(int(claimID))
                record['memberID'] = memberID
                record['employer'] = employer
                record['relative'] = relative
                record['IDCard'] = IDCard
                record['bankAccount'] = bankAccount
                record['accountBank'] = accountBank
                record['contact'] = contact
                record['insuranceScheme'] = scheme
                record['compensationAmount'] = compensationAmount
                # Fill in record info.

            inspectionFee = readCell(sheet, line, 10)
            outpatientFee = readCell(sheet, line, 11)
            diagnoisisDate = readCell(sheet, line, 12, diagnoisisDate)
            receiptNumber = readCell(sheet, line, 13, 0)
            claimAmount = readCell(sheet, line, 14)
            claimItem = readCell(sheet, line, 15)
            claimMoney = readCell(sheet, line, 17)
            compensationRate = readCell(sheet, line, 18)
            compensationMoney = readCell(sheet, line, 19)

            item = Item()
            item['inspectionFee'] = inspectionFee or 0.0
            item['outpatientFee'] = outpatientFee or 0.0
            item['diagnoisisDate'] = Date(diagnoisisDate[0:3])
            item['receiptNumber'] = int(receiptNumber or 0)
            item['claimAmount'] = claimAmount or 0.0
            item['claimItem'] = claimItem or ""
            item['claimMoney'] = claimMoney or 0.0
            item['compensationRate'] = compensationRate or 0.0
            item['compensationMoney'] = compensationMoney or 0.0
            # Fill in item info.

            record['items'].append(item)
        if record is not None:
            db.append(record)
    pass

def queryRecord(key, value, DB):
    result = []
    for record in DB:
        if record[key] == value:
            result.append(record)
    return result

def saveFile(fileName, data, condition = {}):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet')
    sheet.write(0, 0, u'筛选条件')
    row = 1
    for key, value in condition.items():
        sheet.write(0, row, unicode(key) + '=' + unicode(value))
        row += 1

    sheet.write(1, 0, u'保单号')
    sheet.write(1, 1, u'受理号')
    sheet.write(1, 2, u'投保单位')
    sheet.write(1, 3, u'交单日期')
    sheet.write(1, 4, u'赔案编号')
    sheet.write(1, 5, u'员工/家庭成员编号')
    sheet.write(1, 6, u'雇主姓名')
    sheet.write(1, 7, u'连带（家属）')
    sheet.write(1, 8, u'身份证')
    sheet.write(1, 9, u'银行账户')
    sheet.write(1, 10, u'开户行')
    sheet.write(1, 11, u'联系方式')
    sheet.write(1, 12, u'保险方案')
    sheet.write(1, 13, u'检查费')
    sheet.write(1, 14, u'门诊费')
    sheet.write(1, 15, u'诊治日期')
    sheet.write(1, 16, u'收据数量')
    sheet.write(1, 17, u'收据金额/索赔金额')
    sheet.write(1, 18, u'理赔扣减项目/原因')
    sheet.write(1, 19, u'理赔扣减金额')
    sheet.write(1, 20, u'赔付比例')
    sheet.write(1, 21, u'实赔金额')
    sheet.write(1, 22, u'赔付合计')

    line = 2
    for i in range(len(data)):
        sheet.write(line, 0, data[i]['policyID'])
        sheet.write(line, 1, data[i]['acceptID'])
        sheet.write(line, 2, data[i]['insureUnit'])
        sheet.write(line, 3, unicode(data[i]['submitDate']))
        sheet.write(line, 4, data[i]['claimID'])
        sheet.write(line, 5, data[i]['memberID'])
        sheet.write(line, 6, data[i]['employer'])
        sheet.write(line, 7, data[i]['relative'])
        sheet.write(line, 8, data[i]['IDCard'])
        sheet.write(line, 9, data[i]['bankAccount'])
        sheet.write(line, 10, data[i]['accountBank'])
        sheet.write(line, 11, data[i]['contact'])
        sheet.write(line, 12, data[i]['insuranceScheme'])
        sheet.write(line, 22, data[i]['compensationAmount'])
        for item in data[i]['items']:
            sheet.write(line, 13, item['inspectionFee'])
            sheet.write(line, 14, item['outpatientFee'])
            sheet.write(line, 15, unicode(item['diagnoisisDate']))
            sheet.write(line, 16, item['receiptNumber'])
            sheet.write(line, 17, item['claimAmount'])
            sheet.write(line, 18, item['claimItem'])
            sheet.write(line, 19, item['claimMoney'])
            sheet.write(line, 20, item['compensationRate'])
            sheet.write(line, 21, item['compensationMoney'])
            line += 1
        line += 1
    book.save(fileName)

if __name__ == '__main__':
    fileName =  u"2014-11-28中智录入医生发回总.xls"
    print "Import data from " + fileName + " ..."
    DB = []
    readFile(fileName, DB)
    print str(len(DB)) + " record(s) have been imported."

    name1 = u'陈文静'
    print "Search by name " + name1
    match1 = queryByName(name1, DB)
    print str(len(match1)) + " record(s) match."
    for record in match1:
        record.show()

    id1 = u'43042119890104022X'
    print "Search by ID " + id1
    match2 = queryByID(id1, DB)
    print str(len(match1)) + " record(s) match."
    for record in match2:
        record.show()

#    outFile = "testOut.xls"
#    saveFile(outFile, match1, name1)

