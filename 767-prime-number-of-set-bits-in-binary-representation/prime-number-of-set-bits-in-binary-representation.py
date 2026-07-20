class Solution(object):
    def countPrimeSetBits(self, left, right):
        # Prime numbers possible for set bits (0-32)
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        count = 0

        for num in range(left, right + 1):

            # Count set bits
            bits = bin(num).count("1")

            # Check if set bits count is prime
            if bits in primes:
                count += 1

        return count