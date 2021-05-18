class Solution:
    def setBits(self, N):
        # code here
        p=1
        c=0
        while(N!=0):
            if N&1==1:
                c+=1
            N=N>>1
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)
