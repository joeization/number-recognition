import random


Threshold = 0.1
tr = 0.7


def sigmoid(z):
    return ((z/(abs(z)+1))+1)/2
    #return ((1/(math.exp(-z)+1))+1)/2

wl = -0.5
rl = 0.5

mid = 25

acc = 3


class Recog:

    def __init__(self):
        self.pat = [[round(random.uniform(wl, rl), acc)
                    for t in range(mid)]
                    for f in range(256)]
        self.pb = [round(random.uniform(0, 0.1), acc)
                    for t in range(mid)]
        self.opat = [[round(random.uniform(wl, rl), acc)
                    for t in range(10)]
                    for f in range(mid)]
        self.opb = [round(random.uniform(0, 0.1), acc)
                    for t in range(10)]

    def watch(self, form):
        self.tmp = [0 for i in range(mid)]
        for f in range(256):
            for t in range(mid):
                self.tmp[t] += self.pat[f][t] * form[f]
        for x in range(mid):
            self.tmp[x] = round(sigmoid(self.tmp[x]), acc)
            if abs(self.tmp[x]) < self.pb[x]:
                self.tmp[x] = 0
        self.ts = [0 for i in range(10)]
        for i in range(mid):
            for j in range(10):
                self.ts[j] += self.tmp[i] * self.opat[i][j]

        for x in range(10):
            self.ts[x] = round(sigmoid(self.ts[x]), acc)
            if abs(self.ts[x]) < self.opb[x]:
                self.ts[x] = 0

        res = 0
        cnt = self.ts[0]
        for x in range(1, 10):
            if self.ts[x] > cnt:
                cnt = self.ts[x]
                res = x
        return res

    def back(self, ac, form):
        ok = [0]*10
        ok[ac] = 1
        dk = [0]*10
        for k in range(0, 10):
            g = self.ts[k]
            dk[k] = (ok[k]-g)*(g)*(1-g)
        for f in range(0, mid):
            for t in range(0, 10):
                self.opat[f][t] += tr*dk[t]*self.tmp[f]
        dj = [0]*mid
        for t in range(0, mid):
            for tf in range(0, 10):
                dj[t] += self.opat[t][tf]*dk[tf]
        for f in range(0, 256):
            for t in range(0, mid):
                w = self.tmp[t]
                self.pat[f][t] += tr*dj[t]*w*(1-w)*form[f]
