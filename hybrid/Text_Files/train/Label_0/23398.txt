#include <bits/stdc++.h>
using namespace std;
inline long long rd() {
  long long x = 0, f = 1;
  char c = getchar();
  for (; !isdigit(c); c = getchar())
    if (c == '-') f = -1;
  for (; isdigit(c); c = getchar()) x = (x << 1) + (x << 3) + (c ^ 48);
  return x * f;
}
void write(long long x) {
  if (x < 0) x = -x, putchar('-');
  if (x >= 10) write(x / 10);
  putchar(x % 10 + '0');
}
void writeln(long long x) {
  write(x);
  puts("");
}
const int mod = 1e9 + 7;
const int maxn = 1e5 + 233;
const int maxm = maxn * 20;
int y[maxn], rt[maxm], sum[maxm], s[maxm], ab[maxm], de[maxm], abc[maxm],
    cde[maxm], lc[maxm], rc[maxm];
int n, c[maxn];
void add(int x) {
  for (; x <= n; x += ((x) & (-x))) c[x]++;
}
int ask(int x) {
  int ans = 0;
  for (; x; x -= ((x) & (-x))) ans += c[x];
  return ans;
}
void update(int o) {
  s[o] = (s[lc[o]] + s[rc[o]]) % mod;
  sum[o] = (sum[lc[o]] + sum[rc[o]] + 1ll * ab[lc[o]] * cde[rc[o]] +
            1ll * abc[lc[o]] * de[rc[o]]) %
           mod;
  ab[o] = (ab[lc[o]] + ab[rc[o]]) % mod;
  de[o] = (de[lc[o]] + de[rc[o]]) % mod;
  abc[o] = (abc[lc[o]] + abc[rc[o]] + 1ll * ab[lc[o]] * s[rc[o]]) % mod;
  cde[o] = (cde[lc[o]] + cde[rc[o]] + 1ll * s[lc[o]] * de[rc[o]]) % mod;
}
int tot = 0, L[maxn], R[maxn], a[maxn];
void modify(int &o, int l, int r, int x, int v) {
  if (!o) o = ++tot;
  if (l == r) {
    sum[o] = abc[o] = cde[o] = 0;
    if (v)
      s[o] = 1, ab[o] = L[x], de[o] = R[x];
    else
      s[o] = 0, ab[o] = 0, de[o] = 0;
  } else {
    int mid = (l + r) >> 1;
    if (x <= mid)
      modify(lc[o], l, mid, x, v);
    else
      modify(rc[o], mid + 1, r, x, v);
    update(o);
  }
}
int main() {
  n = rd();
  for (register int i = (1); i <= int(n); ++i) a[i] = rd(), y[++*y] = a[i];
  sort(y + 1, y + 1 + *y), *y = unique(y + 1, y + 1 + *y) - y - 1;
  for (register int i = (1); i <= int(n); ++i)
    a[i] = lower_bound(y + 1, y + 1 + *y, a[i]) - y;
  memset(c, 0, sizeof(c));
  for (register int i = (1); i <= int(n); ++i) L[i] = ask(a[i]), add(a[i]);
  memset(c, 0, sizeof(c));
  for (register int i = (n); i >= int(1); --i) R[i] = ask(a[i]), add(a[i]);
  tot = 0;
  for (register int i = (1); i <= int(n); ++i) modify(rt[a[i]], 1, n, i, 1);
  long long ans = 0;
  for (register int i = (1); i <= int(n); ++i) ans += sum[rt[i]];
  int m = rd();
  while (m--) {
    int op = rd(), i = rd();
    ans = (ans - sum[rt[a[i]]] + mod) % mod;
    if (op == 1) {
      modify(rt[a[i]], 1, n, i, 0);
    } else {
      modify(rt[a[i]], 1, n, i, 1);
    }
    ans = (ans + sum[rt[a[i]]]) % mod;
    writeln(ans);
  }
  return 0;
}
