package leetcode

import (
	"fmt"
	"testing"
)

func TestMaxEnvelopes(t *testing.T) {
	var tests = []struct {
		envelopes [][]int
		want      int
	}{
		{[][]int{[]int{5, 4}, []int{6, 4}, []int{6, 7}, []int{2, 3}}, 3},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.envelopes)
		t.Run(testname, func(t *testing.T) {
			ans := maxEnvelopes(tt.envelopes)
			if ans != tt.want {
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
