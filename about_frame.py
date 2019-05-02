import wx


class About(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"About", pos=wx.DefaultPosition, size=wx.Size(300, 200),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel2, wx.ID_ANY,
                                           u"Beta Spectrum Analizer\nVersion Alpha 0.1.0\n© 2019 Pracownia Promieniotwórczości \nNaturalnej Uniewersytetu Śląskiego.",
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        bSizer5.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel2.SetSizer(bSizer5)
        self.m_panel2.Layout()
        bSizer5.Fit(self.m_panel2)
        bSizer4.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
