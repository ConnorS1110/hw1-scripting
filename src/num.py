class NUM:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf')
        self.hi = float('-inf') # Replaced sys.maxsize

    def add(self, n):
        """
        Function:
            add
        Description:
            If n is not ?, n on the instance object is incremented by one and NUM attributes are re-calculated
        Input:
            self - current NUM instance
            n - value to add
        Output:
            None
        """
        # print("Inside Add", n)
        if n != "?": # Why Question mark
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
        # print(self.n, d, self.mu, self.m2, self.lo, self.hi)

    def mid(self):
        """
        Function:
            mid
        Description:
            returns mu (mean) of the current instance
        Input:
            self - current NUM instance
        Output:
            mu (mean)
        """
        return self.mu

    def div(self): # Removed x
        """
        Function:
            div
        Description:
            Determines if there is diversity around the center
        Input:
            self - current NUM instance
        Output:
            True or False
        """
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5
