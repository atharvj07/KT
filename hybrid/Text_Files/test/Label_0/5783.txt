#include <bits/stdc++.h>

using namespace std;

vector<int> edge[100050];
int n;
char fuck[100050];
bool intree[100050];

void build(int pos,int lst)
{
	if(fuck[pos] == 'W') intree[pos] = 1;
	for(auto v : edge[pos])
		if(v != lst)
		{
			build(v,pos);
			intree[pos] |= intree[v];
		}
}

int deg[100050];
int val[100050];
int zj;
int dp1[100050];

void zhijing(int pos,int lst)
{
	dp1[pos] = val[pos];
	for(auto v : edge[pos])
	{
		if(v != lst && intree[v])
		{
			zhijing(v,pos);
			zj = max(zj,dp1[pos] + dp1[v]);
			dp1[pos] = max(dp1[pos],dp1[v] + val[pos]);
		}
	}
}

int main()
{
	scanf("%d",&n);
	for(int i = 1;i < n; ++ i)
	{
		int u,v; scanf("%d%d",&u,&v);
		edge[u].push_back(v);
		edge[v].push_back(u);
	}
	scanf("%s",fuck + 1);
	bool flg = 0;
	for(int i = 1;i <= n; ++ i)
	{
		if(fuck[i] == 'W')
		{
			build(i,0);
			flg = 1;
			break;
		}
	}
	if(!flg)
	{
		printf("0\n");
		return 0;
	}
	int cnt = 0;
	for(int i = 1;i <= n; ++ i)
		if(intree[i])
			for(auto v : edge[i])
				if(intree[v])
				{
					deg[v] ++;
					cnt ++;
				}
	for(int i = 1;i <= n; ++ i)
		if(intree[i])
		{
			if(deg[i] % 2 == 1 && fuck[i] == 'B') cnt ++,val[i] = 2;
			else if(deg[i] % 2 == 0 && fuck[i] == 'W') cnt ++,val[i] = 2;
			else val[i] = 0;
		}
	for(int i = 1;i <= n; ++ i)
		if(intree[i])
		{
			zhijing(i,0);
			printf("%d\n",cnt - zj);
			return 0;
		}
}