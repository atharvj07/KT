#include <iostream>

using namespace std;

struct  Node { int p, l, r; };

Node T[100005];
int n, d[100005];

void print(int u) {
	cout << "node " << u << ": ";
	cout << "parent = " << T[u].p << ", ";
	cout << "depth = " << d[u] << ", ";

	if (T[u].p == -1) cout << "root, ";
	else if (T[u].l == -1)cout << "leaf, ";
	else cout << "internal node, ";

	cout << "[";
	for (int i = 0, c = T[u].l; c != -1; ++i, c = T[c].r) {
		if (i) cout << ", ";
		cout << c;
	}
	cout << "]" << endl;
}

void rec(int u, int p) {
	d[u] = p;
	if (T[u].r != -1) rec(T[u].r, p);
	if (T[u].l != -1) rec(T[u].l, p + 1);
}

int main() {
	int d, v, c, l, r; cin >> n;
	for (int i = 0; i < n; ++i) T[i].p = T[i].l = T[i].r = -1;

	for (int i = 0; i < n; ++i) {
		cin >> v >> d;
		for (int j = 0; j < d; ++j) {
			cin >> c;
			if (j == 0) T[v].l = c;
			else T[l].r = c;
			l = c;
			T[c].p = v;
		}
	}
	for (int i = 0; i < n; ++i)
		if (T[i].p == -1) r = i;

	rec(r, 0);
	for (int i = 0; i < n; ++i) print(i);

	return 0;
}
