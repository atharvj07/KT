#include<bits/stdc++.h>
#define N 805
using namespace std;
int n,m,k,a[N][N],sx,sy,dis[N][N];
int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
char s[N];
pair<int,int>q[N*N];
int main()
{
	scanf("%d%d%d",&n,&m,&k);
	for (int i=1;i<=n;i++)
	{
		scanf("%s",s+1);
		for (int j=1;j<=m;j++)
		{
			if (s[j]=='S') sx=i,sy=j;
			if (s[j]=='#') a[i][j]=1;
		}
	}
	int l=0,r=1,Ans=100000000;
	q[1]=make_pair(sx,sy);
	memset(dis,0x3f ,sizeof dis);
	dis[sx][sy]=0;
	while(l<r)
	{
		l++;
		int x=q[l].first,y=q[l].second;
	//	cout<<x<<' '<<y<<endl;
		Ans=min(Ans,min(min(x-1,n-x),min(y-1,m-y)));
		if (dis[x][y]<k)
		{
			for (int i=0;i<4;i++)
				if (x+dx[i]&&y+dy[i]&&x+dx[i]<=n&&y+dy[i]<=m&&dis[x+dx[i]][y+dy[i]]>10000000&&a[x+dx[i]][y+dy[i]]==0)
				{
					q[++r]=make_pair(x+dx[i],y+dy[i]);
					dis[x+dx[i]][y+dy[i]]=dis[x][y]+1;
				}
		}
	}
//	cout<<Ans<<endl;
	printf("%d\n",(Ans+k-1)/k+1);
}