class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

        
    def computeDifference(self):
        for i in range(len(self.__elements) - 1):
            for subtrahend in self.__elements[i:]:
                absolute_difference = abs(self.__elements[i] - subtrahend)
                if absolute_difference > self.maximumDifference:
                    self.maximumDifference = absolute_difference
                    
        return self.maximumDifference
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)