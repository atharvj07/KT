#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cstring>
#include <functional>
#include <cmath>
#include <complex>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define rep1(i,n) for(int i=1;i<=(n);++i)
#define all(c) (c).begin(),(c).end()
#define fs first
#define sc second
#define pb push_back
#define show(x) cout << #x << " " << x << endl
typedef long long ll;
ll N,X,Y,Z,t,mod=1e9+7;
vector<int> A[1001],B[1001];//t乗したらi-cycleになるものたち,2
ll dp[1001][1001],f[1001][1001],g[1001][1001],fac[1001];
ll ret[1001][1001];
void add(ll &x,ll y){
	x+=y;
	if(x>=mod) x-=mod;
}
ll gcd(ll x,ll y){
	if(y==0) return x;
	return gcd(y,x%y);
}
ll pw(ll a,ll x){
	ll ret=1;
	while(x){
		if(x%2) ret=ret*a%mod;
		a=a*a%mod;
		x/=2;
	}
	return ret;
}
ll inv(ll a){
	return pw(a,mod-2);
}
ll invfac[1001];
int main(){
	fac[0]=1;
	rep(i,1000) fac[i+1]=fac[i]*(i+1)%mod;
	rep(i,1001) invfac[i]=inv(fac[i]);
	cin>>N>>X>>Y>>Z;
	t=abs(X+Z-Y);
	rep1(i,N){
		A[i/gcd(i,t)].pb(i);
	}
	dp[0][0]=1;
	rep1(i,N){
		rep(j,A[i].size()){
			int a=A[i][j];
			int m=a/i;
			rep(k,N/i+1) dp[j+1][k]=0;
			rep(k,N/i+1){//num of cycle
				for(int h=0;k+h*m<=N/i;h++){
					add(dp[j+1][k+h*m],dp[j][k]*invfac[h]%mod*inv(pw(m,h))%mod*pw(i,h*(m-1))%mod);
				}
			}
		}
		rep(k,N/i+1) f[i][k]=dp[A[i].size()][k]*fac[k]%mod;
	}
/*	rep1(i,N){
		cout<<"  cycle"<<i<<endl;
		rep(j,N/i+1){
			printf("f[%d][%d]=%lld\n",i,j,f[i][j]);
		}
		cout<<endl;
	}*/
	rep1(i,N){
		B[i/gcd(i,2)].pb(i);
	}
	dp[0][0]=1;
	rep1(i,N){
		rep(j,B[i].size()){
			int a=B[i][j];
			int m=a/i;
			rep(k,N/i+1) dp[j+1][k]=0;
			rep(k,N/i+1){//num of cycle
				for(int h=0;k+h*m<=N/i;h++){
					add(dp[j+1][k+h*m],dp[j][k]*invfac[h]%mod*inv(pw(m,h))%mod*pw(i,h*(m-1))%mod);
				}
			}
		}
		rep(k,N/i+1) g[i][k]=dp[B[i].size()][k]*fac[k]%mod;
	}
/*	rep1(i,N){
		cout<<"  cycle"<<i<<endl;
		rep(j,N/i+1){
			printf("g[%d][%d]=%lld\n",i,j,g[i][j]);
		}
		cout<<endl;
	}*/
	ret[0][0]=1;
	rep1(i,N){ //using cycle
		rep(j,N+1){
			for(int k=0;i*k+j<=N;k++){ //num
				add(ret[i][i*k+j],ret[i-1][j]*f[i][k]%mod*g[i][k]%mod*inv(pw(i,k))%mod*invfac[k]%mod);
			}
		}
	}
	ll ans=ret[N][N]*fac[N]%mod;
	if(X+Y+Z==0) ans=ans*invfac[N]%mod*pw(N,N)%mod;
	cout<<ans<<endl;
}