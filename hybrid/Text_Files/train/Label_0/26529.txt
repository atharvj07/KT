#include <bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i < b; i ++)
using namespace std;
#define mx 4100
#define mn 2050
#define endl '\n'
typedef long long LL;

#define mod 998244353

int n, m;
LL H[mn][mn], C[mx][mx];

void init(){
	C[0][0] = 1;
	rep(i, 1, 4100){
		C[i][0] = 1;
		rep(j, 1, i + 1) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod;
	}
	rep(i, 1, 2050) {
		H[i][0] = 1;
		rep(j, 1, 2050) H[i][j] = C[i + j - 1][j];
	}
}

LL tot[mn][mn], ex[mn][mn], res = 0;

void solve(int N, int M){
	rep(i, 1, N){
		rep(j, 0, M - 1){
			tot[i][j] = H[i][j] * H[i + 1][M - j - 1] % mod;
		}
		tot[i][M - 1] = H[i][M - 1];
	}
	LL up, down, le, ri;
	rep(i, 1, N) {
		up = down = 0;
		rep(j, 0, M) up = (up + tot[i][j]) % mod, down = (down + tot[N - i][j]) % mod;
		res = (res + up * down) % mod;
 	}
 	rep(i, 1, N){
 		rep(j, 0, M){
 			if(j == 0) le = 1;
 			else le = (H[i + 1][j] * H[N - i][j] % mod + H[i][j] * H[N - i + 1][j] % mod) % mod, le = (le - H[i][j] * H[N - i][j] % mod + mod) % mod;
 			if(j == M - 1) ri = 1;
 			else ri = H[i + 1][M - j - 1] * H[N - i + 1][M - j - 1] % mod;
 			res = (res - le * ri % mod + mod) % mod;
		 }
	 }
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
#endif

	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	init();
	int b;
	cin >> n >> m;
	solve(n, m);
	solve(m, n);
	LL le, ri;
	rep(i, 1, n) {
		rep(j, 1, m){
			le = H[i + 1][j - 1] * H[i][m - j] % mod;
			ri = H[n - i + 1][m - j - 1] * H[n - i][j] % mod;
			res = (res - le * ri % mod + mod) % mod;
			le = H[i + 1][m - j - 1] * H[i][j] % mod;
			ri = H[n - i + 1][j - 1] * H[n - i][m - j] % mod;
			res = (res - le * ri % mod + mod) % mod; 
		}
	}
	cout << res << '\n';
	return 0;
}
