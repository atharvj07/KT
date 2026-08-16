#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
string cts(char x) {
  string t(1, x);
  return t;
}
long long rand(long long a, long long b) { return a + rng() % (b - a + 1); }
const int MOD = 1e9 + 7;
const int inf = (int)1e9 + 500;
const long long oo = (long long)1e18 + 500;
template <typename T>
void chmax(T& a, T b) {
  a = max(a, b);
}
template <typename T>
void chmin(T& a, T b) {
  a = min(a, b);
}
const int MAXN = -1;
void solve() {
  int n;
  cin >> n;
  vector<int> v;
  for (int i = 1; i <= n; i *= 2) {
    v.push_back(i);
    n -= i;
  }
  if (n > 0) {
    v.push_back(n);
    sort((v).begin(), (v).end());
  }
  cout << v.size() - 1 << '\n';
  for (long long i = 1; i <= (long long)v.size() - 1; ++i) {
    cout << v[i] - v[i - 1] << ' ';
  }
  cout << '\n';
}
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int Q;
  cin >> Q;
  while (Q--) {
    solve();
  }
}
