#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int MAXN = 2e5+10;
struct node{
	int to,nxt,u;
}e[MAXN*2];
int head[MAXN],l;
void add(int u,int v){
	e[++l].to=v;e[l].u=u;e[l].nxt=head[u];head[u]=l;
}
int f[MAXN];
int fib[MAXN],s[MAXN];int sum;int vis[MAXN<<1];
void dfs(int u,int fa){
	s[u]=1;
	for(int i=head[u];i;i=e[i].nxt){
		int v=e[i].to;
		if(v!=fa){
			vis[i]=1;
			f[v]=u;dfs(v,u);s[u]+=s[v];
		}
	}
}
bool flag=false;
int find(int u,int p){
	int ans=-1;
	for(int i=head[u];i;i=e[i].nxt){
		if(vis[i]){
			int v=e[i].to;
			if(s[v]==fib[p-2]||s[v]==fib[p-1]){
				return i;
			}
			else{
				ans=max(find(v,p),ans);
			}
		}
	}
	return ans;
}
void update(int u){
	s[u]=1;
	for(int i=head[u];i;i=e[i].nxt){
		if(vis[i]){
			int v=e[i].to;
			f[v]=u;
			update(v);
			s[u]+=s[v];
		}
	}
}
bool check=false;
void solve(int u){
	int p=s[u];p=lower_bound(fib,fib+sum+1,p)-fib;
	if(fib[p]!=s[u]) return;
	if(p==0||p==1){
		flag=true;return;
	}
	//if(flag) return;
	int pos=find(u,p);
	if(pos==-1){
		check=true;
		return;
	}
	vis[pos]=0;
	s[u]-=s[e[pos].to];
	f[u]=u;
	update(u);
	solve(u);
	f[e[pos].to]=e[pos].to;
	update(e[pos].to);
	solve(e[pos].to);
}
int main(){
	std::ios::sync_with_stdio(false);
	int n;cin>>n;
	if(n==1){
		cout<<"YES\n";return 0;
	}
	for(int i=1;i<n;i++){
		int u,v;cin>>u>>v;
		add(u,v);add(v,u);
	}
	fib[0]=1,fib[1]=1;sum=2;
	for(int i=2;;i++){
		fib[i]=fib[i-1]+fib[i-2];
		if(fib[i]>2e5){
			sum=i-1;break;
		}
	}
	f[1]=1;
	dfs(1,1);
	solve(1);
	if(flag&&!check) cout<<"YES\n";
	else cout<<"NO\n";
} 
