import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm

r = []

def compare(a, n):
    for i, j in enumerate(a):
        if n < j:
            if i != 0:
                return i - 1
            else:
                return i

meow = numpy.arange(-0.2, 0.2, 0.001)
for i in tqdm(meow):
    if 0.01 > i:
        r.append(sum(55.81160550 * 0.107**2 / (0.107**2 + i**2)**3 * numpy.arange(0, 0.2, 0.001)))
    else:
        ind = compare(meow, i)
        arr = [meow[:ind], meow[ind:]]
        a = nyan = numpy.arange(-(len(arr[0])), 0, 0.001).tolist()
        nyan2 = numpy.arange(0.01, len(arr[1]), 0.001).tolist()
        a.extend(nyan2)
        r.append(sum(55.81160550 * 0.107**2 / (0.107**2 + i**2)**3 * numpy.array(a)))

plt.plot(numpy.arange(-0.2, 0.2, 0.001), r)

plt.show()

print(numpy.array(meow)[numpy.where(numpy.array(r) == numpy.max(numpy.array(r)))])

print(sum(r[:numpy.where(numpy.array(r) == numpy.max(numpy.array(r)))[0][0]]))