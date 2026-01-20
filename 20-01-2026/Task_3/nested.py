# 3.4 Nested Loop Break: Create a nested loop where the outer loop iterates from 1 to 5, and the inner loop iterates from 1 to 5. If the product of the outer and inner loop variables is greater than 12, break out of the inner loop. Print the values of the outer and inner loop variables for each iteration.

for i in range(1,6):
    for j in range(1,6):
        if((i*j)>12):
            break
        else:
            print(i,j)
            