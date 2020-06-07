package leetcode

var (
	num_index_pair [][]int
	res            []int
)

func countSmaller(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}

	res = make([]int, len(nums))
	num_index_pair = make([][]int, len(nums))
	for i := 0; i < len(nums); i++ {
		num_index_pair[i] = []int{nums[i], i}
	}
	divide(num_index_pair)

	return res
}

func divide(num_index [][]int) [][]int {
	mid := len(num_index) / 2
	if len(num_index) > 1 {
		left := divide(num_index[:mid])
		right := divide(num_index[mid:])

		return conquer(left, right)
	} else {
		return num_index
	}

}

func conquer(left, right [][]int) [][]int {
	sort := make([][]int, 0)
	i := 0
	j := 0
	for i < len(left) && j < len(right) {
		if left[i][0] > right[j][0] {
			sort = append(sort, left[i])
			res[left[i][1]] += len(right) - j
			i++
		} else {
			sort = append(sort, right[j])
			j++
		}
	}

	for i < len(left) {
		sort = append(sort, left[i])
		i++
	}

	for j < len(right) {
		sort = append(sort, right[j])
		j++
	}

	return sort
}
