#include <bits/stdc++.h>
using namespace std;
int32_t main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  long long n;
  cin >> n;
  vector<long long> N(n);
  for (long long &x : N) cin >> x;
  vector<long long> maxtill(n);
  long long mx = -1;
  for (long long i = 0; i < n; i++) {
    mx = max(mx, N[i]);
    maxtill[i] = mx;
  }
  long long now = 0;
  long long m;
  cin >> m;
  while (m--) {
    long long w, h;
    cin >> w >> h;
    cout << max(maxtill[w - 1], now) << endl;
    now = max(maxtill[w - 1], now) + h;
  }
  return 0;
}
