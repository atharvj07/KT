#include <bits/stdc++.h>
using namespace std;
const int maxn = 10000 + 5;
pair<double, double> pos[maxn], time_pos[maxn];
int main() {
  double n, w, v, u, ans = 0.0, maxx = 0.0, maxy = 0.0;
  bool crossfirst = true, crosslate = true;
  cin >> n >> w >> v >> u;
  for (int i = 0; i < n; i++) {
    cin >> pos[i].first >> pos[i].second;
    if (maxx < pos[i].first || (maxx == pos[i].first && maxy < pos[i].second)) {
      maxx = pos[i].first;
      maxy = pos[i].second;
    }
    time_pos[i].first = pos[i].first / v;
    time_pos[i].second = pos[i].second;
    if (pos[i].second / u > time_pos[i].first) crossfirst = false;
    if (pos[i].second / u < time_pos[i].first) crosslate = false;
    ans = max(ans, (w - pos[i].second) / u + pos[i].first / v);
  }
  if (crossfirst || crosslate) ans = w / u;
  printf("%.10lf\n", ans);
  return 0;
}
