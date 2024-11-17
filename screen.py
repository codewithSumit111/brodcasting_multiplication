def broadcast_multiply(list1, list2):
    i = len(list1) - 1
    j = len(list2) - 1
    if len(list1) <= len(list2): #Checking if list1 is smaller than or equal to list2
        while i >= 0:
            list2[j] = list1[i] * list2[j] #Broadcast multiplication
            i -= 1
            j -= 1
        print("Broadcasting multiple of list1 & list2 is:", list2,"\n\n")
    else:
        print("\nlist1 is not smaller than or equal to list2\n")
        list1 = list(map(int, input("Enter the numbers for list1: ").strip().split()))
        list2 = list(map(int, input("Enter the numbers for list2: ").strip().split()))
        broadcast_multiply(list1, list2)

# Taking inputs
list1 = list(map(int, input("\nEnter the numbers for list1: ").strip().split()))
list2 = list(map(int, input("Enter the numbers for list2: ").strip().split()))
print("list1:",list1)
print("list2:",list2)
broadcast_multiply(list1, list2)#Call the function