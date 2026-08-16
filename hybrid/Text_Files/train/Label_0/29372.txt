#include <bits/stdc++.h>
using namespace std;

//https://atcoder.jp/contests/abc120/tasks/abc120_d

const int nm = 1e5;
int n, m, e[nm][2];
long long c, ans[nm];

//union-find
int par[nm], des[nm];
int root(int v) {
	if (par[v] == v)
		return v;
	return root(par[v]);
}
void unite(int x, int y) {
	int rx = root(x);
	int ry = root(y);
	if (rx == ry)
		return;
	c -= (long long) (des[rx] + 1) * (des[ry] + 1);
	if (des[ry] > des[rx])
		swap(rx, ry);
	par[ry] = rx;
	des[rx] += des[ry] + 1;
}
void initUF() {
	for (int i = 0; i < nm; i++)
		par[i] = i;
}

int main() {
	initUF();
	cin >> n >> m;
	for (int i = 0; i < m; i++)
		cin >> e[i][0] >> e[i][1];

	c = (long long) n * (n - 1) / 2;

	for (int i = 0; i < m; i++) {
		ans[m - 1 - i] = c;
		unite(e[m - 1 - i][0], e[m - 1 - i][1]);
	}
	for (int i = 0; i < m; i++)
		cout << ans[i] << endl;
}
