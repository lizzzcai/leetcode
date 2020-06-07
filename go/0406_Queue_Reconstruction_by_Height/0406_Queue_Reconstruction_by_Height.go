package leetcode

import "sort"

func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			// ascend by k if h is equal
			return people[i][1] < people[j][1]
		} else {
			return people[i][0] > people[j][0]
		}
	})

	ans := make([][]int, 0)

	for i := 0; i < len(people); i++ {
		ans = insert(ans, people[i], people[i][1])
	}

	return ans
}

func insert(arr [][]int, item []int, index int) [][]int {
	arr = append(arr, []int{-1, -1})
	copy(arr[index+1:], arr[index:])
	arr[index] = item
	return arr
}
