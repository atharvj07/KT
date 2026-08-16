#include<bits/stdc++.h>
using namespace std;
char c[1000];
int vis[128];
int n,ans;
int main(){
	scanf("%d%s",&n,c+1);
	for(int i=1,tmp;i<=n;++i){
		memset(vis,tmp=0,sizeof vis);
		for(int j=1;j<=i;++j){
			if(!vis[c[j]])vis[c[j]]=1;
		}
		for(int j=i+1;j<=n;++j){
			if(vis[c[j]])tmp++,vis[c[j]]=0;
		}
		ans=max(ans,tmp);
	}
	return !printf("%d\n",ans);
}