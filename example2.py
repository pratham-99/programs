words = '223334444555556622'
count = 1
answer = ''
last_char = None
for i, char in enumerate(words):
    if last_char != None:
        if char == last_char:
            count = count + 1
        else:
            answer = f'{answer}{last_char}{count}'
            count = 1
    if i == (len(words) - 1):
        answer = f'{answer}{last_char}{count}'
    last_char = char

print(answer)
