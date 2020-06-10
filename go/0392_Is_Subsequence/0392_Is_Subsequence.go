package leetcode

func isSubsequence_1(s string, t string) bool {
	i, j := 0, 0
	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
			j++
		} else {
			j++
		}
	}

	return i == len(s)
}

func isSubsequence_2(s string, t string) bool {
	indices := make(map[rune][]int)
	for i, ch := range t {
		val, ok := indices[ch]
		if !ok {
			val = make([]int, 0)
			indices[ch] = val
		}
		indices[ch] = append(indices[ch], i)
	}

	prev := 0 // [prev, len(t))
	for _, ch := range s {
		val, ok := indices[ch]
		if !ok {
			return false
		}
		l, r := 0, len(val)-1
		for l <= r {
			mid := (l + r) / 2
			// >= target
			if val[mid] >= prev {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
		if l == len(val) {
			return false
		}
		prev = val[l] + 1
	}

	return true
}
