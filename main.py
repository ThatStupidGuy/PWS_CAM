import sample
from sample import Signal

sampler = sample.Sampler(100, 2)

signals = [Signal(1,3, 1), Signal(20,1, 0.5), Signal(10, 0.5, 0)]
comb_signal = sampler.construct_sin_signal(signals)
sampler.show(comb_signal)