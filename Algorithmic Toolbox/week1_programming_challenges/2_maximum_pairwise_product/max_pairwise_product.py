# python3


def max_pairwise_product(numbers:list):
    max_num = 0
    second_max_num = 0
    # We just loop through the array once finding the two maximum numbers and return their product
    # This is now O(n)
    for num in numbers:
        if (num >= max_num):
            second_max_num = max_num
            max_num = num
        elif (num >= second_max_num):
            second_max_num = num
    
    max_product = max_num * second_max_num
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
