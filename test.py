#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pylab import *
from numpy import *
from minoritygame import *
fig = figure(1, figsize=(6,4))

T,N,m = 200,19,2

def collect_strgy_score(wld, counts, scores):
    for a in wld.Agents:
        for s in a.Strgies:
            g = int(s.strgy, 2)
            counts[g].append(s.count)
            scores[g].append(s.score)
    return array(counts), array(scores)


for t in range(20):
    counts = [ [] for _ in range(2**(2**m))]
    scores = [ [] for _ in range(2**(2**m))]
    if t%100==0: print(t)
    sim = World(T=T, N=N, m=m, s=2)
    sim.act()
    collect_strgy_score(sim, counts, scores)
    for x in scores:
        print(mean(x), std(x))
    print('\n')
    #for x in counts:
        # print(mean(x), std(x))
    #print('\n')
