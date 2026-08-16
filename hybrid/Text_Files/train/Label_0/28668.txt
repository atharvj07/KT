#include<bits/stdc++.h>
#define ll long long
using namespace std;
int n,m,cnt,la,a[200010][2],rt;
char s[200010];
void build(int x,int y){
	a[++cnt][0]=x;a[cnt][1]=y;
}
int main(){
	int i,j;
	scanf("%s",s+1);
	n=strlen(s+1);
	for(i=1;i<n;i++)if(s[i]!=s[n-i])return puts("-1"),0;
	if(s[1]=='0'||s[n]=='1')return puts("-1"),0;
	m=1;rt=1;la=1;
	for(i=2;i<=n;i++)if(s[i]=='1'){
		build(rt,++m);rt=m;
		for(j=1;j<i-la;j++)build(rt,++m);la=i;
	}
	build(rt,++m);
	rt=m;
	for(i=m+1;i<=n;i++)build(rt,i);
	for(i=1;i<n;i++)printf("%d %d\n",a[i][0],a[i][1]);
}