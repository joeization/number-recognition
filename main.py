import trans
import recog
import random

num = 10

train = []
for x in range(num):
    for i in range(0, 1000):
        ts = 'tmp/'+str(x)+'/'+str(i)+'.jpg'
        train.append(trans.Trans(ts, x))
        #print ts
random.shuffle(train)

print 'train data loaded.'

test = []
for x in range(num):
    for i in range(1000, 1100):
        ts = 'tmp/'+str(x)+'/'+str(i)+'.jpg'
        test.append(trans.Trans(ts, x))
        #print ts

umikaze = recog.Recog()

print 'test data loaded.'

print 'training...'

cnt = 1

for data in train:
    #print cnt
    res = umikaze.watch(data.form)
    if res != data.ans:
        umikaze.back(data.ans, data.form)
    cnt += 1

print 'done.'

print 'testing...'

ac = 0
total = 0

com = [[0 for x in xrange(10)] for y in xrange(10)]

for data in test:
    res = umikaze.watch(data.form)
    com[data.ans-1][res-1] += 1
    if res == data.ans:
        ac += 1
    else:
        pass
        #print res, data.ans
    total += 1

print 'done.'

out = open('out.txt', 'w')

for z in com:
    print z
    for n in range(10):
        if n > 0:
            out.write(' ')
        out.write(str(z[n]))
    out.write('\n')
print float(ac)/total
