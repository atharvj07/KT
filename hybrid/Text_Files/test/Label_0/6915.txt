#include<bits/stdc++.h>
using namespace std;
using UL = unsigned int;
using ULL = unsigned long long;
using LL = long long;
#define rep(i, n) for(UL i = 0; i < (n); i++)


UL K, N, Q;

struct RMQ {
	UL N;
	vector<pair<UL, UL>> V;
	static pair<UL, UL> F(pair<UL, UL> l, pair<UL, UL> r) {
		if (l.second) r.first = K - r.first;
		return { (l.first + r.first) % K, l.second ^ r.second };
	}
	void init() {
		N = 1; while (N < ::N) N <<= 1;
		V.resize(N * 2 - 1);
		rep(i, ::N) {
			int a; scanf("%d", &a);
			if (a > 0) V[N - 1 + i] = { (K - a % K) % K, 0 };
			else if (a < 0) V[N - 1 + i] = { (-a) % K, 0 };
			else V[N - 1 + i] = { 0, 1 };
		}
		for (UL i = N - 2; i != ~0u; i--) {
			V[i] = F(V[(i << 1) + 1], V[(i << 1) + 2]);
		}
	}
	void upd(UL p, pair<UL, UL> v) {
		UL i = p + N - 1;
		V[i] = v;
		while (i) {
			i = (i - 1) >> 1;
			V[i] = F(V[(i << 1) + 1], V[(i << 1) + 2]);
		}
	}
	void swap(UL a, UL b) {
		pair<UL, UL> buf = V[N - 1 + b];
		upd(b, V[N - 1 + a]);
		upd(a, buf);
	}
	int query() {
		return (int)(V[0].first + 1) * (V[0].second ? -1 : 1);
	}

} G;

int main() {
	scanf("%u%u%u", &K, &N, &Q);
	G.init();
	rep(i, Q) {
		UL a, b; scanf("%u%u", &a, &b); a--; b--;
		G.swap(a, b);
		printf("%d\n", G.query());
	}
	return 0;
}

