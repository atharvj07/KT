#include <bits/stdc++.h>

using namespace std;

#define FOR(i,n) for(int i = 0 ;i < (n); i++) 
#define sz(c) ((int)c.size())

class UF {
public:
	int n; vector<int> a;
	UF(int n) : n(n), a(n, -1) {}
	int find(int x) {
		return a[x] < 0 ? x : (a[x] = find(a[x]));
	}
	bool unite(int x, int y) {
		x = find(x), y = find(y);
		if (x == y) return false;
		if (a[x] > a[y]) swap(x, y);
		a[x] += a[y];
		a[y] = x;
		n--;
		return true;
	}
	int size(int x) {
		return -a[find(x)];
	}
};

struct P {
	P() {}
	int x, y;
	P(int x, int y) : x(x), y(y) {}
	P operator+(const P& r) const {
		return P(x + r.x, y + r.y);
	}
	P operator-(const P& r) const {
		return P(x - r.x, y - r.y);
	}
};

int cross(P& l, P& r) {
	return l.x * r.y - l.y * r.x;
}
bool on(P a, P b, P c) {
	b = b - a;
	c = c - a;
	return cross(b, c) == 0;
}

P center(P& l, P& r) {
	return P((l.x + r.x) / 2, (l.y + r.y) / 2);
}

struct L {
	P o; P dir;
	L(){};
};

L l[8][8];
bool b[8][8][8][8];

map<vector<int>, int> mp;
int dfs(vector<int> f) {
	if (mp.count(f)) return mp[f];

	bool end = true;
	FOR(i, sz(f)) {
		if (f[i] != 0) end = false;
	}
	if (end) {
		return mp[f] = 0;
	}

	int ans = 100;
	FOR(i, sz(f)) {
		FOR(j, i) {
			if (f[i] == f[j]) continue;
			auto copyed = f;
			FOR(a, sz(f)) FOR(b, a) {
				if (f[b] == f[a]) continue;
				bool er = ::b[i][j][a][b];
				if (er) {
					int to = f[b];
					int from = f[a];
					FOR(c, sz(f)) if (f[c] == from) f[c] = to;
				}
			}
			ans = min(ans,dfs(f));
			f = copyed;
		}
	}

	return mp[f] = ans + 1;
}

int main() {
	int n; cin >> n;
	vector<P> vp;
	FOR(i, n) {
		int x, y; cin >> x >> y; vp.emplace_back(x * 2, y * 2);
	}
	FOR(i, n) FOR(j, n) {
		if (i == j) continue;
		l[i][j].o = center(vp[i], vp[j]);
		auto d = vp[i] - vp[j];
		l[i][j].dir = P(-d.y, d.x);
	}
	FOR(i, n) FOR(j, n) {
		if (i == j) continue;
		FOR(a, n) FOR(b, n) {
			if (a == b) continue;
			bool x = on(l[i][j].o, l[i][j].o + l[i][j].dir, l[a][b].o);
			bool y = on(l[i][j].o, l[i][j].o + l[i][j].dir, l[a][b].o + l[a][b].dir);
			::b[i][j][a][b] = x && y;
		}
	}

	vector<int> p(n);
	FOR(i, n) p[i] = i;

	int ans = dfs(p);
	cout << ans << endl;
}