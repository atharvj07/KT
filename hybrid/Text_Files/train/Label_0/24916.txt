#include <bits/stdc++.h>
#define rep(i,n) for ((i)=1;(i)<=(n);(i)++)
#define per(i,n) for ((i)=n;(i)>=(1);(i)--)
using namespace std;

int n,l,t;
int rk,i,j;
int a[100005],w[100005],b[100005];
int main(){
	cin>>n>>l>>t;
	for(i=0;i<n;i++){
		cin>>a[i]>>w[i];
		if(w[i]==1) b[i]=(a[i]+t)%l; else b[i]=((a[i]-t)%l+l)%l;
		if(w[i]==1) rk=(rk+1ll*(a[i]+t)/l)%n; else rk=(rk-1ll*(t-a[i]+l-1)/l)%n;
	}
	if(rk<0) rk+=n;
	sort(b,b+n);
	for(i=rk;i<n;i++) cout<<b[i]<<endl;
	for(i=0;i<rk;i++) cout<<b[i]<<endl;
	return 0;
}