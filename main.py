class FactorsSort:
    def factors(self, array):
        factors = []
        for i in array:
            count = 0
            j = 1
            while(j*j <= i):
                if i % j == 0:
                    count += 1
                    if i // j != j:
                        count += 1
                j += 1
            factors.append(count)

        x = zip(factors, array)

        x = (sorted(list(x)))
        q = []
        for i in x:
            q.append(i[1])

        return q


array = list(map(int, input().split()))
object = FactorsSort()
print(object.factors(array))


"""Factors Sort
You are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.

Note: You cannot use any extra space
Example Input

Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Example Output

Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]"""