import numpy as np

num_list = np.random.randint(0, 50, 500)

duplication = [0 for i in range(50)]

for e in num_list:
    duplication[e] += 1

for i in range(3):
    max_value = max(duplication)
    max_value_index = duplication.index(max(duplication))
    max_value_count = duplication.count(max_value)
    print("원소값: ", max_value_index, " 중복 횟수: ", duplication[max_value_index])
    duplication[max_value_index] = 0



# 0~50 사이의 임의의 원소(정수형, 중복가능)를 500개 만들어서 가장 중복이 많이 나온 원소 3개를 원소값과 중복 횟수로 출력하시오.

#
# print(num_list)
# print(duplication)
#
# for i in range(len(duplication)):
#     print(i, ":", duplication[i])
# print(max_value)
# print(max_value_index)
# print(max_value_count)
# print(duplication)