package leetcode

import (
	"fmt"
	"testing"
)

func TestNumMatchingSubseq(t *testing.T) {
	var tests = []struct {
		S     string
		words []string
		want  int
	}{
		{"abcde", []string{"a", "bb", "acd", "ace"}, 3},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v, %v", tt.S, tt.words)
		t.Run(testname, func(t *testing.T) {
			ans := numMatchingSubseq(tt.S, tt.words)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}

}
