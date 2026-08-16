#include <bits/stdc++.h>
using namespace std;
char S[8005];
int X,Y,n,t,x,f[17000],g[17000],a[17000];
int main(){
	scanf("%s",S+1); n=strlen(S+1);
	scanf("%d%d",&X,&Y);
	for (int i=1;i<=n;++i){
		if (S[i]=='F') ++x; else a[++t]=x,x=0;
	}
	if (x) a[++t]=x;
	f[8000]=1;
	for (int i=1;i<=t;i+=2){
		if (i==1){
			f[8000]=0;
			f[8000+a[1]]=1;
			continue;
		}
		for (int j=0;j<=16000;++j)
		if (f[j]) g[j-a[i]]=g[j+a[i]]=1;
		for (int j=0;j<=16000;++j)
			f[j]=g[j],g[j]=0;
	}
	if (!f[X+8000]){
		puts("No"); return 0;
	}
	memset(f,0,sizeof f);
	f[8000]=1;
	for (int i=2;i<=t;i+=2){
		for (int j=0;j<=16000;++j)
		if (f[j]) g[j-a[i]]=g[j+a[i]]=1;
		for (int j=0;j<=16000;++j)
			f[j]=g[j],g[j]=0;
	}
	if (!f[Y+8000]){
		puts("No"); return 0;
	}
	puts("Yes");
	return 0;
}