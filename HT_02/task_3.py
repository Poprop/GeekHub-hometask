# Write a script which accepts a <number> from user and print
# out a sum of the first <number> positive integers.

inp_num=int(input("Please enter your number"))
res=0
for el in range(inp_num+1):
    res+=el
print(res)