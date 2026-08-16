#include <bits/stdc++.h>
using namespace std;
struct re {
  long long x, y;
};
re r[300005];
re f[300005], b[300005];
re ti(re a, re b) {
  re c;
  c.x = max(a.x, b.x);
  c.y = min(a.y, b.y);
  return c;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  int n;
  cin >> n;
  int i;
  for (i = 1; i <= n; i++) cin >> r[i].x >> r[i].y;
  re b1 = r[1];
  for (i = 1; i <= n; i++) {
    b1 = ti(b1, r[i]);
    f[i] = b1;
  }
  b1 = r[n];
  for (i = n; i >= 1; i--) {
    b1 = ti(b1, r[i]);
    b[i] = b1;
  }
  long long s = 0;
  if (f[n - 1].x <= f[n - 1].y) s = max(s, f[n - 1].y - f[n - 1].x);
  if (b[2].x <= b[2].y) s = max(s, b[2].y - b[2].x);
  for (i = 2; i <= n - 1; i++) {
    b1 = ti(f[i - 1], b[i + 1]);
    if (b1.x <= b1.y) s = max(s, b1.y - b1.x);
  }
  cout << s;
  return 0;
}
