#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<string.h>
#include<math.h>
using namespace std;
const int maxn=3e2+7;
typedef long long ll;
const ll INF=1e18;
int n,m;
ll l,dis[maxn][maxn];
int main()
{
	scanf("%d%d%lld",&n,&m,&l);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(i!=j)
				dis[i][j]=INF;
	for(int i=1;i<=m;i++)
	{
		int x,y;
		ll z;
		scanf("%d%d%lld",&x,&y,&z);
		dis[x][y]=dis[y][x]=z;
	}
	for(int k=1;k<=n;k++)
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(dis[i][j]<=l)
				dis[i][j]=1;
			else
				dis[i][j]=INF;
	for(int k=1;k<=n;k++)
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
	int q;
	scanf("%d",&q);
	while(q--)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		if(dis[x][y]<INF)
			printf("%lld\n",dis[x][y]-1);
		else
			printf("-1\n");
	}
	return 0;
}