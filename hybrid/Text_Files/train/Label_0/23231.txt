#include <bits/stdc++.h>
using namespace std;
int N;
long double W, B, P;
pair<long double, long double> bus[10001];
bool win = true;
long double ans;
int main() {
  ios_base::sync_with_stdio(false);
  if (fopen("cf703c.in", "r")) {
    freopen("cf703c.in", "r", stdin);
    freopen("cf703c.out", "w", stdout);
  }
  cin >> N >> W >> B >> P;
  for (int i = 0; i < N; i++) {
    int a, b;
    cin >> a >> b;
    bus[i].first = a * 1.0;
    bus[i].second = b * 1.0;
    if (bus[i].first * P < bus[i].second * B) {
      win = false;
    }
    ans = max(ans, max(bus[i].first / B, bus[i].second / P) +
                       (W - bus[i].second) / P);
  }
  if (win) {
    cout << fixed << setprecision(20) << W / P << '\n';
    return 0;
  } else {
    cout << fixed << setprecision(20) << ans << '\n';
    return 0;
  }
}
