#include<bits/stdc++.h>
const int N=5e5+5;
char c[N];
int n,i,a[N],x;
int main(){
	*c='0';scanf("%s",c+1);for(i=1,n=strlen(c+1);i<=n;++i)a[i]=c[i]-c[i-1];
	for(i=n;i;--i)if(a[i]<0)--a[i-1],a[i]+=10,++a[n];
	for(;a[n]>10;)for(i=n;a[i]>=10 && a[n];--i)++a[i-1],a[i]-=10,a[n]--;
	for(i=n-1;i;--i)if(a[i]==10 && a[n])a[i]=0,++a[i-1],--a[n];
	for(x=0,i=1;i<=n;++i)x+=a[i];printf("%d\n",(x+8)/9);
	return 0;
}