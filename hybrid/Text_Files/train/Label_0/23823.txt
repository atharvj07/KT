#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define fi first
#define se second
#define eb emplace_back
using namespace std;
const int mod = 1e9 + 7;
const int maxn = 2e5 + 233;
ll fac[maxn],inv[maxn];
int exgcd(int a,int b,int& x,int &y){
	if(b==0){
		x = 1;y = 0;
		return a;
	}
	int d = exgcd(b,a%b,y,x);
	y -= (a/b)*x;
	return d;
}
void init(){
	fac[0] = inv[0] = 1;
	for(int i=1;i<maxn;i++){
		fac[i] = fac[i-1]*i%mod;
		int x,y;
		exgcd(i,mod,x,y);
		x = (x+mod)%mod;
		inv[i] = inv[i-1]*x%mod;
	}
}
inline ll C(int n,int k){
	if(k>n)return 0;
	return fac[n]*inv[k]%mod*inv[n-k]%mod;
}
ll f[21][1010],a[21];
int main()
{
	init();
	int n,k;cin>>n>>k;
	for(int i=1;i<=k;i++)scanf("%d",&a[i]);
	f[0][0] = 1;
	for(int i=0;i<k;i++)
		for(int j=0;j<=n;j++)
			if(f[i][j]){
				for(int x=0;x<=a[i+1];x++){
					if(j+x>n)break;
					ll &s = f[i+1][j+x];
					s = (s+f[i][j]*C(n-x,a[i+1]-x)%mod*inv[x])%mod;
				}
			}
	ll ans = fac[n]*f[k][n] % mod;
	cout << ans << endl;
	return 0;
}
