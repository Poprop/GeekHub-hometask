# Write a script which accepts a <number> from user and generates dictionary in range
# <number> where key is <number> and value is <number>*<number>
print("please enter number would you prefer i must to work with")

await_number = None
while await_number is None or isinstance(await_number, str):
    try:
        x = int(input())
        await_number = x
    except ValueError:
        print("Please print int number not str or float")


print(f"Nice your number is {await_number}, lets make some magic")
results = {}
for i in range(await_number):
    results[i] = i * i
print(results)
