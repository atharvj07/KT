#include <bits/stdc++.h>

typedef long long LL;
typedef unsigned long long ULL;

#define debug printf("fuck %d\n", __LINE__);

inline LL read() {
	LL res = 0, bo = 1; char ch = getchar();
	while(ch < '0' || ch > '9') { if (ch == '-') bo = -1; ch = getchar(); }
	while(ch >= '0' && ch <= '9') { res = (res << 1) + (res << 3) + ch - '0'; ch = getchar(); }
	return bo * res;
}

template<typename T> void read(T &x) { x = read(); }
template<typename T, typename ...Argv> void read(T &a, Argv &...argv) { read(a); read(argv...); }

const int N = 405, p = 998244353;
int n, A[N], B[N], SA, SB, inv[N], fac[N], a[N][N], f[N][N][N];

int mul(int x, int y) { return 1LL * x * y % p; }
void add(int &x, int y) { x += y; if (x >= p) x -= p; }
void del(int &x, int y) { x -= y; if (x < 0) x += p; }

int ksm(int x, int y) {
	int res = 1;
	for (; y; y >>= 1, x = mul(x, x)) if (y & 1) res = mul(res, x);
	return res;
}

int main() {
	n = read();
	for (int i = 1; i <= n; ++ i) read(A[i], B[i]), SA += A[i], SB += B[i];
	fac[0] = 1;
	for (int i = 1; i <= 400; ++ i) fac[i] = mul(fac[i - 1], i);
	inv[400] = ksm(fac[400], p - 2);
	for (int i = 399; i >= 0; -- i) inv[i] = mul(inv[i + 1], i + 1);
	for (int i = 1; i <= n; ++ i) {
		a[i][0] = 1;
		for (int j = 1; j <= SB; ++ j) {
			a[i][j] = mul(a[i][j - 1], A[i]);
		}
	}
	f[0][0][0] = p - 1;
	for (int i = 1; i <= n; ++ i) {
		for (int j = 0; j <= SA; ++ j) {
			for (int k = 0; k <= SB; ++ k) {
				// if (!f[i - 1][j][k]) continue;
				add(f[i][j][k], f[i - 1][j][k]);
				for (int l = 0; l < B[i]; ++ l) {
					if (A[i] > j || l > k) break;
					del(f[i][j][k], mul(f[i - 1][j - A[i]][k - l], mul(a[i][l], inv[l])));
				}
			}
		}
	}
	int ans = 0;
	for (int i = 1; i <= SA; ++ i) {
		int inv = ksm(i, p - 2), t = mul(SA, inv);
		for (int j = 0; j <= SB; ++ j) add(ans, mul(f[n][i][j], mul(t, fac[j]))), t = mul(t, inv);
	}
	std::cout << ans << std::endl;
	return 0;
}