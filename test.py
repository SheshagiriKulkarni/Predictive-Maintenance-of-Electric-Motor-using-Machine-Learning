def count_binary_strings_with_exactly_one_consecutive_1s(n):
    if n < 2:
        return 0

    # Initialize DP arrays
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp = [0] * (n + 1)
    
    # Base cases
    dp[2] = 1  # Only "11" is valid
    dp0[2] = 0
    dp1[2] = 1
    
    # Fill the DP table
    for i in range(3, n + 1):
        dp1[i] = dp0[i-1]
        dp0[i] = dp[i-1] + dp0[i-1]
        dp[i] = dp0[i] + dp1[i]
    
    return dp[n]

# Example usage:
n = 5
print(f"Number of distinct binary strings of length {n} with exactly one pair of consecutive 1s: {count_binary_strings_with_exactly_one_consecutive_1s(n)}")
