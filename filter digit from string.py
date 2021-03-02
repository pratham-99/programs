t_str = "i have 2 apple and 1 banana"
k= [int(i) for i in t_str.split() if i.isdigit()]
print(k)