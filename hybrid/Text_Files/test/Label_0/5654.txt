#include<stdio.h>
#include<algorithm>
using namespace std;
int K,N,Max,GCD;

int gcd(int a,int b)
{
	if(!b)return a;
	return gcd(b,a%b);
}

int main()
{
	int i,x;
	
	scanf("%d%d%d",&N,&K,&x);
	Max=GCD=x;
	for(i=2;i<=N;i++)
	{
		scanf("%d",&x);
		Max=max(Max,x);
		GCD=gcd(GCD,x);
	}
	
	if(K%GCD==0&&K<=Max)puts("POSSIBLE");
	else puts("IMPOSSIBLE");
}