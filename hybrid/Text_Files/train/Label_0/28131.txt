#include <bits/stdc++.h>
#define int long long
using std::cin;
using std::cout;

const int N = 105;

int f[N][N][N], g[N][N], p[N][N], mo;

signed main() {
	int n, m, k; 
	cin >> n >> m >> k >> mo;
	f[0][0][0] = 1;
	for (int i = 0; i <= 100; ++ i) {
		g[i][0] = 1;
		for (int j = 1; j <= i; ++ j) {
			g[i][j] = (g[i - 1][j] + g[i - 1][j - 1]) % mo;
		}
	}
	for (int i = 0; i <= 100; ++ i) {
		p[i][0] = 1;
		for (int j = 1; j <= 100; ++ j)  {
			p[i][j] = p[i][j - 1] * i % mo;
		}
	}
	for (int h = 1; h <= k; ++ h) {
		for (int i = 0; i <= n; ++ i) {
			for (int j = 0; j <= m; ++ j) {
				for (int t = (p[k - h + 1][j] * ((p[h][m - j] - p[h - 1][m - j] + mo) % mo)) % mo, s = 1, l = i; l <= n; ++ l) {
					(f[h][l][j] += (s * g[n - i][l - i] % mo * f[h - 1][i][j] % mo)) %= mo;
					(s *= t) %= mo;
				}
			}
		}
		for (int i = 0; i <= n; ++ i) {
			for (int j = m; ~j; -- j) {
				for (int t = (p[h][n - i] * ((p[k - h + 1][i] - p[k - h][i] + mo) % mo)) % mo, s = 1, l = j + 1; l <= m; ++ l) {
					(s *= t) %= mo;
					(f[h][i][l] += (s * g[m - j][l - j] % mo * f[h][i][j] % mo)) %= mo;
				}
			}
		}
	}
	cout << f[k][n][m] << '\n';
	return 0;
}