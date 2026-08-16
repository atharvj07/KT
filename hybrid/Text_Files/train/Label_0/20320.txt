#include <bits/stdc++.h>
using namespace std;
using namespace std;
int n, a[300001], was[300001][3];
long long d[300001][3];
long long calc(int v, int bit) {
  if (v <= 0 || v > n) return 0ll;
  if (v == 1) return -1;
  if (was[v][bit] == 2) return d[v][bit] = -1;
  if (was[v][bit] == 1) return d[v][bit];
  was[v][bit] = 2;
  if (bit) {
    if (calc(v + a[v], bit ? 0 : 1) != -1)
      d[v][bit] = calc(v + a[v], bit ? 0 : 1) + a[v];
    else
      d[v][bit] = -1;
  } else {
    if (calc(v - a[v], bit ? 0 : 1) != -1)
      d[v][bit] = calc(v - a[v], bit ? 0 : 1) + a[v];
    else
      d[v][bit] = -1;
  }
  was[v][bit] = 1;
  return d[v][bit];
}
int main() {
  scanf("%d", &n);
  for (int i = 2; i <= n; ++i) scanf("%d", &a[i]);
  for (int i = 2; i <= n; ++i) {
    if (!was[i][0]) calc(i, 0);
    if (!was[i][1]) calc(i, 1);
  }
  for (int i = 1; i < n; i++)
    if (d[i + 1][0] != -1)
      cout << d[i + 1][0] + i << '\n';
    else
      puts("-1");
  return 0;
}
