package leetcode

import (
	"fmt"
	"testing"
)

func TestMinDistance(t *testing.T) {
	var tests = []struct {
		word1, word2 string
		want         int
	}{
		{"horse", "ros", 3},
		{"intention", "execution", 5},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v,%v", tt.word1, tt.word2)
		t.Run(testname, func(t *testing.T) {
			ans := minDistance(tt.word1, tt.word2)
			if ans != tt.want {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
