package leetcode

func isMatch(s string, p string) bool {
	dp := make([][]bool, len(s)+1)
	for i := 0; i < len(s)+1; i++ {
		dp[i] = make([]bool, len(p)+1)
	}
	for i := 0; i < len(s)+1; i++ {
		for j := 0; j < len(p)+1; j++ {
			if i == 0 && j == 0 {
				dp[i][j] = true

			} else if i == 0 {
				dp[i][j] = p[j-1] == '*' && dp[i][j-1]
			} else if j == 0 {
				dp[i][j] = false
			} else if p[j-1] == '*' {
				dp[i][j] = dp[i][j-1] || dp[i-1][j]
			} else if s[i-1] == p[j-1] || p[j-1] == '?' {
				dp[i][j] = dp[i-1][j-1]
			}
		}
	}
	return dp[len(s)][len(p)]
}
