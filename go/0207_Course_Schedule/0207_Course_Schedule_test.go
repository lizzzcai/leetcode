package leetcode

import (
	"fmt"
	"testing"
)

func TestCanFinish(t *testing.T) {
	var tests = []struct {
		numCourses    int
		prerequisites [][]int
		want          bool
	}{
		{2, [][]int{[]int{1, 0}}, true},
		{2, [][]int{[]int{1, 0}, []int{0, 1}}, false},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%d,%v", tt.numCourses, tt.prerequisites)
		t.Run(testname, func(t *testing.T) {
			ans := canFinish(tt.numCourses, tt.prerequisites)
			if ans != tt.want {
				t.Errorf("got %t, want %t", ans, tt.want)
			}
		})
	}
}
