#!/usr/bin/env python
# coding=utf-8

import Tkinter, ttk, tkFileDialog
from inout import *

translation = {
        u'保单号': 'policyID', u'受理号': 'acceptID',
        u'投保单位': 'insureUnit', u'交单日期': 'submitDate', 
        u'赔案编号': 'claimID', u'员工/家庭成员编号': 'memberID',
        u'雇主姓名': 'employer', u'连带(家属)': 'relative',
        u'身份证': 'IDCard', u'银行账户': 'bankAccount',
        u'开户行': 'accountBank', u'联系方式': 'contact',
        u'保险方案': 'insuranceScheme'
    }

class APP():
    def __init__(self):
        self.initDB()
        self.initUI()

    def initDB(self):
        self.db = []
        self.queryResult = []
        self.condition = {}
        pass

    def initUI(self):
        self.root = Tkinter.Tk()
        self.root.title(u'档案查询程序')
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
    
        self.buttonImport = ttk.Button(self.mainframe, text=u'导入', command=self.Import)
        self.buttonExport = ttk.Button(self.mainframe, text=u'导出', command=self.Export)
        self.buttonQuery = ttk.Button(self.mainframe, text=u'查询', command=self.Query)
    
        self.buttonImport.grid()
        self.buttonExport.grid()
        self.buttonQuery.grid()
    
        self.key = Tkinter.StringVar()
        self.comboboxKey = ttk.Combobox(self.mainframe, textvariable=self.key, state='readonly')
        self.comboboxKey['values'] = (u'保单号', u'受理号', u'投保单位', u'交单日期', 
            u'赔案编号', u'员工/家庭成员编号', u'雇主姓名', u'连带(家属)',
            u'身份证', u'银行账户', u'开户行', u'联系方式', u'保险方案'
        )
        self.comboboxKey.grid()
    
        self.value = Tkinter.StringVar()
        self.entryCondition = ttk.Entry(self.mainframe, textvariable=self.value)
        self.entryCondition.grid()
    
        self.labelResult = ttk.Label(self.mainframe)
        self.result = Tkinter.StringVar()
        self.labelResult['textvariable'] = self.result
        self.result.set(u"0条匹配记录")
#        self.result.set(dictToUnicode(self.condition) + u"0条匹配记录")
        self.labelResult.grid()
    
        self.searchInResult = Tkinter.BooleanVar()
        self.check = ttk.Checkbutton(self.mainframe, text=u'在结果中查询',
            variable=self.searchInResult, onvalue=True, offvalue=False)
        self.check.grid()
#    
#        self.textResult = Tkinter.Text(self.mainframe, width=10, height=4)
#        self.textResult['wrap'] = 'word'
#        self.textResult['state'] = 'disabled'
#        self.scroll = ttk.Scrollbar(self.mainframe,
#                orient=Tkinter.VERTICAL, command=self.textResult.yview)
#        self.scroll.grid()
#        self.textResult['yscrollcommand'] = self.scroll.set
#        self.textResult.grid()
#
        self.root.mainloop()

    def Import(self):
        fileName = tkFileDialog.askopenfilename()
        readFile(fileName, self.db)
        pass

    def Export(self):
        fileName = tkFileDialog.asksaveasfilename()
        saveFile(fileName, self.queryResult, self.condition)
        pass

    def Query(self):
        global translation
        key = translation[self.comboboxKey.get()]
        value = self.entryCondition.get()
        SIR = self.searchInResult.get() == 1
        print key, value, SIR
        if not SIR:
            self.condition.clear()
            self.queryResult = self.db[:]
        self.condition[self.comboboxKey.get()] = value
        self.queryResult = queryRecord(key, value, self.queryResult)
        self.result.set(dictToUnicode(self.condition) + unicode(len(self.queryResult)) + u'条匹配记录')
        print len(self.queryResult), 'record(s) found.'
        pass

if __name__ == '__main__':
    app = APP()
