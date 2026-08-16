#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 5;
const int mod = 1e9 + 7;
string a, s[maxn];
long long val[10], base[10];
int f(char c) { return c - '0'; }
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int m;
  cin >> a >> m;
  for (int i = 0; i < 10; i++) {
    val[i] = i;
    base[i] = 10;
  }
  for (int i = 1; i <= m; i++) cin >> s[i];
  for (int i = m; i >= 1; i--) {
    int L = s[i].size(), res = s[i][0] - '0';
    long long v = 0, b = 1;
    for (int j = L - 1; j > 2; j--) {
      v = (v + val[f(s[i][j])] * b) % mod;
      b = (b * base[f(s[i][j])]) % mod;
    }
    val[res] = v;
    base[res] = b;
  }
  long long ans = 0, b = 1;
  int L = a.size();
  for (int i = L - 1; i >= 0; i--) {
    ans = (ans + b * val[f(a[i])]) % mod;
    b = (b * base[f(a[i])]) % mod;
  }
  cout << ans << endl;
  return 0;
}
