package leetcode

func lengthOfLIS(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}

	c := make([]int, 0)
	size := 0

	for _, x := range nums {
		l, r := 0, size-1
		for l <= r {
			mid := (l + r) / 2
			if c[mid] >= x {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
		if l >= size {
			c = append(c, x)
			size = Max(size, l+1)
		} else {
			c[l] = x
		}
	}
	return size
}

// Max returns the larger of x or y.
func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
