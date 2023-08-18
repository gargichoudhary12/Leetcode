class Solution:
  def brokenCalc(self, x: int, y: int) -> int:
    count = 0
    while y>x:
        count+=1+y%2
        y+=y%2
        y//=2
    return count+(x-y)