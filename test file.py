# import time
#
# start_time = time.time()
#
# i = 1
# while i <= 100000:
#     print(i)
#     i += 1
#
# end_time = time.time()
# elapsed_time = end_time - start_time
# print("Час виконання while: ", elapsed_time, "секунд")
# 0.29449462890625 секунд
# 0.2913033962249756
import time

start_time = time.time()

for i in range(1, 100000):
    print(i)

end_time = time.time()
elapsed_time = end_time - start_time
print("Час виконання for: ", elapsed_time, "секунд")
