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
				// pattern must count as empty
				dp[i][j] = p[j-1] == '*' && dp[i][j-2]
			} else if j == 0 {
				dp[i][j] = false
			} else if s[i-1] == p[j-1] || p[j-1] == '.' {
				// char match or '.' in pattern
				dp[i][j] = dp[i-1][j-1]
			} else if p[j-1] == '*' {
				if s[i-1] == p[j-2] || p[j-2] == '.' {
					// if char in string matchs the char before * in pattern, or char before * is .
					// there are multi-case, it can be empty, single, or multi for the matched char
					dp[i][j] = dp[i][j-2] || dp[i][j-1] || dp[i-1][j]
				} else {
					// if not matched, then can only be empty
					dp[i][j] = dp[i][j-2]
				}
			}
		}
	}

	return dp[len(s)][len(p)]
}
