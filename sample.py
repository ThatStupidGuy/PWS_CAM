import scipy
import numpy as np
import matplotlib.pyplot as plt
import config

class Signal:
    def __init__(self, freq, amp):
        self.freq = freq
        self.amp = amp
    
def construct_signal(signals, x_vals):
    constructed_signal = 0
    for signal in signals:
        constructed_signal += signal.amp*np.sin(signal.freq * x_vals * 2 * np.pi)
    return constructed_signal


signals = [Signal(1,3), Signal(20,1), Signal(10, 0.5)]


comb_signal = construct_signal(signals, x_vals)

class Sampler:
    def __init__(self, sample_rate, duration, signal):
        self.duration = duration
        self.sample_rate = sample_rate
        self.samples = duration * sample_rate
        self.signal = signal
        self.x_vals = np.arange(0,duration, 1/sample_rate)
        
    
    def get_fourier_properties():
        half_length = self.samples // 2 #floor div
        n = np.arange(half_length)
        T = self.samples/self.sample_rate
        freq = n/T

        dft = scipy.fftpack.fft(signal)[:half_length]/half_length #big array with Xk
        amp = np.abs(dft[:half_length])
        return amp, freq

    def get_signals(amps, freqs):
        signals = []
        for a in range(len(amps)):
            if amps[a] - config.NOISE_OFFSET > 0:
                signals.append(Signal(freqs[a], amps[a]))
        for signal in signals:
            print(f"{signal.amp} {signal.freq}")
        return signals

    def get_reconstructed_signal():
        amp, freq = self.get_fourier_properties()
        reconstructed_signal = construct_signal(self.get_signals(amp, freq), x_vals)
        return reconstructed_signal