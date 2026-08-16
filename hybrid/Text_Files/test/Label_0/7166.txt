#include "bits/stdc++.h"
using namespace std;

vector<int> sgt;
int sz{1};

void g() {
	while (sz < 3e5) sz *= 2;
	sgt.resize(2*sz);
}

int f(int l, int r) {
	int ans{};
	l += sz, r += sz;
	while (l <= r) {
		if (l&1) ans = max(ans, sgt[l++]);
		if (!(r&1)) ans = max(ans, sgt[r--]);
		l /= 2, r /= 2;
	}
	return ans;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	
	g();
	int n, k;
	cin >> n >> k;
	vector<int> a(n);
	for (int i = 0; i < n; i++) cin >> a[i];
	
	for (int i = 0; i < n; i++) {
		int z = f(max(0, a[i] - k), min(300000, a[i] + k));
	//	cout << z << endl;
		a[i] += sz;
		sgt[a[i]] = z + 1;
		a[i] /= 2;
		while (a[i]) {
			sgt[a[i]] = max(sgt[2*a[i]], sgt[2*a[i] + 1]);
			a[i] /= 2;
		}
	}
	cout << sgt[1];
}