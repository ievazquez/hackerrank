def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [ 0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx  = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue  = array[largerValueIdx]
        if abs(smallerValue)  > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValue += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValue -= 1
    return sortedSquares

if __name__ == "__main__":
    print(sorted([-1,10,3,4,2]))