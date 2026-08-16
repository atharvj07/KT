#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  int N;
  vector<int> bit;
  fenwick(int n = 1e5) {
    N = n + 5;
    bit.assign(N, 0);
  }
  void resize(int n) {
    N = n + 5;
    bit.assign(N, 0);
  }
  void update(int x, int val) {
    while (x < N) {
      bit[x] += val;
      x += x & -x;
    }
  }
  int sum(int x) {
    int ret = 0;
    while (x > 0) {
      ret += bit[x];
      x -= x & -x;
    }
    return ret;
  }
};
int main() {
  ios_base::sync_with_stdio(0);
  cout.tie(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> idx(n + 5);
  for (int i = 1; i <= n; ++i) {
    int x;
    cin >> x;
    idx[x] = i;
  }
  fenwick bit(n);
  set<long long, greater<long long>> l;
  set<long long> r;
  long long lsum = 0, rsum = 0, ans = 0;
  for (int i = 1; i <= n; ++i) {
    bit.update(idx[i], 1);
    ans += i - bit.sum(idx[i]);
    if (l.size() == 0 || idx[i] < *l.begin())
      l.insert(idx[i]), lsum += idx[i];
    else
      r.insert(idx[i]), rsum += idx[i];
    if (l.size() > r.size() + 1) {
      int x = *l.begin();
      lsum -= x;
      rsum += x;
      l.erase(l.begin());
      r.insert(x);
    } else if (r.size() > l.size()) {
      int x = *r.begin();
      lsum += x;
      rsum -= x;
      l.insert(x);
      r.erase(r.begin());
    }
    long long lcnt = (l.size() * (*l.begin())) - lsum -
                     (1ll * l.size() * (l.size() - 1)) / 2;
    long long rcnt = (rsum - r.size() * (*l.begin())) -
                     (1ll * r.size() * (r.size() + 1)) / 2;
    cout << ans + lcnt + rcnt << ' ';
  }
}
