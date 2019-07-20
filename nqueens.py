
def valid_move(chess,col,row):
    c=1
    for i in range(col-1,-1,-1):
        if chess[i]==row:
        #Rooks move
            return False
        #above knights move
        if chess[i]==row-c:
            return False
        #below knights move
        if chess[i]==row+c:
            return False
        c+=1
    return True
            



def solve(chess,col,size):
    if col == size:
        return True
    for i in range(size):
        if valid_move(chess,col,i):
            chess[col]=i
            if solve(chess,col+1,size):
                return True
    chess[col]=None
    return False
    

def solve_nqueen(size):
    #size=int(input("please input size of the chess"))
    chess=[None]*size
    
    if solve(chess,0,size):
        print("solved")
        print(chess)
        a=[["." for i in range(size)] for j in range(size)]
        for i in range(size):
            a[chess[i]][i]='Q'
        for i in range(size):
            print(a[i])
        return True
    
    else:
        print("no solution")
        return False


if __name__=='__main__':
    assert solve_nqueen(3)==False
    assert solve_nqueen(4)==True
    chess=[3,0,1,2]
    solve(chess,0,4)
    size=int(input("please input size of the chess"))
    solve_nqueen(size)