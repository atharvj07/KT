#include <bits/stdc++.h>
const long long INF = 1e18;
const int MOD = 1e9 + 7;
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  string s;
  cin >> s;
  int n = s.size();
  long long b_odd = 0, b_even = 0;
  long long a_odd = 0, a_even = 0;
  long long res = 0, reso = 0;
  for (int i = 0; i < n; ++i) {
    if (i % 2) {
      if (s[i] == 'a')
        a_odd++, res += a_even, reso += a_odd;
      else
        b_odd++, res += b_even, reso += b_odd;
    } else {
      if (s[i] == 'a')
        a_even++, res += a_odd, reso += a_even;
      else
        b_even++, res += b_odd, reso += b_even;
    }
  }
  cout << res << ' ' << reso << '\n';
}
