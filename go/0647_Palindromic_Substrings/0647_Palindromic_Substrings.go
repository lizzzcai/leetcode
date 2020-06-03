package leetcode

func countSubstrings(s string) int {
	res := 0
	for i := 0; i < len(s); i++ {
		res += expand(s, i, i)
		if i < len(s)-1 && s[i] == s[i+1] {
			res += expand(s, i, i+1)
		}
	}
	return res
}

func expand(s string, i, j int) int {
	count := 0
	for i >= 0 && j < len(s) {
		if s[i] == s[j] {
			i--
			j++
			count += 1
		} else {
			break
		}
	}
	return count
}
