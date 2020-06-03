package leetcode

func superEggDrop(K int, N int) int {
	// init dp
	dp := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		dp[i] = make([]int, K+1)
	}

	for m := 1; m <= N; m++ {
		for n := 1; n <= K; n++ {
			dp[m][n] = dp[m-1][n] + dp[m-1][n-1] + 1
			if dp[m][n] >= N {
				return m
			}
		}
	}

	return dp[N][K]
}
