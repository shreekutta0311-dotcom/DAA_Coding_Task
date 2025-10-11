#Perform KMP algorithm and Naive String search, display the number of 'Comparison operations involved', time taken by both algo
import time
import sys
text = "CATSABCBCABCDOGGSABBCBCABC"
pattern = "ABCBCABC"
# for naive string search
naivecomparisons = 0
start_naive = time.time()
for i in range(len(text) - len(pattern) + 1):
    for j in range(len(pattern)):
        naivecomparisons += 1
        if text[i + j] != pattern[j]:
            break
endnaive = time.time()
#kmp
m=len(pattern)
lps = [0] * m
length = 0
i = 1
while i < m:
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
i = j = 0
n=len(text)
kmpcomparisons=0
start_kmp = time.time()
while i < n:
    if pattern[j] == text[i]:
        i += 1
        j += 1
    if j == m:
        print("Pattern found at index", i - j)
        j = lps[j - 1]
    elif i < n and pattern[j] != text[i]:
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1
end_kmp = time.time()
print("\nEmpirical Analysis ")
print("Naive Search:")
print("Time:", round(endnaive - start_naive, 4), "seconds")
print("Comparisons:", naivecomparisons)
print("\nKMP Search:")
print("Time:", round(end_kmp - start_kmp, 4), "seconds")
print("Comparisons:", kmpcomparisons)



