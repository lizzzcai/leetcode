package leetcode

func reverseString(s []byte) []byte {
	i := 0
	j := len(s) - 1

	for i < j {
		s[i], s[j] = s[j], s[i]
		i++
		j--
	}
	return s
}
