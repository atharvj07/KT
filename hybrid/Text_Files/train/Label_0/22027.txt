#include <bits/stdc++.h>
using namespace std;
long long int power[200005];
void init() {
  power[0] = 1;
  for (long long int i = 1; i < 200005; i++) {
    power[i] = (2 * power[i - 1]) % 998244353;
  }
}
void solve() {
  string s1, s2;
  long long int n, m;
  cin >> n >> m;
  cin >> s1 >> s2;
  long long int k = max(n, m);
  if (n > m) {
    string s = "";
    long long int t = (n - m);
    for (long long int i = 0; i < (t); i++) {
      s += "0";
    }
    s2 = s + s2;
  } else {
    string s = "";
    long long int t = (m - n);
    for (long long int i = 0; i < (t); i++) {
      s += "0";
    }
    s1 = s + s1;
  }
  init();
  long long int ans = 0;
  long long int cnt[200005];
  for (long long int i = 0; i < 200005; i++) {
    cnt[i] = 0;
  }
  for (long long int i = 0; i < k; i++) {
    if (s2[i] == '1') {
      cnt[i] = 1;
    }
  }
  for (long long int i = 1; i < 200005; i++) {
    cnt[i] += cnt[i - 1];
  }
  for (long long int i = 0; i < k; i++) {
    if (s1[k - i - 1] == '1') {
      ans = (ans % 998244353 +
             (cnt[k - i - 1] % 998244353 * power[i] % 998244353) % 998244353) %
            998244353;
    }
  }
  cout << ans << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int tests = 1;
  while (tests--) {
    solve();
  }
}
