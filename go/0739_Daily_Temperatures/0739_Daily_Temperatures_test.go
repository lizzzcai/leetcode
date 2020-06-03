package leetcode

import (
	"fmt"
	"testing"
)

func TestDailyTemperatures(t *testing.T) {
	var tests = []struct {
		T    []int
		want []int
	}{
		{[]int{73, 74, 75, 71, 69, 72, 76, 73}, []int{1, 1, 4, 2, 1, 1, 0, 0}},
		{[]int{89, 62, 70, 58, 47, 47, 46, 76, 100, 70}, []int{8, 1, 5, 4, 3, 2, 1, 1, 0, 0}},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v", tt.T)
		t.Run(testname, func(t *testing.T) {
			ans := dailyTemperatures(tt.T)
			if Equal(ans, tt.want) != true {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}


func Equal(a, b []int) bool {
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