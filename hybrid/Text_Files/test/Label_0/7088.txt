#include <bits/stdc++.h>
using namespace std;
const int maxn = 60;
int n;
long long ai[maxn];
long long sum[maxn];
int l1[maxn], r1[maxn];
int l2[maxn], r2[maxn];
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%lld", &ai[i]);
  for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] + ai[i];
  int res = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j++) {
      long long q = sum[j] - sum[i - 1];
      int s = 1;
      int cnt = 0;
      for (int k = 1; k <= n; k++) {
        for (int l = s; l <= k; l++) {
          if (sum[k] - sum[l - 1] == q) {
            cnt++;
            l1[cnt] = l;
            r1[cnt] = k;
            s = k + 1;
            break;
          }
        }
      }
      if (cnt > res) {
        res = cnt;
        for (int k = 1; k <= cnt; k++) l2[k] = l1[k], r2[k] = r1[k];
      }
    }
  }
  printf("%d\n", res);
  for (int i = 1; i <= res; i++) printf("%d %d\n", l2[i], r2[i]);
  return 0;
}
