#include <bits/stdc++.h>
using namespace std;
const int maxn = 2000, mod = 998244353;
char s[maxn + 10];
int f[maxn * 2 + 10][maxn * 2 + 10], n, now;

inline void addto(int &x, int y) {
	x += y; if (x >= mod) x -= mod;
}

int main() {
	scanf("%s", s + 1);
	n = strlen(s + 1);
	f[0][0] = 1;
	for (int i = 1; i <= n * 2; ++i) {
		if (i <= n) {
			if (s[i] == '0') now += 2;
			else if (s[i] == '1') ++now;
		}
		for (int j = 0; j <= i; ++j)
			if (j <= now && i - j <= min(i, n) * 2 - now) {
				f[i][j] = f[i - 1][j];
				if (j) addto(f[i][j], f[i - 1][j - 1]);
			}
	}
	printf("%d", f[n * 2][now]);
}