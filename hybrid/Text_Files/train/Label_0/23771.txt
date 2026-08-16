#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#define maxn 200005
#define mid ((nl+nr)>>1)
using namespace std;
typedef long long ll;
const ll mod=998244353;
int n,m;
int cnt[maxn];
map<int,int>pre;
int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++)
	{
		pre[i]=i;
		cnt[i-i]++;
	}
	int ans=0;
	for(int i=1;i<=n;i++)
	{
		int l,r;
		scanf("%d%d",&l,&r);
		int pos=-1;
		for(map<int,int> ::iterator it=pre.lower_bound(l);it!=pre.end() && it->first<=r+1;it=pre.erase(it))
		{
			if(it==pre.end()) break;
			pos=max(pos,it->second);
			cnt[-it->second+it->first]--;
		}
		if(pos!=-1 && r+1<=m)
		{
			pre[r+1]=pos;
			cnt[r+1-pos]++;
		}
		while(!cnt[ans] && ans<m) ans++;
		if(ans>=m)
			printf("-1\n");
		else
			printf("%d\n",i+ans);
	}
}