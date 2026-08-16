#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int n,A[510],B[510];
char ch[510][510];
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%s",ch[i]+1);
	int tot=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++) if (ch[i][j]=='#') tot++,A[j]++,B[i]++;
	if (tot==0){
		printf("-1\n"); return 0;
	}
	int ans=1e9,totw=0;
	for (int i=1;i<=n;i++) if (A[i]==n) totw++;
	for (int i=1;i<=n;i++){
		int num=(n-totw)+(A[i]==0)+(n-B[i]);
		ans=min(ans,num);
	}
	printf("%d\n",ans);
	return 0;
}