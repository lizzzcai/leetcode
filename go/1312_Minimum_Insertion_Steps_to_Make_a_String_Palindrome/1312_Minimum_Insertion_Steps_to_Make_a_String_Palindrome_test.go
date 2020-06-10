package leetcode

import (
	"fmt"
	"testing"
)

func TestMinInsertions(t *testing.T) {
	var tests = []struct {
		s    string
		want int
	}{
		{"zzazz", 0},
		{"mbadm", 2},
		{"leetcode", 5},
		{"g", 0},
		{"no", 1},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.s)
		t.Run(testname, func(t *testing.T) {
			ans := minInsertions(tt.s)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
