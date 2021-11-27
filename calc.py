import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm

r = []

def compare(a, n):
    for i, j in enumerate(a):
        if n < j:
            return i
    return -1

def dokujinokeisannsiki(i, arr):
    return sum(55.81160550 * 0.107**2 / (0.107**2 + (i + arr)**2) **3)

meow = numpy.arange(0, 0.2, 0.001)
for i in tqdm(numpy.arange(-0.2, 0.2, 0.001)):
    if 0 > i:
        r.append(dokujinokeisannsiki(i, meow))
    else:
        ind = compare(meow, i)
        arr = [len(meow[:ind]), len(meow[ind:])]
        nyan = -1*(dokujinokeisannsiki(0, numpy.arange(0, arr[0]*0.001, 0.001)))
        nyan2 = (dokujinokeisannsiki(0, numpy.arange(0, arr[1]*0.001, 0.001)))
        r.append(nyan + nyan2)

plt.plot(numpy.arange(-0.2, 0.2, 0.001), r)
plt.xlabel('position')
plt.ylabel('force')
plt.show()

print(numpy.arange(-0.2, 0.2, 0.001)[numpy.where(numpy.array(r) == numpy.max(numpy.array(r)))])
print(numpy.max(numpy.array(r)))

print(sum(r[:numpy.where(numpy.array(r) == numpy.max(numpy.array(r)))[0][0]]))