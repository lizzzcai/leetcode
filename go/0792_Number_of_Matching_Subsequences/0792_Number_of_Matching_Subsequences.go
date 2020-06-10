package leetcode

func numMatchingSubseq(S string, words []string) int {

	m := map[rune][]string{'#': words}
	ans := 0
	for _, x := range "#" + S {
		nxt := m[x]
		delete(m, x)
		for _, s := range nxt {
			if len(s) == 0 {
				ans++
			} else {
				c := rune(s[0])
				m[c] = append(m[c], s[1:])
			}
		}
	}
	return ans
}
