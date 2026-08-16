#include <bits/stdc++.h>

const int MAXN = 100010;
int A[MAXN], n;
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int solve() {
	int cx = 0, tot = 0;
	for (int i = 1; i <= n; ++i) if (A[i] > 1)
		cx += A[i] & 1, ++tot;
	if (cx == 1) {
		for (int i = 1; i <= n; ++i) if (A[i] & 1) --A[i];
		int G = 0;
		for (int i = 1; i <= n; ++i) G = gcd(G, A[i]);
		for (int i = 1; i <= n; ++i) A[i] /= G;
		return solve() ^ 1;
	}
	return tot - cx & 1;
}
int main() {
	std::ios_base::sync_with_stdio(false), std::cin.tie(0);
	std::cin >> n;
	for (int i = 1; i <= n; ++i) std::cin >> A[i];
	std::cout << (solve() ? "First\n" : "Second\n");
	return 0;
}
