#include <bits/stdc++.h>
using namespace std;
void fastio() {
  cin.tie(nullptr);
  cin.sync_with_stdio(false);
}
using LL = long long;
using LD = long double;
const LL MOD = 1e9 + 7;
const LL INF = LLONG_MAX;
const LL N = 3e5 + 1;
int main() {
  fastio();
  LL t;
  cin >> t;
  while (t--) {
    LL n;
    cin >> n;
    string s;
    cin >> s;
    LL c = 0;
    for (LL i = 0; i < n - 1; ++i) {
      if (s[i] == s[i + 1]) c++;
    }
    cout << (c + 1) / 2 << "\n";
  }
}
