package leetcode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// recursion
func kthSmallest(root *TreeNode, k int) int {
	// count the node at left sub tree
	lnc := countNode(root.Left)
	if lnc == k-1 {
		return root.Val
	} else if lnc > k-1 {
		return kthSmallest(root.Left, k)
	} else { // lnc < k-1
		return kthSmallest(root.Right, k-lnc-1)
	}

}

func countNode(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return countNode(node.Left) + countNode(node.Right) + 1
}

// inorder
func inorder(c chan int, root *TreeNode) {
	if root == nil {
		return
	}
	inorder(c, root.Left)
	c <- root.Val
	inorder(c, root.Right)
}

func kthSmallest_2(root *TreeNode, k int) int {
	c := make(chan int)
	go func() {
		inorder(c, root)
		close(c)
	}()
	x, ok := <-c
	for ; k > 1 && ok; x, ok = <-c {
		k -= 1
	}
	return x
}

// stack

func kthSmallest_3(root *TreeNode, k int) int {
	stack := []*TreeNode{}

	for {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}

		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		k--
		if k == 0 {
			return root.Val
		}

		root = root.Right

	}
}
