#include <bits/stdc++.h>
using namespace std;
const int N = 1005, MOD = 1e9 + 7;
int f[N][N], c[N][N];
int mpow(int x, int n) {
	int res = 1;
	while (n) {
		if (n & 1) res = 1LL * res * x % MOD;
		n >>= 1;
		x = 1LL * x * x % MOD;
	}
	return res;
}
int main() {
	c[0][0] = 1;
	for (int i = 1; i < N; ++ i) {
		c[i][0] = 1;
		for (int j = 1; j <= i; ++ j) c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD;
	}
	int n, A, B, C, D;
	scanf("%d%d%d%d%d", &n, &A, &B, &C, &D);
	f[0][A - 1] = 1;
	for (int j = A; j <= B; ++ j) {
		for (int i = 0; i <= n; ++ i) {
			f[i][j] = f[i][j - 1];
			int cc = 1, bb = 1;
			for (int k = 1; k <= D && k * j <= i; ++ k) {
				cc = 1LL * cc * c[n - (i - k * j)][j] % MOD;
				bb = 1LL * bb * mpow(k, MOD - 2) % MOD;
				if (k >= C) (f[i][j] += 1LL * cc * f[i - j * k][j - 1] % MOD * bb % MOD) %= MOD;
			}
		}
	}
	printf("%d\n", f[n][B]);
}

