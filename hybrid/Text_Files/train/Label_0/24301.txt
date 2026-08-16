#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll inf = 1e18;
const int N = 2 * 1e5 + 10;
ll res;
ll a[N];
void solve() {
  ll h, m, H, D, C, N;
  cin >> h >> m >> H >> D >> C >> N;
  ll gg = (H + N - 1) / N;
  if (h < 20) {
    ll wp = (20 - h - 1) * 60 + (60 - m);
    wp = (H + wp * D + N - 1) / N;
    long double ok = C * 0.8;
    cout << fixed << setprecision(6) << min(1.0 * gg * C, 1.0 * wp * C * 0.8)
         << "\n";
  } else
    cout << fixed << setprecision(6) << gg * C * 0.8 << "\n";
}
int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  ll t = 1;
  while (t--) {
    solve();
  }
}
