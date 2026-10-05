def decorate_plot(ax, title, xlabel, ylabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

fig, axs = plt.subplots(3, 1)
axs[0].stem(freq, amp, 'b', markerfmt='o', basefmt='b')
decorate_plot(axs[0], "Spectrum of the signal", "Frequency [Hz]", "DFT Amplitude |X(freq)|")
axs[1].plot(x_vals, comb_signal)
decorate_plot(axs[1], "Original Signal", "Time [s]", "Height")
axs[2].plot(x_vals, reconstructed_signal)
decorate_plot(axs[2], "Reconstructed Signal", "Time [s]", "Height")
plt.show()