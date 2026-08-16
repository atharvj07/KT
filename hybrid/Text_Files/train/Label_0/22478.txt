#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 100;
const int inf = 1e9 + 7;
const double eps = 1e-12;
long long n, m, d, x, col[maxn], last;
set<pair<long long, long long> > a;
bool used[maxn];
bool cmp(pair<int, int> a, long long b) { return a.first < b; }
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> m >> d;
  for (int i = 0; i < n; ++i) {
    cin >> x;
    a.insert({x, i});
  }
  int cnt = 0;
  for (auto x : a) {
    if (!used[x.second]) {
      last = -inf;
      used[x.second] = 1;
      col[x.second] = ++cnt;
      long long cur = x.first + d + 1;
      while (true) {
        if (cur > m) break;
        auto y =
            *a.lower_bound(make_pair(cur, numeric_limits<long long>::min()));
        if (cur > y.first || y.second >= n) break;
        if (last + d + 1 <= y.first && !used[y.second]) {
          used[y.second] = 1;
          col[y.second] = cnt;
          last = cur;
          cur = y.first + d + 1;
          a.erase(y);
        } else
          break;
      }
    }
  }
  cout << cnt << endl;
  for (int i = 0; i < n; ++i) cout << col[i] << " ";
  cout << endl;
  return 0;
}
