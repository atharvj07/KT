#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
struct node {
  int s, e;
  long long ans, l, r, cnt;
  node *bl, *br;
  node(int ss = -1.1e9 - 10, int ee = 1.1e9 + 10) {
    s = ss, e = ee, l = r = cnt = ans = 0, bl = br = NULL;
  }
} root;
int n, q, a[maxn];
node merge(node &le, node &ri) {
  node ret(le.s, ri.e);
  ret.bl = &le, ret.br = &ri;
  ret.ans = le.ans + ri.ans + le.r * ri.cnt + ri.l * le.cnt;
  ret.l = le.l + ri.l + ri.cnt * (le.e - le.s);
  ret.r = le.r + ri.r + le.cnt * (ri.e - ri.s);
  ret.cnt = le.cnt + ri.cnt;
  return ret;
}
void upd(long long x, long long val, node &now) {
  if (now.e == now.s + 1) {
    now.r += val, now.cnt += val;
    return;
  }
  long long mid = now.s + now.e >> 1;
  if (now.bl == NULL) now.bl = new node(now.s, mid);
  if (now.br == NULL) now.br = new node(mid, now.e);
  if (x < mid)
    upd(x, val, *now.bl);
  else
    upd(x, val, *now.br);
  now = merge(*now.bl, *now.br);
}
node get(long long l, long long r, node &now) {
  if (l <= now.s && now.e <= r) return now;
  long long mid = now.s + now.e >> 1;
  if (l < mid && now.bl == NULL) now.bl = new node(now.s, mid);
  if (r > mid && now.br == NULL) now.br = new node(mid, now.e);
  if (r <= mid) return get(l, r, *now.bl);
  if (l >= mid) return get(l, r, *now.br);
  node ret1, ret2;
  return merge(ret1 = get(l, r, *now.bl), ret2 = get(l, r, *now.br));
}
int main() {
  ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i], upd(a[i], 1, root);
  cin >> q;
  while (q--) {
    long long t, l, r;
    cin >> t >> l >> r;
    if (t == 1) l--, upd(a[l], -1, root), a[l] += r, upd(a[l], 1, root);
    if (t == 2) cout << get(l, r + 1, root).ans << "\n";
  }
}
