#해설코드
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1
                DFS(xx,yy)
                board[xx][yy]=0
                
if __name__ == "__main__":
    board = [list(map(int,input().split())) for _ in range(7)]    
    cnt=0
    board[0][0]=1
    DFS(0,0)
    print(cnt)

#나의코드(25.02.19)
# def DFS(x,y):
#     global cnt
    
#     if x==6 and y==6:
#         cnt+=1
#         return 

#     else:
#         for i in range(4):
#             if  0<=x+dx[i]<=6 and 0<=y+dy[i]<=6 and ck[x+dx[i]][y+dy[i]] == 0 and board[x+dx[i]][y+dy[i]] == 0:
#                 ck[x+dx[i]][y+dy[i]]=1
#                 DFS(x+dx[i],y+dy[i])
#                 ck[x+dx[i]][y+dy[i]]=0


# if __name__ == "__main__":
#     board = [list(map(int,input().split())) for _ in range(7)]
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     cnt = 0
#     ck = [[0]*7 for _ in range(7)]
#     ck[0][0] = 1
#     DFS(0,0)
#     print(cnt)