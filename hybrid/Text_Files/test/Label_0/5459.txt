#include <bits/stdc++.h>
const int MAXN = 200000;
long long ans, m;
long long a[MAXN | 1], tmp[MAXN | 1];
int n;
inline int read() {
  register int x = 0, v = 1;
  register char ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') v = -1;
    ch = getchar();
  }
  while (isdigit(ch)) {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * v;
}
void CDQ(int l, int r) {
  if (l == r) return;
  int mid = (l + r) >> 1;
  CDQ(l, mid);
  CDQ(mid + 1, r);
  int pl = l, pr = mid + 1, tot = l - 1;
  while (pl <= mid && pr <= r) {
    if (a[pl] > a[pr]) {
      tmp[++tot] = a[pl];
      ++pl;
    } else {
      tmp[++tot] = a[pr];
      ++pr;
    }
  }
  while (pl <= mid) tmp[++tot] = a[pl++];
  while (pr <= r) tmp[++tot] = a[pr++];
  pl = l;
  pr = mid + 1;
  int cnt = 0;
  while (pl <= mid && pr <= r) {
    if (a[pl] + m > a[pr]) {
      ++cnt;
      ++pl;
    } else {
      ans += cnt;
      ++pr;
    }
  }
  ans += 1LL * cnt * (r - pr + 1);
  for (int i = l; i <= r; ++i) a[i] = tmp[i];
}
int main() {
  n = read();
  scanf("%lld", &m);
  for (int i = 1; i <= n; ++i) a[i] = a[i - 1] + read();
  CDQ(0, n);
  printf("%lld\n", ans);
  return 0;
}
