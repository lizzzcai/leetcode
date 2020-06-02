package leetcode

import (
	"fmt"
	"testing"
)

func TestKthSmallest(t *testing.T) {

	node1 := &TreeNode{3, nil, nil}
	node1.Left = &TreeNode{1, nil, nil}
	node1.Right = &TreeNode{4, nil, nil}

	node1.Left.Right = &TreeNode{2, nil, nil}

	node2 := &TreeNode{5, nil, nil}
	node2.Left = &TreeNode{3, nil, nil}
	node2.Right = &TreeNode{6, nil, nil}
	node2.Left.Left = &TreeNode{2, nil, nil}
	node2.Left.Right = &TreeNode{4, nil, nil}
	node2.Left.Left.Left = &TreeNode{1, nil, nil}

	node2.Left.Right = &TreeNode{2, nil, nil}

	var tests = []struct {
		root *TreeNode
		k    int
		want int
	}{
		{node1, 1, 1},
		{node2, 3, 3},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%v,%v", tt.root, tt.k)
		t.Run(testname, func(t *testing.T) {
			for _, fn := range []func(*TreeNode, int) int{kthSmallest, kthSmallest_2, kthSmallest_3} {
				ans := fn(tt.root, tt.k)
				if ans != tt.want {
					t.Errorf("got %v, want %v", ans, tt.want)
				}
			}

		})
	}
}
