import heapq
from collections import defaultdict

# Huffman Coding


def huffman_coding(chars, weight):

    # Create a min heap of tuples (weight, char)
    heap = [(weight[i], chars[i]) for i in range(len(chars))]
    heapq.heapify(heap)

    # Create a dictionary to store the Huffman codes
    codes = defaultdict(str)

    # While the heap has more than one element
    while len(heap) > 1:
        # Extract the two smallest elements from the heap
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new node with the sum of their weights and a None value
        parent = (left[0] + right[0], left[1] + right[1])

        # Add the new node to the heap
        heapq.heappush(heap, parent)

        for ch in list(left[1]):
            codes[ch] = "0" + codes[ch]
        for ch in list(right[1]):
            codes[ch] = "1" + codes[ch]

    # Return the Huffman codes
    return codes


if __name__ == "__main__":
    chars = "abcdef"
    weight = [5, 11, 7, 13, 3, 17]
    codes = huffman_coding(chars, weight)
    print(codes)

    chars = "acef"
    weight = [5, 7, 3, 17]
    codes = huffman_coding(chars, weight)
    print(codes)
