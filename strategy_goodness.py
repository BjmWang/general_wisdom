#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pylab import *
from numpy import *
from minoritygame import *
# fig = figure(1, figsize=(6,4))

N,m = 19,2
T = 1000*(2**m)


def collect_strgy_score(wld, counts, scores):
    for a in wld.Agents:
        for s in a.Strgies:
            g = int(s.strgy, 2)
            counts[g].append(s.count)
            scores[g].append(s.score)
    return nan_to_num(array(counts)), nan_to_num(array(scores))


all_score_list = []
all_count_list = []
for t in range(40):
    counts = [[] for _ in range(2**(2**m))]
    scores = [[] for _ in range(2**(2**m))]
    if t%10 == 0: print(t)
    sim = World(T=T, N=N, m=m, s=2)
    sim.act()
    collect_strgy_score(sim, counts, scores)
    clist = [abs(mean(c)) for c in counts]
    all_count_list.append(max(clist))
    slist = [abs(mean(s)) for s in scores]
    all_score_list.append(max(slist))

print(all_score_list)
subplot(211); plot(sort(all_count_list), '.-')
subplot(212); semilogy(sort(all_score_list), '.-')
savefig('count_score.eps')
show()
