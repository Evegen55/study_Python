'''
Created on Nov 11, 2016
rewrite this 
function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}
to a Python code
'''
def getFib(position):
    if position == 0: return 0
    if position == 1: return 1
    first = 0
    second = 1
    next = first + second
    i = 2
    while i < position:      
        first = second
        second = next
        next = first + second
        i = i + 1  
    return next;

k = 0
while k < 200:
    print getFib(k)
    k = k+1