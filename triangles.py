def top_left_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print("")

top_left_triangle(5)

#output
"""
*
**
***
****
*****
"""

def top_right_triangle(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print("")

top_right_triangle(5)

#output
"""
    *
   **
  ***
 ****
*****
"""

def bottom_left_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print("")

bottom_left_triangle(5)

#output
"""
*****
****
***
**
*
"""

def bottom_right_triangle(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print("")

bottom_right_triangle(5)

#output
"""
*****
 ****
  ***
   **
    *
"""
def triangle(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print("")

triangle(5)

#output
""" 
    *
   ***
  *****
 *******
*********
"""

def diamond(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print("")

    for i in range(n-1, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        print("")

diamond(5)

#output
""" 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
