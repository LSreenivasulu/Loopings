***
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number".
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number

***
n = int(input().strip())
n_str = str(n)
if len(n_str) == 3:
     middle_digit = int(n_str[1])
    if middle_digit % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Not a Trendy Number")
