#include <bits/stdc++.h>
using namespace std;
void solve() {
  long long n, m, k, t;
  cin >> n >> m >> k >> t;
  pair<long long, long long> p[k];
  string s[3] = {"Carrots", "Kiwis", "Grapes"};
  for (int i = 0; i < k; i++) {
    cin >> p[i].first >> p[i].second;
  }
  sort(p, p + k);
  for (int i = 0; i < t; i++) {
    long long a, b;
    cin >> a >> b;
    bool f = 1;
    long long x = (a - 1) * m + b - 1;
    long long y = 0;
    for (int j = 0; j < k; j++) {
      if (p[j].first == a && p[j].second == b) {
        cout << "Waste" << endl;
        f = 0;
        break;
      }
      if (p[j].first < a) {
        y++;
      } else if (p[j].first == a) {
        if (p[j].second < b) {
          y++;
        }
      }
    }
    if (f) {
      cout << s[(x - y) % 3] << endl;
    }
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.precision(8);
  long long t(1);
  while (t--) {
    solve();
  }
  return 0;
}
