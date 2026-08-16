#include <iostream>
#include <cstring>
using namespace std;

using cat = long long;

cat pw(cat a, cat e, cat mod) {
	if(e <= 0) return 1;
	cat x = pw(a, e/2, mod);
	return (e&1) ? x * x % mod * a % mod : (x * x % mod);
}

int main() {
	int R, C, K;
	cat mod;
	cin >> R >> C >> K >> mod;
	cat fac[102], fac_inv[102];
	fac[0] = fac_inv[0] = 1;
	for(int i = 1; i <= 100; i++) {
		fac[i] = fac[i-1] * i % mod;
		fac_inv[i] = fac_inv[i-1] * pw(i, mod-2, mod) % mod;
	}
	int dp[102][102];
	memset(dp, 0, sizeof(dp));
	dp[C][R] = 1;
	for(int k = 0; k < K; k++) {
		static cat dpw[102];
		for(int i = 0; i <= 100; i++) {
			dpw[i] = (pw(k+1, i, mod) - pw(k, i, mod)) % mod;
			if(dpw[i] < 0) dpw[i] += mod;
		}
		for(int c = 0; c <= C; c++) {
			static cat coef_x[102];
			cat p = (pw(K-k, C-c, mod) - pw(K-k-1, C-c, mod)) * pw(k+1, c, mod) % mod, pw_p = 1;
			if(p < 0) p += mod;
			for(int i = 0; i <= R; i++) {
				coef_x[i] = fac_inv[i] * pw_p % mod;
				pw_p = pw_p * p % mod;
			}
			static int coef_y[102][102];
			for(int i = 0; i <= R; i++) {
				cat a = dpw[i] * pw(K-k, R-i, mod) % mod, pw_a = 1;
				for(int j = 0; j <= C-c; j++) {
					coef_y[i][j] = fac_inv[j] * pw_a % mod;
					pw_a = pw_a * a % mod;
				}
			}
			cat mod2 = mod * mod * 5;
			static int inner_sum[102];
			for(int i = 0; i <= R; i++) {
				cat s = 0;
				for(int j = 0; j <= C-c; j++) {
					s += 1LL * dp[c+j][i] * coef_y[i][j];
					if(s >= mod2) s -= mod2;
				}
				inner_sum[i] = s % mod;
			}
			for(int r = 0; r <= R; r++) {
				cat s = 0;
				for(int x = r; x <= R; x++) {
					s += inner_sum[x] * coef_x[x-r];
					if(s >= mod2) s -= mod2;
				}
				dp[c][r] = s % mod;
			}
		}
	}
	cout << dp[0][0] * fac[R] % mod * fac[C] % mod << "\n";
}
