#!/usr/bin/env python
import wx
import sys
import os
import re
import operator

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"


class MyForm(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY,"Counting")
		panel = wx.Panel(self, wx.ID_ANY)
		self.currentDirectory = os.getcwd()
	 
		openFileDlgBtn = wx.Button(panel, label="Open file")
		openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
	 
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)
		panel.SetSizer(sizer)


	def onOpenFile(self, event):
		dlg = wx.FileDialog(
		    self, message="Choose a file",
		    defaultDir=self.currentDirectory, 
		    defaultFile="",
		    wildcard=wildcard,
		    style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
		    )
		if dlg.ShowModal() == wx.ID_OK:
		    paths = dlg.GetPaths()
		    print "You chose the following file(s):"
		    for path in paths:
		        print path
		dlg.Destroy()

		lines = paths
		num = 0
		dic = {}
		for i in lines:
			dat = open(i, "r").read()
			words = re.findall(r'[a-z]+',dat)
			for word in words:
				if len(word)>3:
				        num=num+1
				        if dic.has_key(word):
				                dic[word]=dic[word]+1
				        else:
				                dic[word]=1

		sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)
		s =str(sorted_dic)
		n =str(num)
		one = 'Number of words with more than 3 letters: '
		two = '\nNumber of occurances of those words: '
		dial = wx.MessageDialog(None,one+n+two+s, 'Info', wx.OK)
        	dial.ShowModal()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
