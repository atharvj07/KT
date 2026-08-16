#include <bits/stdc++.h>
using namespace std;
char s1[3000000 + 5], s[3000000 + 5];
int c[3000000 + 5], T, fa[3000000 + 5];
int l[5000 + 5], r[5000 + 5], pre[3000000 + 5];
int lowbit(int x) { return x & (-x); }
void modify(int x, int y) {
  for (int i = x; i <= T; i += lowbit(i)) c[i] += y;
}
int query(int x) {
  int sum = 0;
  for (int i = x; i > 0; i -= lowbit(i)) sum += c[i];
  return sum;
}
int get(int x) {
  if (fa[x] == x) return x;
  return fa[x] = get(fa[x]);
}
void merge(int x, int y) { fa[get(x)] = get(y); }
int top[2], q[2][3000000 + 5];
void dfs(int n) {
  if (n == 0) {
    int now = get(1), t = 0;
    while (now <= T) {
      s1[now] = s[t++];
      now++;
      now = get(now);
    }
    return;
  }
  int ll = 0, rr = 0, a, b, num = 0;
  top[0] = top[1] = 0;
  for (int i = 21; i >= 0; i--)
    if (ll + (1 << i) <= T && num + c[(1 << i) + ll] < l[n])
      num += c[(1 << i) + ll], ll += (1 << i);
  ll++;
  rr = get(ll + 1);
  a = 0;
  num = 0;
  for (int i = 21; i >= 0; i--)
    if (a + (1 << i) <= T && num + c[(1 << i) + a] <= r[n])
      num += c[(1 << i) + a], a += (1 << i);
  a++;
  if (a > T) {
    dfs(n - 1);
    return;
  }
  b = a;
  while (b <= T && top[1] < (r[n] - l[n] + 1)) {
    q[1][++top[1]] = b;
    b = get(b + 1);
  }
  for (int i = 1; i <= top[1]; i++)
    merge(q[1][i], q[1][i] + 1), modify(q[1][i], -1);
  int now = 1;
  for (int i = 2; i <= r[n] - l[n] + 1; i += 2)
    if (now <= top[1]) {
      pre[q[1][now++]] = rr;
      rr = get(rr + 1);
      rr = get(rr + 1);
    } else
      break;
  for (int i = 1; i <= r[n] - l[n] + 1; i += 2)
    if (now <= top[1]) {
      pre[q[1][now++]] = ll;
      ll = get(ll + 1);
      ll = get(ll + 1);
    } else
      break;
  dfs(n - 1);
}
int main() {
  scanf("%s", s);
  int n, k, i;
  scanf("%d", &k);
  T = k;
  for (i = 1; i <= k; i++) s1[i] = '#';
  for (i = 1; i <= k; i++) fa[i] = i, c[i] = lowbit(i);
  fa[k + 1] = k + 1;
  scanf("%d", &n);
  for (i = 1; i <= n; i++) scanf("%d%d", &l[i], &r[i]);
  dfs(n);
  for (i = 1; i <= k; i++)
    if (pre[i] != 0) s1[i] = s1[pre[i]];
  puts(s1 + 1);
}
