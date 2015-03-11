#!/usr/bin/env python
# coding=utf-8

class Date:
    def __init__(self, date = (1970, 1, 1)):
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])

    def __unicode__(self):
        year, month, day = unicode(self.year), unicode(self.month), unicode(self.day)
        if self.month < 10:
            month = '0' + month
        if self.day < 10:
            day = '0' + day
        return u"%s/%s/%s" % (year, month, day)

class Item(dict):
    def __init__(self):
        self['inspectionFee'] = 0.0
        self['outpatientFee'] = 0.0
        self['diagnoisisDate'] = Date()
        self['receiptNumber'] = 0
        self['claimAmount'] = 0.0
        self['claimItem'] = u""
        self['claimMoney'] = 0.0
        self['compensationRate'] = 0.0
        self['compensationMoney'] = 0.0

    def __unicode__(self):
        uIns = u"Inspection fee: " + unicode(self['inspectionFee']) + '\n'
        uOut = u"Outpatient fee: " + unicode(self['outpatientFee']) + '\n'
        uDia = u"Diagnoisis date: " + unicode(self['diagnoisisDate']) + '\n'
        uRen = u"Receipt number: " + unicode(self['receiptNumber']) + '\n'
        uCla = u"Claim amount: " + unicode(self['claimAmount']) + '\n'
        uCli = u"Claim item: " + (self['claimItem']) + '\n'
        uClm = u"Claim money: " + unicode(self['claimMoney']) + '\n'
        uCor = u"Compensation rate: " + unicode(self['compensationRate'] * 100) + '%' + '\n'
        uCom = u"Compensation money: " + unicode(self['compensationMoney']) + '\n'
        return uIns + uOut + uDia + uRen + uCla + uCli + uClm + uCor + uCom

    def show(self):
        print unicode(self)

class Record(dict):
    def __init__(self):
        self['policyID'] = u""
        self['acceptID'] = u""
        self['insureUnit'] = u""
        self['submitDate'] = Date()
        self['claimID'] = u""
        self['memberID'] = u""
        self['employer'] = u""
        self['relative'] = u""
        self['IDCard'] = u""
        self['bankAccount'] = u""
        self['accountBank'] = u""
        self['contact'] = u""
        self['insuranceScheme'] = u""
        self['compensationAmount'] = 0.0
        self['items'] = []
    
    def __unicode__(self):
        uPID = u"Policy ID: " + self['policyID'] + '\n'
        uAID = u"Accept ID: " + self['acceptID'] + '\n'
        uInU = u"Insure unit: " + self['insureUnit'] + '\n'
        uSmD = u"Submit date: " + unicode(self['submitDate']) + '\n'
        uCID = u"Cliam ID: " + unicode(self['claimID']) + '\n'
        uMID = u"Member ID: " + unicode(self['memberID']) + '\n'
        uEmp = u"Employer: " + self['employer'] + '\n'
        uRel = u"Relative: " + unicode(self['relative']) + '\n'
        uIDC = u"ID card: " + self['IDCard'] + '\n'
        uBAc = u"Bank account: " + self['bankAccount'] + '\n'
        uAcB = u"Account bank: " + self['accountBank'] + '\n'
        uCon = u"Contact: " + unicode(self['contact']) + '\n'
        uInS = u"Insurance scheme: " + self['insuranceScheme'] + '\n'
        uItN = unicode(len(self['items'])) + u" item(s) involed." + '\n'
        uItem = u""
        for item in self['items']:
            uItem += unicode(item)
        uCAm = u"Compensation amount: " + unicode(self['compensationAmount']) + '\n'
        return uPID + uAID + uInU + uSmD + uCID + uMID + uEmp + uRel + uIDC + uBAc + uAcB + uCon + uInS + uItN + uItem + uCAm

    def show(self):
        print unicode(self)

if __name__ == '__main__':
    d0 = Date()
    print d0
    d0.year = 1994
    d1 = Date((2015, 10, 30))
    print d1.year, d1.month, d1.day
    print d0
