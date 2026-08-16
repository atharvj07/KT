#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int maxn=200010;
inline int read(){
    int f=1,x=0;char ch=getchar();
    while (ch<'0'||ch>'9'){if (ch=='-') f=-1;ch=getchar();}
    while (ch>='0'&&ch<='9'){x=(x<<1)+(x<<3)+ch-'0';ch=getchar();}
    return f*x;
}

int T,n,k,m;
int vis[maxn],a[maxn];
int main(){
	T=read();
	while (T--){
		memset(vis,0,sizeof(vis));
		n=read();k=read();m=read();
		int x;
		for (int i=1;i<=m;++i){
		    x=read();
		    vis[x]=1;
		}
		int pos=0;
		for (int i=1;i<=n;++i)
		    if (!vis[i]) a[++pos]=i;
		bool fl=0;
		for (int i=k/2+1;i<=pos;++i){
		    if (pos%(k-1)==0&&pos-i+1>=k/2&&a[i]!=a[i-1]+1){
		        puts("YES");
		        fl=1;break;
		    }
		}
		if (fl)continue;
		puts("NO");
	}
}