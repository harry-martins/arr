N,K=map(int,input().split())
a=[]
a=[int(i) for i in input().split()]
r=0
n=0
while K>0:
	n+=a[r]
	K=K-1
	r=r+1
print(n)
