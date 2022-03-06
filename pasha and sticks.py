#to divide a particular stick in a way that it does not form square and only rectangle

class sticks:
  def calculate(n):
    if n%2!=0:
      return -1 #As if the sticks length is odd forming a rectangle is impossible
    div1=n/2 # dividing the stick into equal parts and then perform cut in sidentical fashion on both side so just need to cALCULATE FOR ONE SIDE
    div2=div1-1 #as there will be one case when both sides are equal and it will form a square
    div2=div/2 # as we will get repetative cases 
   
    
    return div2
  
    
