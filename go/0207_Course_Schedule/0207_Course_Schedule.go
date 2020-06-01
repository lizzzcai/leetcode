package leetcode

func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]int, numCourses)
	degree := make([]int, numCourses)

	for _, prerequisite := range prerequisites {
		graph[prerequisite[1]] = append(graph[prerequisite[1]], prerequisite[0])
		degree[prerequisite[0]] += 1
	}

	bfs := make([]int, 0)
	for course, d := range degree {
		if d == 0 {
			bfs = append(bfs, course)
		}
	}

	for i := 0; i < len(bfs); i++ {
		course := bfs[i]
		for _, j := range graph[course] {
			degree[j] -= 1
			if degree[j] == 0 {
				bfs = append(bfs, j)
			}
		}
	}

	return len(bfs) == numCourses
}
