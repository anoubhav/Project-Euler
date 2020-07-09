from functools import reduce
from operator import mul
import os
import sys
from io import BytesIO, IOBase

def checkrow(mat, size, window):
    maxprod = 1
    # check row
    for r in range(size):
        row = mat[r]
        for i in range(size - window + 1):
            maxprod = max(maxprod, reduce(mul, row[i:i + window]))
    return maxprod

def checkdiagonal(mat, size, window):
    maxprod = 1
    for r in range(size - window + 1):
        for i in range(size - window + 1):
            diag = []
            for w in range(window):
                diag.append(mat[r+w][i+w])
            maxprod = max(maxprod, reduce(mul, diag))
    return maxprod

def naive(mat, size, window):
    # check rows (left - right)
    maxprod = checkrow(mat, size, window)
    # transpose the matrix and check columns (up - down)
    maxprod = max(maxprod, checkrow(list(map(list, zip(*mat))), size, window))
    # check right diagonal
    maxprod = max(maxprod, checkdiagonal(mat, size, window))
    # check left diagonal; flip the matrix horizontally
    maxprod = max(maxprod, checkdiagonal([row[::-1] for row in mat], size, window))
    return maxprod

def discpage(mat):
    c = mat
    m = 0
    product = lambda s: reduce(lambda a,b:a*b, s)
    for i in range(16):
        for j in range(16):
            m = max(m,product(c[i][j:j+4]))
            m = max(m,product([d[j] for d in c[i:i+4]]))
            m = max(m, c[i][j]*c[i+1][j+1]*c[i+2][j+2]*c[i+3][j+3])
            if j >= 3 and i <= 17:
                m = max(m, c[i][j]*c[i+1][j-1]*c[i+2][j-2]*c[i+3][j-3])
    return m

def main():
    size   = 20
    window = 4
    mat = []
    for _ in range(size):
        row = list(map(int, input().split()))
        mat.append(row)
    # my solution
    print(naive(mat, size, window))
    # discussions page
    print(discpage(mat))
        




































# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion
 
if __name__ == "__main__":
    main()

     