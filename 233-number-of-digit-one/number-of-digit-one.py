class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        
        count = 0
        factor = 1
        
        while factor <= n:
            # Divide n into three parts: high, current digit, and low
            # Example for n=1234, factor=100: high=12, curr=3, low=34
            high = n // (factor * 10)
            curr = (n // factor) % 10
            low = n % factor
            
            if curr == 0:
                # Digit '1' only appears based on high numbers
                count += high * factor
            elif curr == 1:
                # Digit '1' appears based on high numbers + the remainder in low
                count += high * factor + low + 1
            else:
                # Digit '1' appears (high + 1) times for this factor
                count += (high + 1) * factor
            
            # Move to the next power of 10
            factor *= 10
            
        return count
