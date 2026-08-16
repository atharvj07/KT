#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getint() {
  T x = 0, p = 1;
  char ch;
  do {
    ch = getchar();
  } while (ch <= ' ');
  if (ch == '-') p = -1, ch = getchar();
  while (ch >= '0' && ch <= '9') x = x * 10 + ch - '0', ch = getchar();
  return p == 1 ? x : -x;
}
template <typename T1, typename T2>
bool umin(T1 &x, const T2 &y) {
  if (x > y) {
    x = y;
    return true;
  }
  return false;
}
template <typename T1, typename T2>
bool umax(T1 &x, const T2 &y) {
  if (x < y) {
    x = y;
    return true;
  }
  return false;
}
const int maxn = (int)2e5 + 10;
const int inf = (int)1e9 + 5;
const int mod = (int)1e9 + 7;
const long long llinf = (long long)1e18 + 5;
const long double pi = acos(-1.0);
int solve(vector<pair<int, int> > a, vector<pair<int, int> > b, int n, int m) {
  sort((a).begin(), a.end());
  sort((b).begin(), b.end(),
       [&](pair<int, int> x, pair<int, int> y) { return x.second < y.second; });
  return max(0, a.back().first - b[0].second);
}
int main() {
  ios_base::sync_with_stdio(0);
  int n;
  cin >> n;
  vector<pair<int, int> > a(n);
  for (int(i) = (0); (i) < (n); ++(i)) cin >> a[i].first >> a[i].second;
  int m;
  cin >> m;
  vector<pair<int, int> > b(m);
  for (int(i) = (0); (i) < (m); ++(i)) cin >> b[i].first >> b[i].second;
  cout << max(solve(a, b, n, m), solve(b, a, m, n)) << endl;
  return 0;
}
