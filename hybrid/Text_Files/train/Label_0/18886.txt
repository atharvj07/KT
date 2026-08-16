#include <bits/stdc++.h>
using namespace std;

const int N = 100010;

typedef long long LL;

LL D[N]; int id[N], sz[N];
map<LL, int> mp;

inline void Fuck() {
	puts("-1"), exit(0);
}

vector<int> G[N];

inline void adde(int from, int to) {
	G[from].push_back(to), G[to].push_back(from);
}

LL dfs(int u, int f) {
	LL res = 0;
	for (auto v : G[u]) if (v != f) 
		res += dfs(v, u) + sz[v];
	return res;
}

int main() {
	int n; scanf("%d", &n);
	for (int i = 1; i <= n; i++) scanf("%lld", &D[i]), mp[D[i]] = i, sz[i] = 1, id[i] = i;
	sort(id + 1, id + n + 1, [](int a, int b){return D[a] > D[b];});
	for (int i = 1; i < n; i++) {
		int v = id[i];
		LL tmp = D[v] - n + sz[v] * 2;
		if (!mp.count(tmp) || tmp >= D[v]) Fuck();
		adde(v, mp[tmp]), sz[mp[tmp]] += sz[v];
	}
	if (dfs(id[n], 0) != D[id[n]]) Fuck();
	for (int i = 1; i <= n; i++)
		for (auto v : G[i]) if (v > i) printf("%d %d\n", i, v);
}
