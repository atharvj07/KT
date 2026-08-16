#include <bits/stdc++.h>
#define Int int64_t

using namespace std;

template <typename T>
struct SegmentTree {
private:
	size_t n;
	vector<T> node;
	T M0;

public:
	SegmentTree(const vector<T>& v, T m0) {
		M0 = m0;
		n = 1;
		while (n < v.size()) { n *= 2; }
		node.assign(2*n - 1, M0);

		for (int i = 0; i < v.size(); ++i) {
			node[n - 1 + i] = v[i];
		}
		for (int i = n - 2; i >= 0; --i) {
			node[i] = merge(node[2*i + 1], node[2*i + 2]);
		}
	}

	T merge(T a, T b) { return max(a, b); }

	void update(int x, T val) {
		x += (n - 1);
		node[x] = val;
		while (x > 0) {
			x = (x - 1) / 2;
			node[x] = merge(node[2*x + 1], node[2*x + 2]);
		}
	}

	T query(int a, int b, int k=0, int l=0, int r=-1) {
		if (r < 0) { r = n; }
		if ((r <= a) || (b <= l)) { return M0; }
		if ((a <= l) && (r <= b)) { return node[k]; }

		T vl = query(a, b, 2*k + 1, l, (l + r) / 2);
		T vr = query(a, b, 2*k + 2, (l + r) / 2, r);
		return merge(vl, vr);
	}
};

int main() {
	int N, Q;
	cin >> N >> Q;
	vector<int> A(N), T(Q), x(Q), y(Q);
	for (int i = 0; i < N; ++i) { cin >> A[i]; }
	for (int i = 0; i < Q; ++i) {
		cin >> T[i] >> x[i] >> y[i];
	}

	SegmentTree<int> seg(A, 0);
	vector<int> ans;
	for (int i = 0; i < Q; ++i) {
		if (T[i] == 1) {
			seg.update(x[i] - 1, y[i]);
		}
		if (T[i] == 2) {
			ans.push_back(seg.query(x[i] - 1, y[i]));
		}
		if (T[i] == 3) {
			int l = x[i] - 1, r = N;
			if (seg.query(l, N) < y[i]) {
				ans.push_back(N + 1);
				continue;
			}

			while (r - l > 1) {
				int m = (r + l) / 2;
				(seg.query(l, m) < y[i] ? l : r) = m;
			}
			ans.push_back(l + 1);
		}
	}
	for (auto v : ans) { cout << v << "\n"; }

	return 0;
}
