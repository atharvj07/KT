#include <bits/stdc++.h>
using namespace std;
long long MOD = 1000000007;
int main() {
  int t;
  cin >> t;
  while (t--) {
    string s;
    long long x, n;
    s.clear();
    cin >> x >> s;
    n = s.size();
    if (n == 1) {
      cout << 1 << endl;
      continue;
    }
    bool done = 0;
    for (int i = 1; i <= x; i++) {
      if (done) {
        long long left = i, right = n - i + MOD;
        right %= MOD;
        right *= (s[i - 1] - '0');
        right %= MOD;
        n = left + right;
        n %= MOD;
      } else {
        int y = s.size();
        if (s[i - 1] == '1') continue;
        string tmp2 = s.substr(i, y);
        for (int j = 1; j < (s[i - 1] - '0'); j++) s += tmp2;
        n = s.size();
        if (n > x) done = 1;
        if (i > n) break;
        n %= MOD;
      }
    }
    cout << n % MOD << endl;
  }
}
