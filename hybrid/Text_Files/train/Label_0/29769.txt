#include <bits/stdc++.h>
#define int long long
using namespace std;
const int maxn=305;
const int mod=1e9+7;
vector<pair<int,int> >vec[maxn];
int n,m,dp[305][305][305],d[4];
void add(int &x,int y)
{
	x+=y;
	if(x>=mod)x-=mod;
}
bool check(int a,int b,int c)
{
	d[1]=a;d[2]=b;d[3]=c;
	sort(d+1,d+4);
	for(int i=0;i<vec[d[3]].size();++i)
	{
		pair<int,int>p=vec[d[3]][i];
		int now=1;
		if(p.first<=d[2])now++;
		if(p.first<=d[1])now++;
		if(now!=p.second)return 0;
	}return 1;
}
signed main()
{
	 scanf("%lld%lld",&n,&m);
	 for(int i=1;i<=m;++i)
	 {
	 	int l,r,x;
	 	scanf("%lld%lld%lld",&l,&r,&x);
	 	vec[r].push_back(make_pair(l,x));
	 }
	 dp[0][0][0]=1;
	 for(int i=0;i<n;++i)
	 {
	 	for(int j=0;j<n;++j)
	 	{
	 		for(int k=0;k<n;++k)
	 		{
	 			int mx=max(max(i,j),k);
	 			if(check(mx+1,j,k))add(dp[mx+1][j][k],dp[i][j][k]);
	 			if(check(i,mx+1,k))add(dp[i][mx+1][k],dp[i][j][k]);
	 			if(check(i,j,mx+1))add(dp[i][j][mx+1],dp[i][j][k]);
			}
		}
	 }
	 int res=0;
	 for(int i=0;i<=n;++i)
	 {
	 	for(int j=0;j<=n;++j)
	 	{
	 		for(int k=0;k<=n;++k)
	 		{
	 			if(i==n||j==n||k==n)add(res,dp[i][j][k]);
			 }
		 }
	 }
	 cout<<res<<endl;
}