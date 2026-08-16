#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#define LL long long
using namespace std;
char s[200010];
int n,last[30],pos[200010],tr[200010],num[30];
void change(int k,int c) {for(int i=k;i<=n;i+=i&-i) tr[i]+=c;}
int get(int k) {int ans=0;for(int i=k;i>=1;i-=i&-i) ans+=tr[i];return ans;}
bool vis[200010];
int main()
{
	scanf("%s",s+1);
	n=strlen(s+1);
	for(int i=1;i<=n;i++)
	{
		int c=s[i]-'a';num[c]++;
		pos[i]=last[c];last[c]=i;
	}
	int tot=0;
	for(int i=0;i<26;i++) tot+=(num[i]&1);
	if(tot>1) return puts("-1"),0;
	memset(vis,false,sizeof(vis));
	LL ans=0;
	for(int i=1;i<=n;i++) change(i,1);
	for(int i=1;i<=n;i++) if(!vis[i])
	{
		int c=s[i]-'a';
		int j=last[c];last[c]=pos[j];
		if(i==j) continue;
		ans+=get(i-1);ans+=(get(n)-get(j));
		change(i,-1);change(j,-1);
		vis[j]=true;
		//printf("%d %d %d %lld\n",i,j,get(n),ans);
	}
	printf("%lld",ans);
}