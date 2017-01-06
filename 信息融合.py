#coding = utf-8
def intersect(A,B):
    r = []
    for elem in A:
        if elem in B:
            r.append(elem)    
    return r
def DST(A,B):
    #检查输入参数
    if A[0] != B[0] or  (len(A[1]) != len(B[1])) or len(A[0]) != len(A[1]):
        raise Exception("Invalid arguments!")
    #计算归一化系数
    K = 1.0
    for i in range(len(A[0])):
        for j in range(len(B[0])):
            if len(intersect(A[0][i], B[0][j])) is 0:
                K = K- A[1][i]* B[1][j]
                pass    
    print("归一化系数为：",K)
    r = [[],[]]
    for k  in  range(len(A[0])):
        r[0].append(A[0][k]);r[1].append(0.0)        
        for i in range(len(A[0])):
            for j in range(len(B[0])):
                if intersect(A[0][i], B[0][j]) == A[0][k]:                
                    r[1][k] += A[1][i]* B[1][j] / K
    return r
    
CIA = [[["本",],["萨",],["霍",],["本","萨"],["本","萨","霍"]],[0.4,0.3,0.1,0.1,0.1]]
NSA = [[["本",],["萨",],["霍",],["本","萨"],["本","萨","霍"]],[0.2,0.2,0.05,0.5,0.05]]
if __name__ == '__main__':    
    r = DST(CIA,NSA)
    '''打印输出结果'''
    for i in range(len(r[0])):
        print(r[0][i],r[1][i])