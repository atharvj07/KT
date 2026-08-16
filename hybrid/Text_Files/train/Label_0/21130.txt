#include <bits/stdc++.h>
using namespace std;
int n,m,k,sum,a[105],b[105],c[105],d[105],mp[105];
void dfs(int t1,int t2)
{
	if(t1==n)
	{
		int res=0;
		for(int i=0;i<k;i++)
			res+=d[i]*(mp[b[i]]-mp[a[i]]==c[i]);
		sum=max(sum,res);
		return;
	}
	for(int i=t2;i<=m;i++)
	{
		mp[t1]=i;
		dfs(t1+1,i);
	}
}
int main()
{
	cin>>n>>m>>k;
	for(int i=0;i<k;i++)
	{
		cin>>a[i]>>b[i]>>c[i]>>d[i];
		a[i]--;
		b[i]--;
	}
	dfs(0,1);
	cout<<sum;

	return 0;
}