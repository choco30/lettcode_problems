#To find a power n in o(log n) time instead on o(n)
class exponent:
  def calculate(a:int, b:int):
    pow=int(bin(b).replace("0b","")) # find the binary of a number
    no=a
    res=1
    while pow>0:
      if(pow&1): #to check if the bit at that position is set or not
        res*=a
      a=a*a
      pow>>1 # to shift the no one digit back
    return res  
