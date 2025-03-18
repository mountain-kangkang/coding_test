from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = [-1] * len(words)

    while queue:
        word, cnt = queue.popleft()

        for i, w in enumerate(words):
            if visited[i] != -1:
                continue
            else:
                for ii in range(len(word)):
                    if word[:ii] == w[:ii] and word[ii + 1:] == w[ii + 1:]:
                        visited[i] = cnt + 1
                        queue.append((w, visited[i]))
                        if w == target:
                            return visited[i]

    return 0