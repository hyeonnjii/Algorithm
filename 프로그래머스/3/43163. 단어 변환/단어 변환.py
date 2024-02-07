from collections import defaultdict, deque

def solution(begin, target, words):
    # begin 단어를 시작 노드
    # 리스트를 순환하며 `각 단어: 한개의 알파벳만 바뀌는 단어들`로  인접리스트 생성
    # 해당 인접리스트 그래프는 가중치가 없으므로 bfs를 사용하여 최단 거리 계산
    
    # 그래프 key에 target 없을 경우, target의 value list가 없는 경우 0으로 return
    
    def adjacency_list(words):
        graph = defaultdict(list)
        words.insert(0, begin)
        
        for word in words:
            for other in words:
                if sum(1 for c1, c2 in zip(word, other) if c1 != c2) == 1:
                #if (len(set(word).intersection(set(other))) == len(words[0]) - 1):
                    graph[word].append(other)
                    
        return graph
    
    def bfs_to_word(graph, begin, target):
        q = deque()
        visited = {}
        distance = 0
        
        q.append((begin, distance))
        visited[begin] = True
        
        while q:
            cur_word, cur_distance = q.popleft()
            if cur_word == target:
                break
            
            for next_word in graph[cur_word]:
                if next_word not in visited:
                    q.append((next_word, cur_distance+1))
                    visited[next_word] = True
        
        return cur_distance
    
    graph = adjacency_list(words)
    if (target not in graph) or (not graph[target]):
        return 0
    else:
        return bfs_to_word(graph, begin, target)
    
    
