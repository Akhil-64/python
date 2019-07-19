quantity=int(input())
value=int(input())
tax=0.10*(quantity+value)
tax1=tax+quantity+value
dis=0.40*(tax1)
bill=tax1-dis
print("total bill amount:",bill)
