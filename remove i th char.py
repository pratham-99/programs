str = "geeksofgeek"

new_str = ""
for i in range(len(str)):
    if i != 4:
        new_str += str[i]
print(new_str)
