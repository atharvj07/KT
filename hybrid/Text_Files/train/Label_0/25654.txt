#include <bits/stdc++.h>
using namespace std;

const long long INIT = LLONG_MIN;

class segment_tree {
private:
  int n;
  vector<long long> dat;

  static inline long long func(long long a, long long b) {
    return max(a, b);
  }

  long long query(int a, int b, int k, int l, int r) const {
    if(r <= a || b <= l) return INIT;
    if(a <= l && r <= b) return dat[k];

    const auto vl = query(a, b, k * 2 + 1, l, (l + r) / 2);
    const auto vr = query(a, b, k * 2 + 2, (l + r) / 2, r);
    return func(vl, vr);
  }

public:
  segment_tree(int n_):n(1) {
    while(n < n_) n <<= 1;
    dat.resize(2 * n - 1, INIT);
  }

  void update(int k, long long a) {
    k += n - 1;
    dat[k] = a;
    while(k > 0) {
      k = (k - 1) / 2;
      dat[k] = func(dat[k * 2 + 1], dat[k * 2 + 2]);
    }
  }

  long long query(int a, int b) const {
    return query(a, b, 0, 0, n);
  }
};

inline segment_tree make_segment_tree(const vector<long long> &a, const vector<long long> &weight) {
  const int n = a.size();
  segment_tree res(n);

  for(int i = 0; i < n; ++i) {
    res.update(i, a[i] - weight[i]);
  }

  return res;
}

inline bool ok(int r, long long m, const vector<long long> &vl, const vector<long long> &vr,
	       const segment_tree &left, const segment_tree &right) {

  const int n = vl.size();
  vector<long long> value(n);

  for(int i = 0; i < n; ++i) {
    value[i] = max(vl[i] + left.query(max(0, i - r), i + 1),
		   vr[i] + right.query(i, min(n, i + r + 1)));
  }

  return accumulate(value.begin(), value.end(), 0ll) >= m;
}

int main() {
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  int n, c;
  long long m;
  cin >> n >> m >> c;

  vector<long long> a(n);
  for(auto &e : a) cin >> e;

  vector<long long> vr(n);
  vr.front() = 0;
  for(int i = 1; i < n; ++i) {
    vr[i] = vr[i - 1] + c;
  }

  vector<long long> vl(vr);
  reverse(vl.begin(), vl.end());

  const auto left = make_segment_tree(a, vl);
  const auto right = make_segment_tree(a, vr);

  int low = -1, high = n;
  while(low + 1 < high) {
    const int middle = (low + high) / 2;
    if(ok(middle, m, vl, vr, left, right)) {
      high = middle;
    }
    else {
      low = middle;
    }
  }

  cout << (high == n ? -1 : high) << endl;

  return 0;
}
