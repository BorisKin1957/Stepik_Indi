line = input().strip('\n')
str_lst = line.split(' = ')[-1]
str_lst = str_lst.replace('[', '').replace(']', '').replace('"Р', 'Р').replace('", ','|').replace('"', '')

booked = str_lst.split('|')

print(booked)
