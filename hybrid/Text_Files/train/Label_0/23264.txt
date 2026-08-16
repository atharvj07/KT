#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
set<pair<int, int> > S;
inline int query(int l, int r, int k) {
  auto lit = S.upper_bound(pair<int, int>(l, 0));
  if (lit == S.end() || lit->second > r) {
    if (k == 1) {
      S.emplace(r, l);
      return r - l + 1;
    } else
      return 0;
  }
  int sum = 0;
  auto rit = lit;
  while (rit != S.end() && rit->second <= r) {
    sum += rit->first - rit->second + 1;
    rit++;
  }
  auto it = rit;
  it--;
  pair<int, int> lp(l, l - 1), rp(r + 1, r);
  if (lit->second < l) lp = pair<int, int>(lit->second, l - 1);
  if (it->first > r) rp = pair<int, int>(r + 1, it->first);
  S.erase(lit, rit);
  if (k == 1) {
    S.emplace(rp.second, lp.first);
    return rp.second - lp.first + 1 - sum;
  } else {
    if (lp.first <= lp.second) S.emplace(lp.second, lp.first);
    if (rp.first <= rp.second) S.emplace(rp.second, rp.first);
    return lp.second - lp.first + 1 + rp.second - rp.first + 1 - sum;
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, q;
  cin >> n >> q;
  int ans = n;
  while (q--) {
    int l, r, k;
    cin >> l >> r >> k;
    ans -= query(l, r, k);
    cout << ans << "\n";
  }
  return 0;
}
