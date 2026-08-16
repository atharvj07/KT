#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL ans=0;
int a,b,c,d,e,f,g;
int x,y,z;
int main(){
	scanf("%d%d%d%d%d%d%d",&a,&b,&c,&d,&e,&f,&g);
	ans=b;
	x=a,y=d,z=e;
	int t=(x&1)+(y&1)+(z&1);
	if (y&1)
		swap(x,y);
	if (z&1)
		swap(z,y);
	if (t>=2){
		if (z>0)
			ans+=3,x--,y--,z--;
	}
	ans+=x/2*2;
	ans+=y/2*2;
	ans+=z/2*2;
	printf("%lld",ans);
	return 0;
}