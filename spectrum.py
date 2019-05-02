import time
import pickle


class Spectrum:
    __spectrum = []
    __old = []
    __data = ""

    def set_spectrum(self, spectrum):
        self.__spectrum = spectrum

    def set_spectrum_data(self, data):
        self.__data = data

    def get_spectrum_data(self):
        return self.__data

    def get_spectrum(self):
        return self.__spectrum

    def get_spectrum_x(self):
        return [x[0] for x in self.__spectrum]

    def get_spectrum_y(self):
        return [y[1] for y in self.__spectrum]

    def clear_data(self):
        self.__data = ""

    def save(self):
        try:
            t = str(time.asctime(time.localtime(time.time()))).replace(":", "-")
            file_name = t + ".anb"
            with open(file_name, "wb") as file:
                pickle.dump(self, file)
        except IOError as e:
            print(e)
