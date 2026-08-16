#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) FOR(i,0,a)
typedef long long ll;
const int MOD=1e9+7;

const int MAX_N=1e3;

int N,A,B,C,D;

ll fact[MAX_N+1];
ll dp[MAX_N+1][MAX_N+1];

ll mod_pow(ll n,int m){
	ll res=1;
	while(m){
		if (m&1) res=res*n%MOD;
		m>>=1;
		n*=n;
		n%=MOD;
	}
	return res;
}

ll mod_inverse(ll n){
	return mod_pow(n,MOD-2);
}

ll comb(int n,int m){
	return fact[n]*mod_inverse(fact[m]*fact[n-m]%MOD)%MOD;
}

int main(){
	cin>>N>>A>>B>>C>>D;
	fact[0]=1;
	FOR(i,1,N+1){
		fact[i]=fact[i-1]*i%MOD;
	}
	REP(i,N+1) dp[0][i]=1;
	FOR(n,1,N+1){
		FOR(b,A,B+1){
			dp[n][b]=dp[n][b-1];
			for(int g=C;g<=D && n-b*g>=0;g++){
				dp[n][b]+=fact[n]*mod_inverse(mod_pow(fact[b],g)*fact[n-b*g]%MOD*fact[g]%MOD)%MOD*dp[n-b*g][b-1]%MOD;
				dp[n][b]%=MOD;
			}
		}
	}
	printf("%lld\n",dp[N][B]);
	return 0;
	}
