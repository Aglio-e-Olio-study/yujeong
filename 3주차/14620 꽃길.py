import sys 
input = sys.stdin.realine 

N = int(input())
graph = [list(map(int, input.split())) for _ in range(N)]
vist = [[false] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 꽃에 매겨질 수 있는 코스트 값이 1000, 3개면 3000
global ans 
ans = 3000 

def dfs(limit, total): 
    # 꽃을 3개 심은 경우 cost를 비교해서 더 작은 값이면 ans에 삽입 
    if limit == 3: 
        global ans 
        ans = min(ans, total)
        return

    for i in range(1, N-1): 
        for j in range(1, N-1): 
            key = false # 꽃을 심을 수 있는가 없는가 판별 변수
            money = 0 
            if not visit[i][j]: 
                money += graph[i][j]
                for k in range(4): 
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if visit [xx][yy] or xx < 0 or yy < 0 or y >= N: 
                        break 
                    if k == 3: 
                        key = True 
                        money += graph[xx][yy]
                    # 다 심을 수 있는 경우 
                    if key: 
                        // 다섯칸 모두 visit 처리 
                        visit[i][j] = True 
                        for k in range(4): 
                            xx = i + dx[k] 
                            yy = j + dy[k]
                            visit[xx][yy] = True
                        dfs(limit+1, total+money)

                        # dfs에서 나왔을 때 visit 값을 false로 만들어줌
                        for k in range(4): 
                            xx = i + dx[k]
                            yy = j + dy[k]
                            visit[xx][yy] = false
                        visit[i][j] = False
        dfs(0,0)
        print(ans)