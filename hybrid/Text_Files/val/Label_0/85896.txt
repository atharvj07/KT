#include <bits/stdc++.h>
using namespace std;
int minn[67108864];
int has[200005],f[200005];
char s[200005];
inline int min(int a,int b)
{return a<b?a:b;}
int main (){
	scanf ("%s",s+1);
	int n=strlen(s+1),i,j;
	memset (minn,0x3f,sizeof(minn));
	memset (f,0x3f,sizeof(f));
	for (i=1;i<=n;i++)
	{has[i]=has[i-1]^(1<<(s[i]-'a'));}
	f[0]=0;minn[0]=0;
	for (i=1;i<=n;i++)
	{for (j=0;j<26;j++)
	{f[i]=min(f[i],minn[has[i]^(1<<j)]+1);}
	f[i]=min(f[i],minn[has[i]]+1);
	minn[has[i]]=min(minn[has[i]],f[i]);
	}
	printf ("%d\n",f[n]);
	return 0;
}