def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    items = {}

    for i, weight in enumerate(weights):
        weight_index = limit - weights[i]

        if weight_index not in items:
            items[weight] = i
        else:
            return (i, items[weight_index])
    return None
