#concepts
#funtions
#oops concepts
#patterns
#left angled triangle
def left_anged_triangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print("")

left_anged_triangle(5)
