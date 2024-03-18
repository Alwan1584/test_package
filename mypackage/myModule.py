def top_n (items, n):
    """Return top n items in a list or array

    Args:
        items(array): list or array of items
        n (int): number of items to return
    Return: 
          Array of top n items, descending order
    
    Egs:
       >>>top_n([8,4,3,2], 3)
       [8,4,3]
    """
    for i in range(n): #keep sorting until we have top n items
        for j in range(len(items)-1-i): 

            if items[j] > items[j+1]: #if this item is bigger than the next
                items[j], items[j+1] = items[j+1], items[j] #swap the two

    #get the last two items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]




    