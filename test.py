#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pylab import *
from numpy import *
from minoritygame import *
fig = figure(1, figsize=(6,4))

for t in range(100):
    sim = World(T=200, N=101, m=2, s=2)
    sim.act()
    print(sim.collect_strgy_score())
