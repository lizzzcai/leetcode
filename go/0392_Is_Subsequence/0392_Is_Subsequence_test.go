package leetcode

import (
	"fmt"
	"testing"
)

func TestIsSubsequence(t *testing.T) {
	var tests = []struct {
		s, t string
		want bool
	}{
		{"abc", "ahbgdc", true},
		{"axc", "ahbgdc", false},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v, %v", tt.s, tt.t)
		t.Run(testname, func(t *testing.T) {
			for _, fn := range []func(string, string) bool{isSubsequence_1, isSubsequence_2} {
				ans := fn(tt.s, tt.t)
				if ans != tt.want {
					t.Errorf("got %v, want %v", ans, tt.want)
				}
			}

		})
	}
}
