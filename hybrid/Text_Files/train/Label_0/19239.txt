#include<bits/stdc++.h>
using namespace std;
const int p=1e9+7;
const int N=2e5+5;
struct each{
	int c,w;
}a[N];
map<int,int>ma[N];
typedef pair<int,int>P;
typedef set<P>::iterator it;
int n,X,Y,fa[N],fac[N],tot[N];
bool com(each x,each y){
	return x.w<y.w;
}
set<P>s[N];
#define fi first
#define se second
long long fsp(int x,int y){
	int ans=1;
	while(y){
		if(y&1)	ans=1LL*ans*x%p;
		x=1LL*x*x%p,y>>=1;
	}
	return ans;
}
int find(int x){
	return fa[x]!=x?fa[x]=find(fa[x]):x;
}
bool check(int x,int y){
	if(a[x].c==a[y].c)	return a[x].w+a[y].w<=X;
	return a[x].w+a[y].w<=Y;
}
void merge(int i,int x){
	int f=0;
	it j=s[i].begin();
	while(j!=s[i].end()&&check(j->se,x)){
		fa[j->se]=find(x);
		if(!f)	f=1,j++;
		else{
			it k=j++;
			s[i].erase(k);
		}
	}
}
int main(){
	scanf("%d%d%d",&n,&X,&Y),fac[0]=1;
	for(int i=1;i<=n;i++)
		scanf("%d%d",&a[i].c,&a[i].w);
	sort(a+1,a+n+1,com);
	for(int i=1;i<=n;i++)
		s[a[i].c].insert(P(a[i].w,i));
	for(int i=1;i<=n;i++)	fa[i]=i;
	for(int i=1;i<=n;i++)	merge(i,1);
	for(int i=2;i<=n;i++){
		if(check(i,1))	fa[find(1)]=find(i);
		merge(a[i].c,i),merge(a[i-1].c,i);
	}
	for(int i=1;i<=n;i++)
		++ma[find(i)][a[i].c],++tot[find(i)];
	for(int i=1;i<=n;i++)	fac[i]=1LL*fac[i-1]*i%p;

	int ans=1;
	for(int i=1;i<=n;i++)
		if(find(i)==i){
			ans=1LL*ans*fac[tot[i]]%p;
			map<int,int>::iterator it=ma[i].begin();
			for(;it!=ma[i].end();it++)	ans=ans*fsp(fac[it->se],p-2)%p;
		}
	printf("%d\n",ans);
	return 0;
}
