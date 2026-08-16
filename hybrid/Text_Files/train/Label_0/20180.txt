#include<iostream>
#include<queue>
using namespace std;
long long f[101010];
long long x[101010];
long long E,T;
long long calc(int i,int j)
{
	return max(f[j-1]+T,f[j-1]+2*x[i]-2*x[j]);
}
priority_queue<long long> Q;
int main()
{
	int n;
	cin>>n>>E>>T;
	for(int i=1;i<=n;i++)
		cin>>x[i];
	f[1]=T;
	int now=0;
	for(int i=2;i<=n;i++)
	{
		f[i]=f[i-1]+T;
		int l=1,r=i-1;
		while(r>l)
		{
			int m=(l+r)/2;
			if(T-2*x[i]+2*x[m]>=0)
				r=m;
			else
				l=m+1;
		}
		f[i]=min(f[i],max(f[l-1]+T,f[l-1]+2*x[i]-2*x[l]));
		if(l>1)
		{
			while(now<l-1)
			{
				now++;
				Q.push(2*x[now]-f[now-1]);
			}
			f[i]=min(f[i],2*x[i]-Q.top());
		}
	}
	cout<<f[n]+E<<endl;
	return 0;
}