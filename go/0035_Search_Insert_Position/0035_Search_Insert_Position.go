package leetcode

func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)-1
	if nums[l] >= target {
		return l
	}
	if nums[r] < target {
		return r + 1
	}

	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return l
}
