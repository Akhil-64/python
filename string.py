a=10
b=5.6
c='abc'
print('{}{}'.format('abc','abc'))
print('%d %f %s' %(a,b,c))
print('a is {} and b is {}'.format(5,6))
print('{0} {2} {3} {1}'.format('one','two','three','four'))
print("%-10s" %('test',))#old format
print("{:>10}".format('test'))#right
print("{:^10}".format('test'))#center
print("{:<10}".format('test'))#left
print("{:*>10}".format("test"))
print("%.5s" %('test12345'))#trunc
print("{:.5}".format("xylophone"))
a="{:.5}".format("akhilkumar")
print(a)
print("{:>10.5}".format("akhilkumar"))#both alignment and padding
print("%-10.5s"  %("akhilkumar"))#both
print("{:f}".format(3.123456789))
print("{:06.2f}".format(3.14234))
print("{:+d}".format(25))
print("%d" %((-25)))
print("{:d}".format((-25)))
print("bin:{0:b},oct{0:o},hex{0:x}".format(12))
