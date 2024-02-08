def exist():
    for i in range(len(input_string)-len(target_string) + 1):
        if target_string == input_string[i:i+len(target_string)]:
            return i
    return -1

input_string = input()
target_string = input()

print(exist())