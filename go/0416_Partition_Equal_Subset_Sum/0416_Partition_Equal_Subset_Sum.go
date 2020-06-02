package leetcode

func canPartition(nums []int) bool {
	/*
	   time: O(m*n)
	   space O(m)
	*/
	s := 0
	for _, x := range nums {
		s += x
	}

	if s%2 != 0 {
		return false
	}

	s = s / 2
	n := len(nums)

	dp := make([]bool, s+1)
	dp[0] = true

	for i := 1; i <= n; i++ {
		for j := s; j > 0; j-- {
			if j >= nums[i-1] {
				dp[j] = dp[j] || dp[j-nums[i-1]]
			}
		}
	}

	return dp[s]

}
