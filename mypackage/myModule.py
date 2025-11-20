def top_n(items, n):
    """Return the top n items in an array in desc order.
    
    Args:
        items (array): list or array-like object
        n (int): number of top items to return in desc order
        Returns:
        array: top n items in desc order
        
        Egs:
        >>> top_n([1, 3, 2, 5, 4], 3)
        [5, 4, 3]
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]: # if this item is greater than the next item
                items[j], items[j + 1] = items[j + 1], items[j] # swap them
    
    #get last two items
    top_n = items[-n:]

    #return in desc order
    return top_n[::-1]