import scipy
import numpy as np
import config
import plotter
class Signal:
    def __init__(self, freq, amp):
        self.freq = freq
        self.amp = amp

class Sampler:
    def __init__(self, sample_rate, duration):
        self.duration = duration
        self.sample_rate = sample_rate
        self.samples = duration * sample_rate
        self.x_vals = np.arange(0,duration, 1/sample_rate)

    def construct_signal(self, signals):
        constructed_signal = 0
        for signal in signals:
            constructed_signal += signal.amp*np.sin(signal.freq * self.x_vals * 2 * np.pi)
        return constructed_signal    
    
    def get_fourier_properties(self, signal):
        half_length = self.samples // 2 #floor div
        n = np.arange(half_length)
        T = self.samples/self.sample_rate
        freqs = n/T

        dft = scipy.fftpack.fft(signal)[:half_length]/half_length #big array with Xk
        amps = np.abs(dft[:half_length])
        return amps, freqs

    def get_signals(self, amps, freqs):
        signals = []
        for a in range(len(amps)):
            if amps[a] - config.NOISE_OFFSET > 0:
                signals.append(Signal(freqs[a], amps[a]))
        for signal in signals:
            print(f"{signal.amp} {signal.freq}")
        return signals

    def get_reconstructed_signal(self, amps, freqs):
        reconstructed_signal = self.construct_signal(self.get_signals(amps, freqs))
        return reconstructed_signal

    def show(self, signal):
        graph_plotter = plotter.Plotter()
        amps, freqs = self.get_fourier_properties(signal)
        graph_plotter.plot(self.x_vals, freqs, amps, signal, self.get_reconstructed_signal(amps, freqs))