#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pylab import *
from numpy import *
from minoritygame import *

K = 400
N = [5,11,21,41,81,151,301]
s, m = 2, 2
T = (2**m)*1000

def collect_strgy_score(wld, m):
    counts = [[] for _ in range(2**(2**m))]
    scores = [[] for _ in range(2**(2**m))]
    for a in wld.Agents:
        for s in a.Strgies:
            g = int(s.strgy, 2)
            counts[g].append(s.count)
            scores[g].append(s.score)
    return nan_to_num(array(counts)), nan_to_num(array(scores))


for k in range(K):
    print(datetime_str(), k)
    for n in N:
        print('\t', n)
        seed(k*1000+n)
        sim = World(T, n, m, s)
        sim.act()

        counts, scores = collect_strgy_score(sim, m)
        clistM = [nan_to_num(mean(c)) for c in counts]
        clistS = [nan_to_num(std(c)) for c in counts]
        slistM = [nan_to_num(mean(s)) for s in scores]
        slistS = [nan_to_num(std(s)) for s in scores]

        savetxt('data/scoreAVG_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(slistM))
        savetxt('data/scoreSTD_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(slistS))
        savetxt('data/countAVG_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(clistM))
        savetxt('data/countSTD_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(clistS))
        savetxt('data/prices_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(sim.Prices[1:]))
        savetxt('data/ACTION_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(sim.D))
        savetxt('data/wRates_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(sim.SuccessRates))
        savetxt('data/winned_%d_%d_%d_%d_%d.txt'%(k,T,n,m,s), array(sim.W[m:]))
