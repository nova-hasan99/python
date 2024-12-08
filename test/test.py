

str = input().lstrip('0')
count = 0

for i in range(1, len(str) - 1):
    if str[i - 1] != '0' and str[i] and str[i + 1] != '0':
        count += 1

print(count)