#include<cstdio>

using namespace std;

typedef long long ll;

#define MOD 1000000007
#define rep(i, n) for(int i = 0; i < n; i++)

int n, a[100000];
int c[100000];

ll mod_pow(ll x, int n){
	if(n == 0) return 1;
	return x * mod_pow(x, n - 1) % MOD;
}

ll solve(){
	rep(i, n){
		if(!(n ^ (a[i] & 1))) return 0;
		if(a[i] >= n) return 0;
	}
	if(c[0] > 1) return 0;
	rep(i, n) if(c[i] > 2) return 0;
	return mod_pow(2, n / 2);
}

int main(){
	scanf("%d", &n);
	rep(i, n){ scanf("%d", &a[i]); c[a[i]]++; }
	printf("%lld\n", solve());
	return 0;
}