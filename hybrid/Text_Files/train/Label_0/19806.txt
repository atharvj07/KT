#include <bits/stdc++.h>
using namespace std;
int aa, bb;
int check(int x, int y, int z, int w) {
  if (x + z <= aa && max(y, w) <= bb) return x * y + z * w;
  if (max(x, z) <= aa && y + w <= bb) return x * y + z * w;
  if (x + z <= aa && y + w <= bb)
    return x * y + z * w;
  else
    return -1;
}
int main() {
  int n;
  cin >> n >> aa >> bb;
  int a[n][2];
  for (int i = 0; i < n; i++) {
    cin >> a[i][0] >> a[i][1];
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      ans = max(ans, check(a[i][0], a[i][1], a[j][0], a[j][1]));
      ans = max(ans, check(a[i][0], a[i][1], a[j][1], a[j][0]));
      ans = max(ans, check(a[i][1], a[i][0], a[j][0], a[j][1]));
      ans = max(ans, check(a[i][1], a[i][0], a[j][1], a[j][0]));
    }
  }
  cout << max(0, ans) << endl;
  return 0;
}
