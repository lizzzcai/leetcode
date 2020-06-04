package leetcode

import (
	"fmt"
	"testing"
)

func TestReverseString(t *testing.T) {

	var tests = []struct {
		s    []byte
		want []byte
	}{
		{[]byte{'h', 'e', 'l', 'l', 'o'}, []byte{'o', 'l', 'l', 'e', 'h'}},
		{[]byte{'H', 'a', 'n', 'n', 'a', 'h'}, []byte{'h', 'a', 'n', 'n', 'a', 'H'}},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.s)
		t.Run(testname, func(t *testing.T) {
			for _, fn := range []func([]byte) []byte{reverseString} {
				ans := fn(tt.s)
				if Equal(ans, tt.want) != true {
					t.Errorf("got %v, want %v", ans, tt.want)
				}
			}

		})
	}
}

func Equal(a, b []byte) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}
