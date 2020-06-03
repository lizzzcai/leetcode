package leetcode

import (
	"fmt"
	"testing"
)

func TestSuperEggDrop(t *testing.T) {
	var tests = []struct {
		K, N int
		want int
	}{
		{2, 6, 3},
		{1, 2, 2},
		{3, 14, 4},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v,%v", tt.K, tt.N)
		t.Run(testname, func(t *testing.T) {
			ans := superEggDrop(tt.K, tt.N)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
