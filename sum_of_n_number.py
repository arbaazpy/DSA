import time


def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end-start



def sumOfN3(n): # Better than above
    """
    This shows a different means of solving the summation problem.
    This function,  sumOfN3, takes advantage of a closed equation
    to compute the sum of the first n integers without iterating.
    """
    start = time.time()
    result = (n*(n+1))//2
    end = time.time()
    return result, end-start


for i in range(1000, 10001, 1000):
    print(f"sum of {i} = {sumOfN3(i)[0]} took {float(sumOfN3(i)[1])} seconds.")

print("==========================================")

for i in range(1000, 10001, 1000):
    print(f"sum of {i} = {sumOfN(i)[0]} took {float(sumOfN(i)[1])} seconds.")