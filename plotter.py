import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def decorate_plot(self, ax, title, xlabel, ylabel):
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    def plot(self, x_vals, freqs, amps, original_signal, reconstructed_signal):
        fig, axs = plt.subplots(3, 1)
        axs[0].stem(freqs, amps, 'b', markerfmt='o', basefmt='b')
        self.decorate_plot(axs[0], "Spectrum of the signal", "Frequency [Hz]", "DFT Amplitude |X(freq)|")
        axs[1].plot(x_vals, original_signal)
        self.decorate_plot(axs[1], "Original Signal", "Time [s]", "Height")
        axs[2].plot(x_vals, reconstructed_signal)
        self.decorate_plot(axs[2], "Reconstructed Signal", "Time [s]", "Height")
        plt.show()