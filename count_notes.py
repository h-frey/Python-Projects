def findMin(V):

    # All denominations of Ugandan Currency
    deno = [ 50, 100, 200, 500, 1000, 2000, 5000,
            10000, 20000, 50000]
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while(i >= 0):

        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i -= 1

    # Print result
    for i in range(len(ans)):
        print(ans[i], end=" ")


# Driver Code
if __name__ == '__main__':
    n = int(input("Enter amount: "))
    print("Following is minimal number",
          "of change for", n, ": ", end="")
    findMin(n)


    


   
   
    
   
