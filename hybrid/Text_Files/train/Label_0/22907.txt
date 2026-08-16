#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline void read(T& t) {
  T f = 1;
  char ch = getchar();
  t = 0;
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -f;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') t = t * 10 + ch - '0', ch = getchar();
  t *= f;
}
template <typename T, typename... Args>
inline void read(T& t, Args&... args) {
  read(t);
  read(args...);
}
int n, m;
struct node {
  int l, r, s;
  node() {}
  node(int L, int R, int S) {
    l = L;
    r = R;
    s = S;
  }
  inline node operator+(node& b) {
    return node(min(l, b.l), max(r, b.r), s + b.s);
  }
  bool operator<(const node& b) const { return s < b.s; }
};
struct tree {
  int lcs, rcs;
  node lmin, rmin;
  node lmax, rmax;
  node smin, smax;
  node sigma;
  bool reve;
} v[200005];
int va[100005];
int tot;
inline void up_data(int l, int r, int p) {
  if (l == r) return;
  v[p].lmin = min(v[v[p].lcs].lmin, v[v[p].lcs].sigma + v[v[p].rcs].lmin);
  v[p].rmin = min(v[v[p].rcs].rmin, v[v[p].rcs].sigma + v[v[p].lcs].rmin);
  v[p].lmax = max(v[v[p].lcs].lmax, v[v[p].lcs].sigma + v[v[p].rcs].lmax);
  v[p].rmax = max(v[v[p].rcs].rmax, v[v[p].rcs].sigma + v[v[p].lcs].rmax);
  v[p].smin = min(v[v[p].lcs].rmin + v[v[p].rcs].lmin,
                  min(v[v[p].lcs].smin, v[v[p].rcs].smin));
  v[p].smax = max(v[v[p].lcs].rmax + v[v[p].rcs].lmax,
                  max(v[v[p].lcs].smax, v[v[p].rcs].smax));
  v[p].sigma = v[v[p].lcs].sigma + v[v[p].rcs].sigma;
}
void build(int l, int r, int& p) {
  p = ++tot;
  if (l == r) {
    v[p].lcs = v[p].rcs = 0;
    v[p].lmin = v[p].rmin = v[p].smin = node(l, r, va[l]);
    v[p].lmax = v[p].rmax = v[p].smax = node(l, r, va[l]);
    v[p].sigma = node(l, r, va[l]);
    return;
  }
  build(l, ((l + r) >> 1), v[p].lcs);
  build(((l + r) >> 1) + 1, r, v[p].rcs);
  up_data(l, r, p);
}
inline void revise(int p) {
  swap(v[p].lmin, v[p].lmax);
  swap(v[p].rmin, v[p].rmax);
  swap(v[p].smin, v[p].smax);
  v[p].lmin.s *= -1;
  v[p].lmax.s *= -1;
  v[p].rmin.s *= -1;
  v[p].rmax.s *= -1;
  v[p].smax.s *= -1;
  v[p].smin.s *= -1;
  v[p].sigma.s *= -1;
  v[p].reve ^= 1;
}
void revise(int l, int r, int p, int pos, int val) {
  if (l == r && l == pos)
    return v[p].lmin = v[p].rmin = v[p].lmax = v[p].rmax = v[p].smin =
               v[p].smax = v[p].sigma = node(l, r, val),
           void();
  if (v[p].reve) {
    v[p].reve ^= 1;
    revise(v[p].lcs);
    revise(v[p].rcs);
  }
  if (pos <= ((l + r) >> 1))
    revise(l, ((l + r) >> 1), v[p].lcs, pos, val);
  else
    revise(((l + r) >> 1) + 1, r, v[p].rcs, pos, val);
  up_data(l, r, p);
}
tree merge(tree a, tree b) {
  tree c;
  c.lmin = min(a.lmin, a.sigma + b.lmin);
  c.rmin = min(b.rmin, b.sigma + a.rmin);
  c.lmax = max(a.lmax, a.sigma + b.lmax);
  c.rmax = max(b.rmax, b.sigma + a.rmax);
  c.smin = min(a.rmin + b.lmin, min(a.smin, b.smin));
  c.smax = max(a.rmax + b.lmax, max(a.smax, b.smax));
  c.sigma = a.sigma + b.sigma;
  return c;
}
tree enquire(int l, int r, int p, int nl, int nr) {
  if (nl <= l && r <= nr) return v[p];
  if (v[p].reve) revise(v[p].lcs), revise(v[p].rcs), v[p].reve ^= 1;
  if (nr <= ((l + r) >> 1)) return enquire(l, ((l + r) >> 1), v[p].lcs, nl, nr);
  if (nl >= ((l + r) >> 1) + 1)
    return enquire(((l + r) >> 1) + 1, r, v[p].rcs, nl, nr);
  tree t = merge(enquire(l, ((l + r) >> 1), v[p].lcs, nl, nr),
                 enquire(((l + r) >> 1) + 1, r, v[p].rcs, nl, nr));
  return t;
}
void Revise(int l, int r, int p, int nl, int nr) {
  if (nl <= l && r <= nr) return revise(p), void();
  if (v[p].reve) revise(v[p].lcs), revise(v[p].rcs), v[p].reve ^= 1;
  if (nl <= ((l + r) >> 1)) Revise(l, ((l + r) >> 1), v[p].lcs, nl, nr);
  if (nr >= ((l + r) >> 1) + 1) Revise(((l + r) >> 1) + 1, r, v[p].rcs, nl, nr);
  up_data(l, r, p);
}
queue<pair<int, int> > q;
int main() {
  read(n);
  for (int i = 1; i <= n; i++) read(va[i]);
  int root;
  build(1, n, root);
  read(m);
  int opt, l, r, k;
  tree tp;
  while (m--) {
    read(opt, l, r);
    if (opt == 0)
      revise(1, n, 1, l, r);
    else {
      read(k);
      long long SUM = 0;
      while (k--) {
        tp = enquire(1, n, 1, l, r);
        if (tp.smax.s <= 0) break;
        SUM += tp.smax.s;
        Revise(1, n, 1, tp.smax.l, tp.smax.r);
        q.push(make_pair(tp.smax.l, tp.smax.r));
      }
      printf("%lld\n", SUM);
      while (q.size()) {
        Revise(1, n, 1, q.front().first, q.front().second);
        q.pop();
      }
    }
  }
  return 0;
}
