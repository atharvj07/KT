#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#define rep(i,l,r) for(int i=(l);i<=(r);++i)
#define per(i,r,l) for(int i=(r);i>=(l);--i)
using namespace std;
typedef long long ll;
const int maxn=1e5+10;
int n,L,T,x,w,a[maxn];ll cnt;
int main(){
	scanf("%d%d%d",&n,&L,&T);
	rep(i,0,n-1){
		scanf("%d%d",&x,&w);
		if(w==1){
			a[i]=(x+T)%L;
			cnt+=(x+T)/L;
		}
		else{
			a[i]=(x-T)%L;
			cnt+=(x-T)/L;
			if(a[i]<0) a[i]+=L,--cnt;
		}
	}
	sort(a,a+n);cnt=(cnt%n+n)%n;
	rep(i,0,n-1) printf("%d\n",a[(cnt+i)%n]);
	return 0;
}