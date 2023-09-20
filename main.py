import sltions
import prblms

if __name__ == '__main__':
    
    n = prblms.User().intInput()
    x = prblms.User().listInputInt()
    print(sltions.Sltions().minOperations(x,n))

