#include<bits/stdc++.h>
#define N 100010
using namespace std;
template<typename T>inline void read(T &x)
{
	x=0;
	static int p;p=1;
	static char c;c=getchar();
	while(!isdigit(c)){if(c=='-')p=-1;c=getchar();}
	while(isdigit(c)) {x=(x<<1)+(x<<3)+(c-'0');c=getchar();}
	x*=p;
}
int n;
int h[N],l,q;
int st[N][19];
int main()
{
	read(n);
	for(int i=1;i<=n;i++) read(h[i]);
	read(l);read(q);
	for(int i=1;i<=n;i++)
	{
		int pos=upper_bound(h+1,h+n+1,h[i]+l)-h-1;
		if(h[i]+l>=h[n])st[i][0]=n;
		else st[i][0]=pos;
	}
	for(int len=1;len<=18;len++)
		for(int i=1;i<=n;i++) st[i][len]=st[st[i][len-1]][len-1];
	while(q--)
	{
		static int a,b;
		read(a);read(b);
		if(a>b)swap(a,b);
		int now=a,ans=0;
		for(int i=18;i>=0;i--)
			if(st[now][i]<b)now=st[now][i],ans+=(1<<i);
		printf("%d\n",ans+1);
	}
	return 0;
}