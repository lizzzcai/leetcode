package leetcode

// math
func isPowerOfTwo_1(n int) bool {
	if n <= 0 {
		return false
	}

	for n != 1 {
		if n%2 != 0 {
			return false
		} else {
			n /= 2
		}
	}

	return true
}

// bit manipulation
func isPowerOfTwo_2(n int) bool {
	if n <= 0 {
		return false
	}

	return (n & (n - 1)) == 0

}
