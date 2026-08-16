#include <bits/stdc++.h>

#define rep(i, x, n) for (int i = x; i < n; i++)
typedef long long ll;

const int INF = 1e9 + 7;

using namespace std;

vector<vector<pair<int, ll>>> tree(100001);
vector<ll> cost(100001);

void dfs(int c, int p, ll v) {
	cost[c] = v;
	for (pair<int, int> tmp : tree[c]) {
		if (tmp.first != p) {
			dfs(tmp.first, c, v + tmp.second);
		}
	}
}

int main()
{
	cin.tie(0); ios::sync_with_stdio(false);

	int n;
	cin >> n;

	rep (i, 0, n - 1) {
		int a, b, c;
		cin >> a >> b >> c;

		tree[a].push_back(make_pair(b, c));
		tree[b].push_back(make_pair(a, c));
	}

	int q, k;
	cin >> q >> k;

	dfs(k, -1, 0);

	rep (i, 0, q) {
		int x, y;
		cin >> x >> y;

		cout << cost[x] + cost[y] << endl;
	}

	return 0;
}
