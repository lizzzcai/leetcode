package leetcode

import "math"

func minDistance(word1 string, word2 string) int {
	w1 := "#" + word1
	w2 := "#" + word2

	n1 := len(w1)
	n2 := len(w2)

	dp := make([][]int, n1)
	for i := 0; i < n1; i++ {
		dp[i] = make([]int, n2)
	}

	// if s2 is emtpy, we delete s1
	for i := 0; i < n1; i++ {
		dp[i][0] = i
	}
	// if s1 is empty, we insert into s1
	for i := 0; i < n2; i++ {
		dp[0][i] = i
	}

	for i := 1; i < n1; i++ {
		for j := 1; j < n2; j++ {
			cost := 0
			if w1[i] != w2[j] {
				cost = 1
			}
			dp[i][j] = int(min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost))
		}
	}

	return dp[n1-1][n2-1]

}

func min(a ...int) int {
	result := math.MaxInt64
	for _, v := range a {
		if v < result {
			result = v
		}
	}
	return result
}
