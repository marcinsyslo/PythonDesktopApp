import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import io
import json


def func(x, a, b, e):
    return (x ** a + b) * ((e - x) ** 2)


def get_fig(dpi, image_format, spectrum, fit=False):
    x_label = settings_reader("chartX_unit", "Energy [keV]")
    y_label = settings_reader("chartY_unit", "Counting [N]")
    # format_value = self.settings_reader(parameter_name="image_format", default_value=image_format)
    fig, ax = plt.subplots()

    x_data = spectrum.get_spectrum_x()
    y_data = spectrum.get_spectrum_y()

    if fit:
        popt, pcov = curve_fit(func, x_data, y_data, bounds=((0, -3, 200), (1, 10, 1200)))

        spectrum.set_spectrum_data(popt)

        table = []
        for n in x_data:
            table.append(func(n, *popt))

        ax.plot(x_data, table, "r-", label="Fit")

    ax.plot(x_data, y_data, "b-", label="Spectrum")
    ax.legend()
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.grid()
    plt.Figure.dpi = dpi

    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return buf


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
