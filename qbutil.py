from math import gcd
from functools import reduce

class question:
    def __init__(self, q, a):
        self.q = q
        self.a = a
        self.clean()
        
    def __str__(self):
        return 'q: ' + self.q + '\na: ' + self.a    
    
    def clean(self):
        if '&'in self.q:
            self.q = self.q[:self.q.index('&')]
        if '&'in self.a:
            self.a = self.a[:self.a.index('&')]
        self.q = ''.join([i if ord(i) < 128 else ' ' for i in self.q])
        self.a = ''.join([i if ord(i) < 128 else ' ' for i in self.a])

def interleave(lists):
    n = reduce(gcd, [len(l) for l in lists])
    res = []
    for iteration in range(n):
        for m_list in lists:
            num_elems = len(m_list) // n
            start = iteration * num_elems
            end = start + num_elems
            res.extend(m_list[start : end])
    return res
    
    