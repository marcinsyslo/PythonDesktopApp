import wx
import frames


class Main:
    def __init__(self):
        app = wx.App(False)
        frame = frames.MainFrameImpl(None)
        frame.Show(True)
        app.MainLoop()


if __name__ == '__main__':
    Main()
