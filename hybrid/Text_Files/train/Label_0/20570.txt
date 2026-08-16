#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a, b, T, ans = 0;
  cin >> n >> a >> b >> T;
  vector<int> d(n, 1);
  for (int& p : d) {
    char c;
    cin >> c;
    if (c == 'w') p += b;
  }
  vector<int> rtime(n), ltime(n);
  rtime[0] = d[0], ltime[0] = d[0];
  for (int i = 1; i < n; i++) {
    rtime[i] = d[i] + a + rtime[i - 1];
    ltime[i] = d[n - i] + a + ltime[i - 1];
  }
  if (d[0] <= T) ans = 1;
  for (int i = 1; i < n; i++) {
    int time = T - rtime[i];
    if (time >= 0) ans = max(ans, 1 + i);
    time -= i * a;
    if (time > 0) {
      time += d[0];
      int num_left =
          lower_bound(ltime.begin(), ltime.end(), time) - ltime.begin();
      if (ltime[num_left] > time && num_left > 0) num_left--;
      ans = max(ans, 1 + i + num_left);
    }
  }
  for (int i = 1; i < n; i++) {
    int time = T - ltime[i];
    if (time >= 0) ans = max(ans, 1 + i);
    time -= i * a;
    if (time > 0) {
      time += d[0];
      int num_right =
          lower_bound(rtime.begin(), rtime.end(), time) - rtime.begin();
      if (rtime[num_right] > time && num_right > 0) num_right--;
      ans = max(ans, 1 + i + num_right);
    }
  }
  cout << min(n, ans) << endl;
  return 0;
}
