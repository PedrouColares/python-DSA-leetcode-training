from binarySearch import BinarySearch 
from twoSum import TwoSum

if __name__ == '__main__':
    binary = BinarySearch()
    result = binary.run([1, 2, 3], 1)

    summ = TwoSum()
    sumResult = summ.run([1, 9, 13, 24, 12], 21)
    print(sumResult)