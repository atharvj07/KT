#include <bits/stdc++.h>
using namespace std;
const long long INF = 1e9;
const long long N = 1e5;
const long long mod = 1e9 + 7;
const long double eps = 1E-7;
long long n, mx, mn = 1e9, cnt, m, ans;
void solve() {
  string s;
  cin >> s;
  string s1, s2;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] % 2 == 0)
      s1 += s[i];
    else
      s2 += s[i];
  }
  merge(s1.begin(), s1.end(), s2.begin(), s2.end(), s.begin());
  cout << s << endl;
}
int main() {
  ios_base::sync_with_stdio(0);
  long long T;
  cin >> T;
  while (T--) {
    solve();
  }
}
