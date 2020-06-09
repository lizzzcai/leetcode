package leetcode

import (
	"fmt"
	"testing"
)

func TestIsPowerOfTwo(t *testing.T) {

	var tests = []struct {
		n    int
		want bool
	}{
		{1, true},
		{218, false},
		{16, true},
		{0, false},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.n)
		t.Run(testname, func(t *testing.T) {
			for _, fn := range []func(int) bool{isPowerOfTwo_1, isPowerOfTwo_2} {
				ans := fn(tt.n)
				if ans != tt.want {
					t.Errorf("got %v, want %v", ans, tt.want)
				}
			}

		})
	}
}
