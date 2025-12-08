import random
names=input("enter everybody's name separated by comma:")
names_list=names.split(',')
names_list = [name.strip() for name in names_list]

print(names_list)
will_pay_bill=random.choice(names_list)
print(f"{will_pay_bill} will pay the bill.")
