#include <bits/stdc++.h>

const int N = 100005;

int n, k;
struct perm {
	int p[N];
	int& operator [] (int index) { return p[index]; }
	int operator [] (int index) const { return p[index]; }
	perm inverse() const {
		static perm tmp;
		for (int i = 1; i <= n; ++i)
			tmp[p[i]] = i;
		return tmp;
	}
	friend perm operator * (const perm &a, const perm &b) {
		static perm tmp;
		for (int i = 1; i <= n; ++i)
			tmp[i] = a[b[i]];
		return tmp;
	}
	perm pow(int k) const {
		static bool vis[N];
		static int cycle[N], id[N], tot;
		static perm tmp;
		for (int i = 1; i <= n; ++i) if (!vis[i]) {
			int j = i;
			tot = 0;
			do {
				id[j] = tot, cycle[tot++] = j, vis[j] = 1, j = p[j];
			} while (j != i);
			j = i;
			do {
				tmp[j] = cycle[(id[j] + k) % tot], j = p[j];
			} while (j != i);
		}
		return tmp;
	}
} p, q, t, s;


int main() {
	std::ios::sync_with_stdio(0), std::cin.tie(0);
	std::cin >> n >> k;
	for (int i = 1; i <= n; ++i) std::cin >> p[i];
	for (int i = 1; i <= n; ++i) std::cin >> q[i];
	t = q * p.inverse() * q.inverse() * p;
	switch (k % 6) {
		case 0: 
			s = q.inverse() * p; break;
		case 1:
			s = p; break;
		case 2:
			s = q; break;
		case 3:
			s = q * p.inverse(); break;
		case 4:
			s = t * p.inverse(); break;
		case 5:
			s = t * q.inverse(); break;
	}
	t = t.pow(k / 6), s = t * s * t.inverse();
	for (int i = 1; i <= n; ++i) std::cout << s[i] << ' ';
	std::cout << '\n';
	return 0;
}