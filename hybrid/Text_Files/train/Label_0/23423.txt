#include <bits/stdc++.h>
using namespace std;
const int BUFSIZE = 20 << 21;
char Buf[BUFSIZE + 1], *buf = Buf;
template <class T>
void scan(T& a) {
  int sgn = 1;
  for (a = 0; *buf < '0' || *buf > '9'; buf++)
    if (*buf == '-') sgn = -1;
  while (*buf >= '0' && *buf <= '9') {
    a = a * 10 + (*buf - '0');
    buf++;
  }
  a *= sgn;
}
const int N = (int)1e6 + 10;
vector<pair<int, int>> g[N];
vector<int> v[N];
int mx[N], l[N], r[N], p[N], a[N], n, q;
long long s[N], c[N], sum[N], ans[N];
void modify(long long c[], int x, int y) {
  for (; x <= n; x += x & (-x)) c[x] += y;
}
long long get(long long c[], int x) {
  long long s = 0;
  for (; x; x -= x & (-x)) s += c[x];
  return s;
}
void modify_mx(int x, int y) {
  for (; x <= n; x += x & (-x)) mx[x] = max(mx[x], y);
}
int get_mx(int x) {
  int s = 0;
  for (; x; x -= x & (-x)) s = max(s, mx[x]);
  return s;
}
void work() {
  memset(mx, 0, sizeof(mx));
  for (int i = 1; i <= n; i++) v[i - 1].clear();
  for (int i = 1; i <= n; i++) {
    int pre = get_mx(n - p[i] + 1);
    a[i] = i - pre - 1;
    v[pre].push_back(i);
    sum[i] = sum[i - 1] + a[i];
    modify_mx(n - p[i] + 1, i);
  }
  for (int i = 1; i <= n; i++) g[i].clear();
  for (int i = 1; i <= q; i++) {
    ans[i] += sum[r[i]] - sum[l[i] - 1];
    g[l[i]].push_back(make_pair(r[i], i));
  }
  memset(s, 0, sizeof(s));
  memset(c, 0, sizeof(c));
  for (int i = 1; i <= n; i++) {
    for (const auto& j : v[i - 1]) modify(s, j, j - a[j]), modify(c, j, 1);
    for (const auto& j : g[i])
      ans[j.second] += (get(s, j.first) - get(s, i - 1)) -
                       i * (get(c, j.first) - get(c, i - 1));
  }
}
int main() {
  fread(Buf, 1, BUFSIZE, stdin);
  scan(n);
  scan(q);
  for (int i = 1; i <= n; i++) scan(p[i]);
  for (int i = 1; i <= q; i++) scan(l[i]);
  for (int i = 1; i <= q; i++) scan(r[i]);
  work();
  reverse(p + 1, p + n + 1);
  for (int i = 1; i <= q; i++)
    l[i] = n - l[i] + 1, r[i] = n - r[i] + 1, swap(l[i], r[i]);
  work();
  for (int i = 1; i <= q; i++)
    printf("%lld%c", ans[i] + r[i] - l[i] + 1, " \n"[i == q]);
  return 0;
}
