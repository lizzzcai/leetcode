package leetcode

import (
	"fmt"
	"testing"
)

func TestTwoCitySchedCost(t *testing.T) {

	var tests = []struct {
		costs [][]int
		want  int
	}{
		{[][]int{[]int{10, 20}, []int{30, 200}, []int{400, 50}, []int{30, 20}}, 110},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.costs)
		t.Run(testname, func(t *testing.T) {
			for _, fn := range []func([][]int) int{twoCitySchedCost, twoCitySchedCost_1} {
				ans := fn(tt.costs)
				if ans != tt.want {
					t.Errorf("got %v, want %v", ans, tt.want)
				}
			}

		})
	}
}
