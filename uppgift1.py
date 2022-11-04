file = open('input')
test_input = file.read()
file.close()

test_input = test_input.splitlines()

my_data = []

for num in test_input:
    my_data.append(int(num))


expected_data = 2020
result_data = []

for x in range(len(my_data)):
    for y in range(len(my_data)):
        if my_data[x] + my_data[y] == expected_data:
            result_data.append(my_data[x])
            result_data.append(my_data[y])
            break
    if len(result_data) > 0:
        break

result = result_data[0] * result_data[1]
print(result)


