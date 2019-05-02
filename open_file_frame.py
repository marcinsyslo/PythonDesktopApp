import wx


class OpenFileFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Open File", pos=wx.DefaultPosition, size=wx.Size(420, 75),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(420, 75), wx.Size(420, 75))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.filePath = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                          wx.Size(400, 35), wx.FLP_DEFAULT_STYLE)
        bSizer2.Add(self.filePath, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.filePath.Bind(wx.EVT_FILEPICKER_CHANGED, self.open_file)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def open_file(self, event):
        event.Skip()
