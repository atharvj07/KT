#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:1000000000,1000000000")
using namespace std;
const long long inf = 1e18 + 7;
const long long mod = 1e9 + 7;
const double eps = 1e-12;
const double PI = 2 * acos(0.0);
const double E = 2.71828;
map<pair<long long, long long>, pair<long long, long long> > f;
pair<long long, long long> dfs(long long v, long long d) {
  pair<long long, long long> ans = make_pair(0, 0);
  if (!v) return ans;
  if (v <= 9) {
    ans.first = 1;
    if (v < d) ans.second = d - v;
    return ans;
  }
  pair<long long, long long> st = make_pair(v, d);
  if (f.count(st)) return f[st];
  long long next = 1;
  while (next <= v / 10) next *= 10LL;
  while (true) {
    long long now = v / next;
    long long nd = max(d, now);
    pair<long long, long long> res = dfs(v % next, nd);
    v -= v % next;
    ans.first += res.first;
    if (res.second > 0)
      v -= res.second;
    else {
      v -= nd;
      if (nd) ans.first++;
    }
    if (!now) break;
  }
  ans.second = -v;
  return f[st] = ans;
}
int main(void) {
  long long n;
  cin >> n;
  cout << dfs(n, 0).first << endl;
  return 0;
}
