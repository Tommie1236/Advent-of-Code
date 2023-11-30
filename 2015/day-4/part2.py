import hashlib

with open('key.txt', 'r') as file:
    key = file.readline().strip('\n')
    
i = 0
while True:
    #if i % 100000 == 0:
        #print(i)
    if hashlib.md5((key+str(i)).encode()).hexdigest()[:6] == '000000':
        break
    i += 1

print(i)