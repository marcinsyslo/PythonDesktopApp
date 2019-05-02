import wx
import json


class SettingsFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Settings", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Spectrum settings"), wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Chart dpi", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer9.Add(self.m_staticText3, 0, wx.ALL, 5)

        values = self.load_settings_from_file()  # These values are load from file!

        self.dpi_value_box = wx.SpinCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, str(values["dpi"]), wx.DefaultPosition, wx.DefaultSize,
                                         wx.SP_ARROW_KEYS, 60, 150, 0)
        bSizer9.Add(self.dpi_value_box, 0, wx.ALL, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Image format", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer11.Add(self.m_staticText4, 0, wx.ALL, 5)

        image_format_box_choices = [u"jpg", u"pdf", u"png"]
        image_format_box_choices_numbers = {"jpg": 0, "pdf": 1, "png": 2}      # Change to one operation at impl class
        self.image_format_box = wx.Choice(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          image_format_box_choices, 0)

        self.image_format_box.SetSelection(image_format_box_choices_numbers[values["image_format"]])
        bSizer11.Add(self.image_format_box, 0, wx.ALL, 5)

        bSizer8.Add(bSizer11, 1, wx.EXPAND, 5)

        sbSizer4.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer4, 1, wx.ALL, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Others"), wx.VERTICAL)

        bSizer91 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText31 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Chart X unit", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        bSizer91.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.chart_X_unit_text = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, values["chartX_unit"], wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer91.Add(self.chart_X_unit_text, 0, wx.ALL, 5)

        sbSizer5.Add(bSizer91, 1, wx.EXPAND, 5)

        bSizer911 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText311 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Chart Y unit", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText311.Wrap(-1)
        bSizer911.Add(self.m_staticText311, 0, wx.ALL, 5)

        self.chart_Y_unit_text = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, values["chartY_unit"], wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer911.Add(self.chart_Y_unit_text, 0, wx.ALL, 5)

        sbSizer5.Add(bSizer911, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer5, 1, wx.ALL, 5)

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
        self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
        m_sdbSizer2.Realize()

        bSizer3.Add(m_sdbSizer2, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_sdbSizer2Cancel.Bind(wx.EVT_BUTTON, self.cancel_operation)
        self.m_sdbSizer2OK.Bind(wx.EVT_BUTTON, self.set_settings)

    @staticmethod
    def load_settings_from_file():
        # Default values:
        values = {"dpi": 80,
                  "image_format": ".png",
                  "chartX_unit": "Energy [MeV]",
                  "chartY_unit": "Counting [N]"}
        # Read values from .settings file:

        try:
            file = open(".settings", "r")
            values = json.load(file)
            file.close()
        except IOError as e:
            print(e)
        return values

    def __del__(self):
        pass

    # Virtual event handlers, overide them in derived class
    def cancel_operation(self, event):
        event.Skip()

    def set_settings(self, event):
        event.Skip()
