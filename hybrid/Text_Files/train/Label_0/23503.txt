#include <bits/stdc++.h>
using namespace std;
const int maxn = 5e5 + 5;
int w[15];
int a[maxn];
int n;
int change(char *s) {
  int res = 0, tmp = 1;
  for (int i = n - 1; ~i; i--) {
    if (s[i] == '1') res += tmp;
    tmp *= 2;
  }
  return res;
}
int sum[maxn / 5][105];
int cnt[maxn / 5];
int get2(int x, int t) {
  if (x & (1 << t))
    return 1;
  else
    return 0;
}
int main() {
  int m, q;
  char s[15];
  cin >> n >> m >> q;
  for (int i = 0; i < n; i++) cin >> w[i];
  for (int i = 0; i < m; i++) {
    scanf("%s", s);
    a[i] = change(s);
    cnt[a[i]]++;
  }
  sort(a, a + m);
  int siz = unique(a, a + m) - a;
  int mx = (1 << n) - 1;
  int tmp;
  for (int i = 0; i <= mx; i++) {
    for (int j = 0; j < siz; j++) {
      tmp = 0;
      for (int t = 0; t < n; t++) {
        if (get2(i, t) ^ get2(a[j], t) == 0) {
          tmp += w[n - t - 1];
        }
      }
      if (tmp <= 100) sum[i][tmp] += cnt[a[j]];
    }
    for (int j = 1; j <= 100; j++) sum[i][j] += sum[i][j - 1];
  }
  int k, id;
  while (q--) {
    scanf("%s%d", s, &k);
    id = change(s);
    printf("%d\n", sum[id][k]);
  }
  return 0;
}
