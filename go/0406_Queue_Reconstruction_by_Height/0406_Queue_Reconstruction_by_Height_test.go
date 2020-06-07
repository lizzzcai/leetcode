package leetcode

import (
	"fmt"
	"testing"
)

func TestReconstructQueue(t *testing.T) {
	var tests = []struct {
		people [][]int
		want   [][]int
	}{
		{[][]int{[]int{7, 0}, []int{4, 4}, []int{7, 1}, []int{5, 0}, []int{6, 1}, []int{5, 2}},
			[][]int{[]int{5, 0}, []int{7, 0}, []int{5, 2}, []int{6, 1}, []int{4, 4}, []int{7, 1}}},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.people)
		t.Run(testname, func(t *testing.T) {
			ans := reconstructQueue(tt.people)
			if Equal(ans, tt.want) != true {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}

func Equal(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v[0] != b[i][0] || v[1] != b[i][1] {
			return false
		}
	}
	return true
}
