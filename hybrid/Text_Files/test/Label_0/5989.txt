#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vint = vector<int>;
using vll = vector<ll>;
constexpr ll LLINF = 1ll << 60;

template<typename T>
struct SegmentTree {
	T id;
	function<T(T, T)> op;
	vector<T> dat;
	int size;

	SegmentTree(int n, T id, function<T(T, T)> op) : id(id), op(op) {
		size = 1;
		while (size < n) size <<= 1;
		dat.assign(size * 2 + 10, id);
	}

	void update(int k, T x) {
		k += size; dat[k] = x;
		while (k > 1) k >>= 1, dat[k] = op(dat[k<<1], dat[(k<<1)|1]);
	}

	void merge(int k, T x) { update(k, op(x, dat[k+size])); }

	T query(int a, int b) {
		T tl = id, tr = id;
		for (int l = a + size, r = b + size; l < r; l >>= 1, r >>= 1) {
			if (l & 1) tl = op(tl, dat[l++]);
			if (r & 1) tr = op(tr, dat[--r]);
		}
		return (op(tl, tr));
	}
};

int main() {
	int N; cin >> N;
	SegmentTree<ll> seg(N, -LLINF, [](ll a, ll b) { return (max(a, b)); } );

	vll A(N);
	for (auto &v : A) cin >> v;

	for (int i = 0; i < N; i++) {
		seg.update(i, 0ll);
	}

	for (int i = 0; i < N; i++) {
		ll dat = seg.query(0, A[i]);
		//cout << dat << " ";
		seg.update(A[i]-1, dat + A[i]);
		//cout << seg.query(A[i]-1, A[i]) << endl;
	}

	cout << (ll)N*(N+1)/2 - seg.query(0, N) << endl;
}

