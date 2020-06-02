package leetcode

import (
	"fmt"
	"testing"
)

func TestCanPartition(t *testing.T) {
	var tests = []struct {
		nums []int
		want bool
	}{
		{[]int{1, 5, 11, 5}, true},
		{[]int{1, 2, 3, 5}, false},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.nums)
		t.Run(testname, func(t *testing.T) {
			ans := canPartition(tt.nums)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
