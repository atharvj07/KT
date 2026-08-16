#include <bits/stdc++.h>
using namespace std;
int s[100001][11];
int main() {
  ios_base::sync_with_stdio(false);
  memset((s), (0), sizeof(s));
  int n, k, w;
  cin >> n >> k >> w;
  string str;
  cin >> str;
  for (int _n(min(k, n)), r(0); r < _n; r++) {
    for (int i = r; i < n; i += k) {
      s[i][r] = str[i] == '1';
    }
    for (int _n(n), i(0); i < _n; i++) s[i][r] += i ? s[i - 1][r] : 0;
  }
  for (int _n(w), q(0); q < _n; q++) {
    int l, r;
    cin >> l >> r;
    --l, --r;
    int rm = (l + k - 1) % k;
    int cnt = s[r][rm] - (l + k - 2 >= 0 ? s[l + k - 2][rm] : 0);
    int need = (r - l + 1) / k - cnt;
    int rest = 0;
    for (int _n(l + k - 1), j(l); j < _n; j++) {
      int m = j % k;
      rest += s[r][m] - (j - 1 >= 0 ? s[j - 1][m] : 0);
    }
    int ans = need + rest;
    cout << ans << endl;
  }
  return 0;
}
