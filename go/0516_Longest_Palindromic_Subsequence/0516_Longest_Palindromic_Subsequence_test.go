package leetcode

import (
	"fmt"
	"testing"
)

func TestLongestPalindromeSubseq(t *testing.T) {
	var tests = []struct {
		s    string
		want int
	}{
		{"bbbab", 4},
		{"cbbd", 2},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.s)
		t.Run(testname, func(t *testing.T) {
			ans := longestPalindromeSubseq(tt.s)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
