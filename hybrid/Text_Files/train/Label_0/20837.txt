#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-7;
const int MOD = (int)1e9 + 7;
const int MAXN = (int)1e5 + 10;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int v1, v2, t, d, ans = 0;
  cin >> v1 >> v2 >> t >> d;
  ans = v1 + v2;
  for (int i = 2; i < t; ++i) {
    if (v2 < v1) swap(v1, v2);
    v1 += d;
    ans += v1;
  }
  cout << ans << '\n';
  return 0;
}
