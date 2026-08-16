#include<algorithm>
#include<iostream>
#include<cstdio>
#define LL long long
using namespace std;
int n,m;
LL mn,ans,x;
const int N=2010,mod=1000000007;
int fa[N];
LL tans[N];
struct bian
{
	int x,y,z;
	friend bool operator <(const bian &a,const bian &b)
		{return a.z<b.z;}
}e[N];
void Init(){for(int i=1;i<=n;++i)fa[i]=i;}
int find(int x){return x==fa[x]?fa[x]:fa[x]=find(fa[x]);}
LL ksm(LL a,LL b,LL mod)
{
	LL res=1;
	for(;b;b>>=1,a=a*a%mod)
		if(b&1)res=res*a%mod;
	return res;
}
LL get(int c)
{
	LL res=0;
	for(int i=1,x,y;i<=m;++i)
	{
		x=find(e[i].x);y=find(e[i].y);
		if(x==y)continue;
		res+=e[i].z;++c;fa[x]=y;
		if(c==n-1)break;
	}
	return res;
	return res;
}
int main()
{
	cin>>n>>m>>x;
	for(int i=1;i<=m;++i)scanf("%d%d%d",&e[i].x,&e[i].y,&e[i].z);
	sort(e+1,e+1+m);Init();mn=get(0);
	if(mn>x)return puts("0")==2333;
	if(mn==x)(ans+=(ksm(2,n-1,mod)-2)*ksm(2,m-n+1,mod))%=mod;
	for(int i=1;i<=m;++i)
		Init(),fa[e[i].x]=fa[e[i].y],tans[i]=get(1)+e[i].z;
	sort(tans+1,tans+1+m);
	for(int i=n;i<=m;++i)
		if(tans[i]==x)(ans+=ksm(2,m-i+1,mod))%=mod;
	cout<<ans;
	return 0;
}