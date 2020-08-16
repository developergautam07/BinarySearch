def Bsearch(LIST, ITEM, n): # n is the number of elements in list
    ''' Main Function for the Binary Search '''
    beg = 0 # starting element
    last = n - 1  # end element
    while (beg<=last):
        mid = (beg + last)//2
        if (ITEM == LIST[mid]):
            return mid
        elif (ITEM > LIST[mid]):
            beg = mid + 1
        else:
            last = mid - 1
    else:
        return False

#__main__        
if __name__ == "__main__": 
    
    # Taking the length of list from user
    n = int(input("Enter the Number of elements you want in list: "))
    lst = [0]* n

    # Taking the elements of list from user
    print("Please Enter The elements\n*please enter the list in sorted form*:")
    for i in range(n):
        lst[i] = int(input("Element" + str(i) + ": "))

    # Taking the item from the user to search
    item = int(input("Enter the element you want to search: "))

    # Searching The Item
    pos = Bsearch(lst, item, n)

    if pos: # If item found
        print(f"\nElement found at index: {pos}, Position: {pos+1}")
    else: # If item not found
        print(f"\n Element Not Exist in the below list!!\n{lst}")