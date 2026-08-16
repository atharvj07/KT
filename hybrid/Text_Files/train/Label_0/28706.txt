#include <bits/stdc++.h>
using namespace std;
long long i = 0, j = 0, k = 0;
char arr[101][1001];
void solve() {
  memset(arr, 0, sizeof(arr));
  int n, m, o, t;
  cin >> n >> m >> o >> t;
  for (int i = 0; i <= n - 1; ++i)
    for (int j = 0; j <= m - 1; ++j) cin >> arr[i][j];
  vector<string> v;
  for (i = 0; i < n; ++i) {
    string s = "";
    for (j = 0; j < m; ++j) {
      if (int(arr[i][j]) == 46)
        s += arr[i][j];
      else {
        v.push_back(s);
        s = "";
      }
    }
    v.push_back(s);
  }
  if (2 * o <= t) {
    int tt = 0;
    for (string s : v) tt += (int)(s).size();
    cout << tt * o << endl;
  } else {
    int oo = 0, tt = 0;
    for (string s : v) {
      int ss = (int)(s).size();
      if (ss & 1) {
        oo++;
        tt += ss / 2;
      } else {
        tt += ss / 2;
      }
    }
    cout << oo * o + tt * t << endl;
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int t = 1;
  cin >> t;
  while (t--) solve();
}
