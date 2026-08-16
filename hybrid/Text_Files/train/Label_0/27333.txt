#include<bits/stdc++.h>
using namespace std;
#define RI register int
const int N=200005;
int n,K,tag,l,r,a[N*3];char S[N];
void print() {for(RI i=l;i<=r;++i) putchar(a[i]^tag?'A':'B');}
int main()
{
	scanf("%d%d",&n,&K);
	scanf("%s",S+1);
	for(RI i=1;i<=n;++i) a[i]=(S[i]=='A');
	l=1,r=n,tag=0;
	for(RI i=1;i<=n+n;++i) {
		if(a[l]^tag) a[l]^=1;
		else tag^=1,++l,a[++r]=tag^1;
		if(i==K) {print();return 0;}
	}
	if((n&1)&&(K&1)) a[l]^=1;
	print();
	return 0;
}