import sample
from sample import Signal

sampler = sample.Sampler(100, 2)

signals = [Signal(1,3), Signal(20,1), Signal(10, 0.5)]
comb_signal = sampler.construct_signal(signals)
sampler.show(comb_signal)