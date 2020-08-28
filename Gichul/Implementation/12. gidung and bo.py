#구현
#카카오
#https://programmers.co.kr/learn/courses/30/lessons/60059
# n = int(input())
# build_frame = []
# for _ in range(n):
#     build_frame.append(list(map(int,input().split())))
def possible(answer):
    for x,y,stuff in answer:
        if stuff ==0 : #설치된 것이 '기둥인 경우'
            #바닥 위 혹은 보의 한쪽끝위 혹은 다른 기둥위 라면 정상
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff ==1 : #설치된 것이 '기둥인 경우'
            #바닥 위 혹은 보의 한쪽끝위 혹은 다른 기둥위 라면 정상
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate  = frame
        if operate == 0: #삭제시
            answer.remove([x,y,stuff]) #일단 삭제후
            if not possible(answer):#가능한지 확인
                answer.append([x,y,stuff])#불가능하면 다시 설치
        if operate == 1: #설치시
            answer.append([x,y,stuff]) #일단 설치
            if not possible(answer):
                answer.remove([x,y,stuff])

    return sorted(answer)