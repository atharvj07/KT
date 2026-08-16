#include<bits/stdc++.h> 
using namespace std;
typedef long long ll;
typedef pair<long long,int> pli;
typedef unsigned int ui;
#define l(x) ch[x].l
#define r(x) ch[x].r
#define ls x<<1
#define rs x<<1|1
#define pb push_back
#define fi first
#define se second
const int Inf=0x3f3f3f3f;
const int inf=0xcfcfcfcf;
const int Size=3e6+10;
const int N=2e5+10;
const int ed=(int)(log(100000)/log(2));
inline int read(){
	register int x=0,f=1;
	register char c=getchar();
	while(!isdigit(c)){
		if(c=='-') f=-1;
		c=getchar();
	}
	while(isdigit(c)){
		x=(x<<1)+(x<<3)+(c&15);
		c=getchar();
	}
	return x*f;
}
int head[N],ver[N<<1],nextt[N<<1],deg[N],tot1;
int n,son[N],flag,minn1=0,minn2=0,minn=Inf;
map<int,int> mm;
void add(int x,int y){
	ver[++tot1]=y,nextt[tot1]=head[x],head[x]=tot1,deg[y]++;
	ver[++tot1]=x,nextt[tot1]=head[y],head[y]=tot1,deg[x]++;
}
void dfs(int x,int fa){
	son[x]=1;
	for(int i=head[x];i;i=nextt[i]){
		int y=ver[i];
		if(y==fa) continue;
		dfs(y,x);
		son[x]+=son[y];
	}
}
void dfs2(int x,int goal){
	if(x==goal){
		flag=1;
		return;
	}
	for(int i=head[x];i;i=nextt[i]){
		int y=ver[i];
		if(mm[y]) continue;
		mm[y]=1;minn=min(minn,y);
		dfs2(y,goal);
		if(flag) return;
		mm[y]=0;
	}
}
int count(int x){
	int sum=0;
	for(int i=head[x];i;i=nextt[i]){
		int y=ver[i];
		if(mm[y]) continue;
		sum+=son[y];
	}
	return sum+1;
}
void solve(){
	dfs(0,-1);
	ll sum=1ll*n*(n-1)/2;
	int po=-1,x1=0,x2=1;ll pre2=0,pre=0;
	mm[0]=1;
	pre=count(0)-1;
	ll sum2=0,tmp2=pre;
	for(int i=head[0];i;i=nextt[i]){
		int y=ver[i];
		if(son[y]==tmp2) continue;
		sum2+=1ll*son[y]*(tmp2-son[y]);
		tmp2-=son[y];
	}
	pre+=sum2;
	printf("%lld ",sum-1ll*pre);
	for(int i=1;i<n;i++){
		ll tmp,tmp2;
		if(i==1){
			dfs2(0,1);
			tmp=1ll*count(0);
			tmp2=1ll*count(1);
			printf("%lld ",pre-tmp*tmp2);
			pre=tmp,pre2=tmp2;
		}
		else{
			if(mm[i]==0){
				if(minn1<=i){
					minn=Inf;
					dfs2(x1,i);
					minn1=minn;
				}
				if(flag==0){
					if(minn2<=i){
						minn=Inf;
						dfs2(x2,i);
						minn2=minn;
					}
				}
				else{
					x1=i;
					tmp=count(x1);
					printf("%lld ",pre2*(pre-tmp));
					pre=tmp;
					flag=0;
					continue;
				}
				if(flag==0){
					printf("%lld ",pre*pre2);
					po=i+1;
					break;
				}
				x2=i;
				tmp=count(x2);
				printf("%lld ",pre*(pre2-tmp));
				pre2=tmp;
			}
			else{
				printf("0 ");
			}
		}
		flag=0;
	}
	if(po!=-1){
		for(int i=po;i<=n;i++) printf("0 ");
	}
	else printf("1 ");
	printf("\n");
}
int main(){
	int t=read();
	while(t--){
		n=read();
		for(int i=1;i<n;i++){
			int x=read(),y=read();
			add(x,y);
		}
		solve();
		for(int i=0;i<n;i++) head[i]=0;
		tot1=0,mm.clear();
		minn1=0,minn2=0;
	} 
}




