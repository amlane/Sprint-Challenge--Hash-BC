#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    as you add items to the hashtable, 
    check if the item you're adding is already a key (the difference)
    key: value == difference between limit and weight: index
    if the item is there return results
    if not, insert the item
    """
    results = []
    for i in range(0, length):
        difference = limit - weights[i]
        if hash_table_retrieve(ht, weights[i]) is None:
            hash_table_insert(ht, difference, i)
        else:
            if hash_table_retrieve(ht, weights[i]) <= i:
                results.append(i)
                results.append(hash_table_retrieve(ht, weights[i]))
            else:
                results.append(hash_table_retrieve(ht, weights[i]))
                results.append(i)

    if len(results) is 0:
        return None
    else:
        return results


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 4], 2, 8))
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))