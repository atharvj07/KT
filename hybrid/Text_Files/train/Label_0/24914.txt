#include <bits/stdc++.h>
using namespace std;

//&Start
#define lng long long
#define lit long double
#define kk(i,n) "\n "[i<n]
const int inf=0x3f3f3f3f;
const lng Inf=1e17;

//&Data
const int N=1e5+10;
int n,l,t,rk;
struct Ant{
	int x,d;
	friend bool operator<(Ant a,Ant b){return a.x<b.x;}
}ant[N];

//&Main
int main(){
	scanf("%d%d%d",&n,&l,&t);
	for(int i=1;i<=n;i++) scanf("%d%d",&ant[i].x,&ant[i].d);
	for(int i=1;i<=n;i++){
		ant[i].x+=(ant[i].d==1)?t:-t;
		rk+=ant[i].x/l+(ant[i].x%l<0?-1:0);
		((ant[i].x%=l)+=l)%=l;
	}
	sort(ant+1,ant+n+1);
	((rk%=n)+=n)%=n;
	for(int i=rk+1;i<=n;i++) printf("%d\n",ant[i].x);
	for(int i=1;i<=rk;i++) printf("%d\n",ant[i].x);
	return 0;
}