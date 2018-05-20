#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pylab import *
from numpy import *
from minoritygame import *

#N = [5,11,21,41,81,151,301]
N = [10,20,40,80,150,300] # n - how many agent?
s,m = 2,2
K = 400 # repeat K times/runs
T = (2**m)*1000 # run T iterations (each run)


def process_a_winned_file(fname, m=m):
    x = map(lambda x: int(sign(sign(x)+1)), loadtxt(fname))
    y = ''.join(str(i) for i in x)
    #
    t=[]
    for i in rlen(y):
        if i>=len(y)-m: break
        t.append(int(y[i:i+m+1], 2))
    #
    hd=histogram(t, 2**(m+1), density=True)[0]
    hds=sort(hd)
    return np.polyfit(rlen(hds), hds, 1)[0], t


def process_an_agentSeries(nnn, K=K):
    """TODO: Docstring for process_an_agentSeries.
    """
    xx=[]
    for i in range(K):
        if i%100==0: print(i)
        fname = './data/winned_%d_4000_%d_2_2.txt'%(i, nnn)
        x=process_a_winned_file(fname)
        xx.append(x[0])
    return xx

xxx = [process_an_agentSeries(i) for i in N]
subplot(2,1,1); plot(xxx[0], 'x-')
subplot(2,1,2); plot(xxx[-1],'.-')
# add {x,y}lim, label,...
savefig('check_winned.eps')
show()

ttt = [mean(sort(x)[-10:]) for x in xxx]
plot(ttt, '.-')
# add {x,y}lim, label,...
show()
