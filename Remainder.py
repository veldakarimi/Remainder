# Write your remainder function here:
def remainder(num1, num2):
  num = (num1*num1) % (num2*(1/2))
  return num
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0