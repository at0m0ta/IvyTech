 1  import math
 2  
 3  x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))
 4   
 5  a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) 
 6  b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
 7  c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
 8  
 9  A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c))) 
10  B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
11  C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
12  
13  print("The three angles are ", round(A * 100) / 100.0,  
14      round(B * 100) / 100.0, round(C * 100) / 100.0)
