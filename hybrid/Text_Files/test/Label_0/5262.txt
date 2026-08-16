#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long ans = 0, w = 1;
  char c = getchar();
  while (!isdigit(c) && c != '-') c = getchar();
  if (c == '-') w = -1, c = getchar();
  while (isdigit(c)) ans = (ans << 1) + (ans << 3) + c - '0', c = getchar();
  return ans * w;
}
long long sum1[300010 << 2], sum2[300010 << 2];
int a[300010], w[300010];
int n, q;
long long mod(long long a) {
  a %= 1000000007;
  if (a < 0) a += 1000000007;
  return a;
}
long long add(long long a, long long b) { return mod(a + b); }
long long mul(long long a, long long b) { return mod(a * b); }
void pushup1(int t) { sum1[t] = sum1[(t << 1)] + sum1[(t << 1 | 1)]; }
void pushup2(int t) { sum2[t] = add(sum2[(t << 1)], sum2[(t << 1 | 1)]); }
void modify1(int t, int l, int r, int pos, long long vl) {
  if (l == r) {
    sum1[t] = vl;
    return;
  }
  if (pos <= ((l + r) >> 1))
    modify1((t << 1), l, ((l + r) >> 1), pos, vl);
  else
    modify1((t << 1 | 1), ((l + r) >> 1) + 1, r, pos, vl);
  pushup1(t);
}
void modify2(int t, int l, int r, int pos, long long vl) {
  if (l == r) {
    sum2[t] = vl;
    return;
  }
  if (pos <= ((l + r) >> 1))
    modify2((t << 1), l, ((l + r) >> 1), pos, vl);
  else
    modify2((t << 1 | 1), ((l + r) >> 1) + 1, r, pos, vl);
  pushup2(t);
}
long long qry1(int o, int l, int r, int ql, int qr) {
  if (ql <= l && r <= qr) return sum1[o];
  long long ans = 0;
  if (((l + r) >> 1) >= ql) ans += qry1((o << 1), l, ((l + r) >> 1), ql, qr);
  if (((l + r) >> 1) < qr)
    ans += qry1(((o << 1) | 1), ((l + r) >> 1) + 1, r, ql, qr);
  return ans;
}
long long qry2(int o, int l, int r, int ql, int qr) {
  if (ql <= l && r <= qr) return sum2[o];
  long long ans = 0;
  if (((l + r) >> 1) >= ql) ans = qry2((o << 1), l, ((l + r) >> 1), ql, qr);
  if (((l + r) >> 1) < qr)
    (ans += qry2(((o << 1) | 1), ((l + r) >> 1) + 1, r, ql, qr)) %= 1000000007;
  return ans;
}
int query1_pos(int t, int l, int r, int L, int R, long long vl) {
  if (l == r) return l;
  if (R <= ((l + r) >> 1))
    return query1_pos((t << 1), l, ((l + r) >> 1), L, R, vl);
  if (L > ((l + r) >> 1))
    return query1_pos((t << 1 | 1), ((l + r) >> 1) + 1, r, L, R, vl);
  long long suml = qry1((t << 1), l, ((l + r) >> 1), L, ((l + r) >> 1));
  if (suml >= vl)
    return query1_pos((t << 1), l, ((l + r) >> 1), L, ((l + r) >> 1), vl);
  else
    return query1_pos((t << 1 | 1), ((l + r) >> 1) + 1, r, ((l + r) >> 1) + 1,
                      R, vl - suml);
}
int main() {
  scanf("%d%d", &n, &q);
  for (int i = 1; i <= n; ++i) scanf("%d", a + i), a[i] -= i;
  for (int i = 1; i <= n; ++i) scanf("%d", w + i);
  for (int i = 1; i <= n; ++i) {
    modify1(1, 1, n, i, w[i]);
    modify2(1, 1, n, i, mul(a[i], w[i]));
  }
  while (q--) {
    int first = read(), second = read();
    if (first < 0) {
      first = -first;
      w[first] = second;
      modify1(1, 1, n, first, w[first]);
      modify2(1, 1, n, first, mul(a[first], w[first]));
    } else {
      long long sum = qry1(1, 1, n, first, second);
      int l = first, r = second, pos = -1;
      while (l <= r) {
        if (2 * qry1(1, 1, n, first, ((l + r) >> 1)) >= sum)
          pos = ((l + r) >> 1), r = ((l + r) >> 1) - 1;
        else
          l = ((l + r) >> 1) + 1;
      }
      long long ans = 0;
      ans = add(ans, mul(a[pos], add(qry1(1, 1, n, first, pos),
                                     -qry1(1, 1, n, pos, second))));
      ans =
          add(ans, add(-qry2(1, 1, n, first, pos), qry2(1, 1, n, pos, second)));
      printf("%lld\n", ans);
    }
  }
  return 0;
}
