#include <bits/stdc++.h>
using namespace std;
long long d[3030][110][2];
int main() {
  int l, n, a[1000], b[1000], i, j, k, len, wid;
  long long ans;
  cin >> n >> l;
  for (i = 0; i < n; i++) cin >> a[i] >> b[i];
  for (i = 0; i < n; i++) {
    d[a[i]][i][0]++;
    d[b[i]][i][1]++;
  }
  for (i = 0; i <= l; i++) {
    for (j = 0; j < n; j++) {
      wid = a[j];
      len = b[j];
      if (i >= wid)
        for (k = 0; k < n; k++) {
          if (k == j) continue;
          if (a[k] == len)
            d[i][j][0] += d[i - wid][k][0], d[i][j][0] %= 1000000007;
          if (b[k] == len && a[k] != b[k])
            d[i][j][0] += d[i - wid][k][1], d[i][j][0] %= 1000000007;
        }
      swap(len, wid);
      if (i >= wid && len != wid)
        for (k = 0; k < n; k++) {
          if (k == j) continue;
          if (a[k] == len)
            d[i][j][1] += d[i - wid][k][0], d[i][j][1] %= 1000000007;
          if (b[k] == len && a[k] != b[k])
            d[i][j][1] += d[i - wid][k][1], d[i][j][1] %= 1000000007;
        }
    }
  }
  ans = 0;
  for (j = 0; j < n; j++)
    if (a[j] != b[j])
      ans += d[l][j][0] + d[l][j][1];
    else
      ans += d[l][j][0];
  cout << ans % 1000000007;
  return 0;
}
