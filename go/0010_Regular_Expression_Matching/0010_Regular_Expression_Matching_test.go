package leetcode

import (
	"fmt"
	"testing"
)

func TestIsMatch(t *testing.T) {
	var tests = []struct {
		s, p string
		want bool
	}{
		{"aa", "a", false},
		{"aa", "a*", true},
		{"ab", ".*", true},
		{"aab", "c*a*b", true},
		{"mississippi", "mis*is*p*.", false},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v,%v", tt.s, tt.p)
		t.Run(testname, func(t *testing.T) {
			ans := isMatch(tt.s, tt.p)
			if ans != tt.want {
				t.Errorf("got %t, want %t", ans, tt.want)
			}
		})
	}
}
