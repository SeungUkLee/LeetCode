func numJewelsInStones(J string, S string) int {
	var count int
	jewelMap := make(map[rune]int)

	for i, k := range J {
		jewelMap[k] = i
	}
	
	for _, k := range S {
		if _, exists := jewelMap[k]; exists {
			count ++
		}
	}

	return count
}