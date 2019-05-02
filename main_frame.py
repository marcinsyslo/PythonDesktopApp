import wx


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Aplikacja", pos=wx.DefaultPosition,
                          size=wx.Size(800, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainPanel = MainAppPanel(self)
        self.mainPanel.Hide()
        mainSizer.Add(self.mainPanel, flag=wx.EXPAND, proportion=1, border=1)

        self.menuMain = wx.MenuBar(0)
        self.menuMainFile = wx.Menu()
        self.menuMainFileOpen = wx.MenuItem(self.menuMainFile, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuMainFile.Append(self.menuMainFileOpen)

        self.menuMainFileSave = wx.MenuItem(self.menuMainFile, wx.ID_ANY, u"Save As..." + u"\t" + u"Ctrl + S",
                                            wx.EmptyString, wx.ITEM_NORMAL)
        self.menuMainFile.Append(self.menuMainFileSave)
        self.menuMainFileSave.Enable(False)

        self.menuMainFile.AppendSeparator()

        self.menuMainFileExit = wx.MenuItem(self.menuMainFile, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuMainFile.Append(self.menuMainFileExit)

        self.menuMain.Append(self.menuMainFile, u"File")

        self.menuMainEdit = wx.Menu()
        self.menuMainEditSettings = wx.MenuItem(self.menuMainEdit, wx.ID_ANY, u"Settings", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self.menuMainEdit.Append(self.menuMainEditSettings)

        self.menuMain.Append(self.menuMainEdit, u"Edit")

        self.menuMainView = wx.Menu()
        self.menuMainViewSpectrum = wx.MenuItem(self.menuMainView, wx.ID_ANY, u"Spectrum", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self.menuMainViewSpectrumFit = wx.MenuItem(self.menuMainView, wx.ID_ANY, u"Fit Spectrum", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self.menuMainView.Append(self.menuMainViewSpectrum)
        self.menuMainView.Append(self.menuMainViewSpectrumFit)
        self.menuMainViewSpectrum.Enable(False)
        self.menuMainViewSpectrumFit.Enable(False)

        self.menuMain.Append(self.menuMainView, u"View")

        self.menuMainHelp = wx.Menu()
        self.menuMainHelpAbout = wx.MenuItem(self.menuMainHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuMainHelp.Append(self.menuMainHelpAbout)

        self.menuMain.Append(self.menuMainHelp, u"Help")

        self.SetMenuBar(self.menuMain)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.menu_item_open, id=self.menuMainFileOpen.GetId())
        self.Bind(wx.EVT_MENU, self.menu_item_save, id=self.menuMainFileSave.GetId())
        self.Bind(wx.EVT_MENU, self.menu_item_exit, id=self.menuMainFileExit.GetId())
        self.Bind(wx.EVT_MENU, self.menu_edit_settings, id=self.menuMainEditSettings.GetId())
        self.Bind(wx.EVT_MENU, self.menu_view_spectrum, id=self.menuMainViewSpectrum.GetId())
        self.Bind(wx.EVT_MENU, self.menu_view_spectrum_fit, id=self.menuMainViewSpectrumFit.GetId())
        self.Bind(wx.EVT_MENU, self.menu_help_about, id=self.menuMainHelpAbout.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def menu_item_open(self, event):
        event.Skip()

    def menu_item_save(self, event):
        event.Skip()

    def menu_item_exit(self, event):
        event.Skip()

    def menu_edit_settings(self, event):
        event.Skip()

    def menu_view_spectrum_fit(self, event):
        event.Skip()

    def menu_view_spectrum(self, event):
        event.Skip()

    def menu_help_about(self, event):
        event.Skip()


class MainAppPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetMinSize(wx.Size(1800, 800))

        mainPanelSizer = wx.GridSizer(0, 2, 0, 0)

        secPanelSizer = wx.BoxSizer(wx.VERTICAL)

        textSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Spectrum data"), wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(textSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)

        self.m_staticText2.Wrap(-1)
        textSizer.Add(self.m_staticText2, 0, wx.ALL, 5)

        secPanelSizer.Add(textSizer, 1, wx.EXPAND, 5)

        buttonSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Export data"), wx.VERTICAL)

        self.m_button2 = wx.Button(buttonSizer.GetStaticBox(), wx.ID_ANY, u" Export data to txt file",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        buttonSizer.Add(self.m_button2, 0, wx.ALL, 5)

        secPanelSizer.Add(buttonSizer, 0, wx.EXPAND, 5)

        mainPanelSizer.Add(secPanelSizer, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 5)

        imageMainSizer = wx.BoxSizer(wx.VERTICAL)

        imageSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Spectrum"), wx.VERTICAL)

        self.graph = wx.StaticBitmap(imageSizer.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.Point(1, 1),
                                     wx.DefaultSize, 0)
        self.graph.SetMinSize(wx.Size(1000, 1000))

        imageSizer.Add(self.graph, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        imageMainSizer.Add(imageSizer, 1, wx.BOTTOM | wx.EXPAND, 5)

        mainPanelSizer.Add(imageMainSizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.SetSizer(mainPanelSizer)
        self.Layout()
        mainPanelSizer.Fit(self)

        # Connect Events
        self.Bind(wx.EVT_UPDATE_UI, self.update)
        self.m_button2.Bind(wx.EVT_BUTTON, self.export_data)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def update(self, event):
        event.Skip()

    def export_data(self, event):
        event.Skip()
