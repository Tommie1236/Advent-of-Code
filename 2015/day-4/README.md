# Writeup AoC 2015 Day-4

## Part 1
### Challenge: 
```
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

  - If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
  - If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

```

Today we have a challenge that looks difficult but is accually very simple.

Santa want's you to find the lowest number that combined with the key given, that when hashed with md5 starts with 5 zero's.

I started by getting the key from `key.txt`.
```py
with open('key.txt', 'r') as file:
    key = file.readline().strip('\n')
```

Then its just a loop that hashes the `key + i` with `i` being a integer that increments each pass. And comparing the last 5 charachers with `00000`. Breaking out of the loop when `True`.

```py
i = 1
while True:
    if i % 10000 == 0:
        print(i)
    if hashlib.md5((key+str(i)).encode()).hexdigest()[:5] == '00000':
        break
    i += 1
```

I also added some code to print each 10000th number. Don't print it each pass because printing to the theminal takes a lot of time. It is the difference between getting the answer in 2 seconds or 70 seconds (on my computer)

## Part 2
### Challenge:

```
Now find one that starts with six zeroes.
```

This is very simple. Use the code from [part-1](README.md#part-1) but change the hash slice from `[:5]` to `[:6]` and the zero's to compare with from `'00000'` to `'000000'`.  
I also suggest to change the printing interfall to something like `100000`. or removing the print entrirely.

Without prints you should get the answer in under 20a30 seconds.