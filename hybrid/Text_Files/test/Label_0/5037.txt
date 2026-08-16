#include<bits/stdc++.h>
using namespace std;
const int maxn=1e5+10;
int n,m,x,y,ind[maxn];
signed main()
{
	cin>>n>>m;
	for(int i=1;i<=m;i++)cin>>x>>y,ind[x]++,ind[y]++;
	for(int i=1;i<=n;i++)	
	if(ind[i]&1)puts("NO"),exit(0);
	puts("YES");
	return 0;
}