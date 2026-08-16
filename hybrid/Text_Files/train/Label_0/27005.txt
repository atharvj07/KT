#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#define ll long long
using namespace std;
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
int main(){
	ll a,b;cin>>a>>b;
	if(a<b)swap(a,b);
	ll g=gcd(a,b);ll ans=0;ll fu=g;
	for(int i=2;i<=sqrt(g);i++){
		if(g%i)continue;
		ans++;
		while(g%i==0)g/=i;
	}
	if(g > 1) ans ++;
	cout<<ans+1;
	return 0;
}