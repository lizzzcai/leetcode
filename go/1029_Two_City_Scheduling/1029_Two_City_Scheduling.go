package leetcode

import "sort"

func twoCitySchedCost(costs [][]int) int {
	n := len(costs)
	sort.Slice(costs, func(i, j int) bool { return costs[i][0]-costs[i][1] < costs[j][0]-costs[j][1] })
	res := 0
	for i := 0; i < n/2; i++ {
		res += costs[i][0]
	}
	for i := n / 2; i < n; i++ {
		res += costs[i][1]
	}
	return res
}

func twoCitySchedCost_1(costs [][]int) int {
	n := len(costs)
	_sort(costs, 0, n-1, n/2)
	res := 0
	for i := 0; i < n/2; i++ {
		res += costs[i][0]
	}
	for i := n / 2; i < n; i++ {
		res += costs[i][1]
	}
	return res
}

func _sort(costs [][]int, l, r, k int) {
	if l < r {
		p := partition(costs, l, r)
		if p == k {
			return
		} else if p < k {
			_sort(costs, p+1, r, k)
		} else {
			_sort(costs, l, p-1, k)
		}
	}
}

func partition(costs [][]int, l, r int) int {
	pivot := costs[r][0] - costs[r][1]
	a := l
	for i := l; i < r; i++ {
		if costs[i][0]-costs[i][1] <= pivot {
			// swap i and a
			costs[i], costs[a] = costs[a], costs[i]
			a++
		}
	}
	costs[r], costs[a] = costs[a], costs[r]
	return a
}
