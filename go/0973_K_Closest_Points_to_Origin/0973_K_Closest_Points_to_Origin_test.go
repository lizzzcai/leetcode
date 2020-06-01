package leetcode

import (
	"fmt"
	"strconv"
	"strings"
	"testing"
)

func check(x [][]int, y [][]int) bool {
	if len(x) == 0 && len(y) == 0 {
		return true
	}

	xMap := make(map[string]int)
	yMap := make(map[string]int)

	for _, xElem := range x {
		valuesText := []string{}
		for i := range xElem {
			number := xElem[i]
			text := strconv.Itoa(number)
			valuesText = append(valuesText, text)
		}
		result := strings.Join(valuesText, "+")
		xMap[result]++
	}
	for _, yElem := range y {
		valuesText := []string{}
		for i := range yElem {
			number := yElem[i]
			text := strconv.Itoa(number)
			valuesText = append(valuesText, text)
		}
		result := strings.Join(valuesText, "+")
		yMap[result]++
	}

	for xMapKey, xMapVal := range xMap {
		if yMap[xMapKey] != xMapVal {
			return false
		}
	}
	return true
}

func TestKClosest(t *testing.T) {
	var tests = []struct {
		points [][]int
		K      int
		want   [][]int
	}{
		{[][]int{[]int{1, 3}, []int{-2, 2}}, 1, [][]int{[]int{-2, 2}}},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v,%v", tt.points, tt.K)
		t.Run(testname, func(t *testing.T) {
			ans := kClosest(tt.points, tt.K)
			if check(ans, tt.want) == false {
				t.Errorf("got %v, want %v", ans, tt.want)
			}
		})
	}
}
