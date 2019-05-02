import wx
import time
import pickle
import json

import main_frame
import open_file_frame
import settings_frame
import about_frame
import spectrum
import chart_creator


class MainFrameImpl(main_frame.MainFrame):
    __spectrum_data = spectrum.Spectrum()  # Loaded spectrum

    def __init__(self, parent):
        super().__init__(parent)

    def menu_item_open(self, event):
        frame = OpenFileFrameImpl(self)
        frame.Show(True)

    def menu_item_save(self, event):
        self.__spectrum_data.save()

    def menu_item_exit(self, event):
        self.Close()

    def menu_edit_settings(self, event):
        frame = SettingsFrameImpl(self)
        frame.Show()

    def menu_view_spectrum_fit(self, event, dpi_default=80, image_format="png"):
        try:
            self.view_spectrum(dpi_default, image_format, fit=True)

        except Exception as e:
            print(e)

    def menu_view_spectrum(self, event, dpi_default=80, image_format="png"):
        try:
            self.view_spectrum(dpi_default, image_format, fit=False)

        except Exception as e:
            print(e)

    def view_spectrum(self, dpi_default, image_format, fit):
        self.mainPanel.Show()
        data = ""
        dpi_value = self.settings_reader(parameter_name="dpi", default_value=dpi_default)
        bmp = wx.Image(chart_creator.get_fig(dpi=dpi_value, image_format=image_format, spectrum=self.__spectrum_data, fit=fit),
                       wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        if fit:
            func = "f(x) = ((x ^ a) + b) * ((e - x) ^ 2)"
            data = func + "\n\n" + str(self.__spectrum_data.get_spectrum_data())

        self.mainPanel.m_staticText2.SetLabelText(data)
        self.mainPanel.graph.SetBitmap(bmp)
        self.Fit()
        self.SetSize((1400, 600))

    @staticmethod
    def settings_reader(parameter_name, default_value):
        value = {}
        try:
            file = open(".settings", "r")
            value = json.load(file)
            file.close()
        except IOError as e:
            print(e)
            return default_value
        return value[parameter_name]

    def menu_help_about(self, event):
        frame = about_frame.About(self)
        frame.Show(True)

    def set_spectrum(self, spectrum_data):
        self.__spectrum_data.set_spectrum(spectrum_data)

    def set_spectrum_obj(self, spectrum_data):
        self.__spectrum_data = spectrum_data


class OpenFileFrameImpl(open_file_frame.OpenFileFrame):

    def __init__(self, parent):
        super().__init__(parent)

    def open_file(self, event):
        t = time.asctime(time.localtime(time.time()))
        file_path = str(self.filePath.GetPath())

        if file_path.endswith(".anb"):

            try:
                top_window = wx.GetApp().TopWindow
                file = open(file_path, "rb")
                spectrum_obj = pickle.load(file)
                self.set_top_window_obj(spectrum_obj, top_window)
            except IOError as e:
                print(e)
                self.Close()
            finally:
                self.Close()

        elif file_path.endswith(".txt"):

            top_window = wx.GetApp().TopWindow
            try:
                file = open(file_path, "r")
                temp = open("temp.txt", "w")

                spectrum_temp = [(float(i.split()[0]), int(i.split()[1])) for i in file]

                self.set_top_window_parameters(spectrum_temp, top_window)
                temp.write(file_path + "\nOpen time: " + t)
                temp.close()
                file.close()

            except Exception as e:
                print("Error: " + str(e))
                self.Close()

            finally:
                top_window.mainPanel.Hide()
                self.Close()

        else:
            print("Incorrect format. Only .txt or .anb")

    @staticmethod
    def set_top_window_parameters(spectrum_data, top_window):
        top_window.menuMainViewSpectrum.Enable(True)
        top_window.menuMainViewSpectrumFit.Enable(True)
        top_window.menuMainFileSave.Enable(True)
        top_window.set_spectrum(spectrum_data)

    @staticmethod
    def set_top_window_obj(spectrum_data, top_window):
        top_window.menuMainViewSpectrum.Enable(True)
        top_window.menuMainViewSpectrumFit.Enable(True)
        top_window.menuMainFileSave.Enable(True)
        top_window.set_spectrum_obj(spectrum_data)


class SettingsFrameImpl(settings_frame.SettingsFrame):

    def __init__(self, parent):
        super().__init__(parent)

    def set_settings(self, event):
        image_format_box_choices_numbers = {0: "jpg", 1: "pdf", 2: "png"}
        values = {"dpi": self.dpi_value_box.GetValue(),
                  "image_format": image_format_box_choices_numbers[self.image_format_box.GetSelection()],
                  "chartX_unit": self.chart_X_unit_text.GetValue(),
                  "chartY_unit": self.chart_Y_unit_text.GetValue()}
        # These values are read from app's window for save/set method ^

        try:
            file = open(".settings", "w")
            json.dump(values, file)  # Up here we save these values :)
            file.close()
        except IOError as e:
            print(e)
        finally:
            self.Close()

    def cancel_operation(self, event):
        self.Close()
