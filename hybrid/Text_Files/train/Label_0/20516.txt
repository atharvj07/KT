#include <bits/stdc++.h>
using namespace std;
bool comp(const pair<long long, long long>& a,
          const pair<long long, long long>& b) {
  return a.first + a.second > b.first + b.second;
}
signed main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long T = 1;
  while (T--) {
    long long n, r;
    cin >> n >> r;
    vector<pair<long long, long long>> v(n), vp, vn;
    for (auto it : v) {
      long long l, r;
      cin >> l >> r;
      if (r >= 0)
        vp.push_back({l, r});
      else
        vn.push_back({l, r});
    }
    sort(vp.begin(), vp.end());
    sort(vn.begin(), vn.end(), comp);
    bool ok = true;
    for (auto p : vp) {
      if (r >= p.first)
        r += p.second;
      else
        ok = false;
    }
    for (auto p : vn) {
      if (r >= p.first)
        r += p.second;
      else
        ok = false;
    }
    if (r < 0) ok = false;
    if (ok)
      cout << "YES\n";
    else
      cout << "NO\n";
  }
  return 0;
}
