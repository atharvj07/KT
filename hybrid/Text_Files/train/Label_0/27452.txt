#include <bits/stdc++.h>

using namespace std;

#define int long long

const int maxn = 2e5;
pair <int, int> t[4 * maxn + 5];
int sum[4 * maxn + 5];
int a[maxn];

void push(int v, int l, int r) {
	if (t[v].first == -1) return;
	if (l == r - 1) {
		sum[v] = t[v].second;
		t[v] = {-1, -1};
		return;
	}
	t[2 * v] = max(t[2 * v], t[v]);
	t[2 * v + 1] = max(t[2 * v + 1], t[v]);
	sum[v] = t[v].second * (r - l);
	t[v] = {-1, -1};
}

void build(int v, int l, int r) {
	t[v] = {-1, -1};
	if (l == r - 1) {
		sum[v] = a[l];
		return;
	}
	int m = (l + r) / 2;
	build(2 * v, l, m);
	build(2 * v + 1, m, r);
	sum[v] = sum[2 * v] + sum[2 * v + 1];
}

void upd(int v, int l, int r, int tl, int tr, pair <int, int> val) {
	if (l >= tr || tl >= r) return;
	if (l <= tl && tr <= r) {
		t[v] = val;
		return;
	}
	push(v, tl, tr);
	int tm = (tl + tr) / 2;
	upd(2 * v, l, r, tl, tm, val);
	upd(2 * v + 1, l, r, tm, tr, val);
	int val1 = sum[2 * v];
	if (t[2 * v].first != -1) val1 = (tm - tl) * t[2 * v].second;
	int val2 = sum[2 * v + 1];
	if (t[2 * v + 1].first != -1) val2 = (tr - tm) * t[2 * v + 1].second;
	sum[v] = val1 + val2;
}

int get(int v, int l, int r, int tl, int tr) {
	if (l >= tr || tl >= r) return 0;
	if (l <= tl && tr <= r) {
		if (t[v].first == -1) return sum[v];
		return (tr - tl) * t[v].second;
	}
	push(v, tl, tr);
	int tm = (tl + tr) / 2;
	int ans1 = get(2 * v, l, r, tl, tm), ans2 = get(2 * v + 1, l, r, tm, tr);
	/*int val1 = sum[2 * v];
	if (t[2 * v].first != -1) val1 = (tm - tr) * t[2 * v].second;
	int val2 = sum[2 * v + 1];
	if (t[2 * v + 1].first != -1) val2 = (tr - tm) * t[2 * v + 1].second;
	sum[v] = val1 + val2;*/
	return ans1 + ans2;
}

void solve() {
	int n, q;
	cin >> n >> q;
	string s, f;
	cin >> s >> f;
	pair <int, int> seg[q];
	for (int i = 0; i < q; ++i) cin >> seg[i].first >> seg[i].second;
	for (int i = 0; i < n; ++i) a[i] = f[i] - '0';
	build(1, 0, n);
	int tmr = 0;
	for (int i = q - 1; i >= 0; --i) {
		int res = get(1, seg[i].first - 1, seg[i].second, 0, n);
		//cout << res << '\n';
		if (res * 2 == seg[i].second - seg[i].first + 1) {
			cout << "NO\n";
			return;
		}
		if (res * 2 > seg[i].second - seg[i].first + 1) upd(1, seg[i].first - 1, seg[i].second, 0, n, {tmr, 1});
		else upd(1, seg[i].first - 1, seg[i].second, 0, n, {tmr, 0});
		++tmr;
	}
	for (int i = 0; i < n; ++i) {
		if (get(1, i, i + 1, 0, n) != s[i] - '0') {
			cout << "NO\n";
			return;
		}
	}
	cout << "YES\n";
}

signed main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;
	while (t) {
		--t;
		solve();
	}
	return 0;
}