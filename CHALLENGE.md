## Challenge 1

Commander Lambda has tasked you with writing a program to generate an identifier for new and existing minions. Luckily, Lambda has come up with a foolproof system. Given a sequence of prime numbers 2357111317… Each minion picks a number out of a hat, the number will represent the starting index in the sequence of primes and their ID will be the next 5 digits in the sequence. For example, if an employee draws 3 their ID will be 71113. Write a solution that takes a number n, where 0 <= n <= 10000, and returns a number of length 5 representing their ID.

Test Cases
Input: 0
Output: 23571

Input: 3
Output: 71113

## Challenge 2

When you went undercover in Commander Lambda's organisation, you set up a coded messaging system with Bunny Headquarters to allow them to send you important mission updates. Now that you're here and promoted to Henchman, you need to make sure you can receive those messages - but since you need to sneak them past Commander Lambda's spies, it won't be easy! Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers stations, and will use them to broadcast lists of numbers. They've given you a numerical key, and their messages will be encrypted within the first sequence of numbers that adds up to that key within any given list of numbers.

Given a non-empty list of positive integers l and a target positive integer t, write a function solution(l,t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the list containing the smallest start and end indexes where this sequence can  be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).

For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function solution(l, t) would return the list [0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, given the list
l as [1, 2, 3, 4] and the key t as 15, the function solution(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.
To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards:
 - Each list l will contain at least 1 element but never more than 100.
 - Each element of l will be between 1 and 100.
 - t will be a positive integer, not exceeding 250.
 - The first element of the list l has index 0.
 - For the list returned by solution(l, t), the start index must be equal or smaller than the end index.

Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist of a number broadcast that can be summed up to the key. You know that the message will always be hidden in the first sublist that sums up to the key, so solution(l, t)
should only return that sublist.

Test Cases

Input: [1, 2, 3, 4], 15
Output: -1, -1

Input: [4, 3, 10, 2, 8], 12
Output: 2, 3

