key = list(input())
unfiltered = list(input())

encode = []
for i in key:
    encode.append(ord(i)-65)

sentence = []
for i in unfiltered:
    if i.isalpha():
        sentence.append(i)

output = []
count = 0
for i in sentence:
    if count < len(key):
        value = ord(i) + encode[count]
        while value > 25+65:
            value -= 26
        x = chr(value)
        output.append(x)
        count += 1
    else:
        count = 0
        value = ord(i) + encode[count]
        while value > 25+65:
            value -= 26
        x = chr(value)
        output.append(x)
        count += 1

print(''.join(output))

    



    
