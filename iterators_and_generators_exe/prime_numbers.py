def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_primes(nums):
    for el in nums:
        if is_prime(el):
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))