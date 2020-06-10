package leetcode

func minInsertions(s string) int {
	return len(s) - longestPalindromeSubseq(s)
}

func longestPalindromeSubseq(s string) int {
	n := len(s)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}

	// dp[i][j]: s[i,j+1]
	for j := 0; j < n; j++ {
		for i := j; i >= 0; i-- {
			if i == j {
				dp[i][j] = 1
			} else if s[i] == s[j] {
				dp[i][j] = dp[i+1][j-1] + 2
			} else {
				dp[i][j] = Max(dp[i+1][j], dp[i][j-1])
			}
		}
	}
	return dp[0][n-1]
}

func Max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
