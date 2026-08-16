#include <bits/stdc++.h>
using namespace std;
void USACO(string s) {
  freopen((s + ".in").c_str(), "r", stdin);
  freopen((s + ".out").c_str(), "w", stdout);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, s, t;
  cin >> n >> s >> t;
  s--, t--;
  int a[n];
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    a[i]--;
  }
  for (int k = 0; k < n; ++k) {
    if (s == t) {
      cout << k << "\n";
      return 0;
    }
    s = a[s];
  }
  cout << -1 << "\n";
}
