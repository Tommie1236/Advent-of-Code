import hashlib

with open('key.txt', 'r') as file:
    key = file.readline().strip('\n')
    
i = 1
while True:
    if i % 10000 == 0:
        print(i)
    if hashlib.md5((key+str(i)).encode()).hexdigest()[:5] == '00000':
        break
    i += 1

print(i)