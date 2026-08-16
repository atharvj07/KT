#include <bits/stdc++.h>
using namespace std;
int rd() {
  int rx = 0, fx = 1;
  char c = getchar();
  while (c < 48 || c > 57) {
    if (c == '-') fx = -1;
    c = getchar();
  }
  while (c >= 48 && c <= 57) {
    rx = rx * 10 + c - 48;
    c = getchar();
  }
  return rx * fx;
}
const int N = 4e5 + 50;
int n, Q, top, now, bl, br;
int a[N], pl[30], pr[30];
struct Node {
  int l, r, w;
};
Node operator+(Node a, Node b) { return (Node){a.l, b.r, a.w + b.w}; }
void RV(Node &a) { a = (Node){a.l, a.r, -a.w}; }
Node max(Node a, Node b) {
  if (a.w > b.w)
    return a;
  else
    return b;
}
Node min(Node a, Node b) {
  if (a.w < b.w)
    return a;
  else
    return b;
}
struct Segment_tree {
  int tag[N];
  Node mxl[N], mxr[N], mxf[N], mnl[N], mnr[N], mnf[N], bsu[N];
  void mup(int rt) {
    bsu[rt] = bsu[(rt << 1)] + bsu[((rt << 1) | 1)];
    mxl[rt] = max(mxl[(rt << 1)], bsu[(rt << 1)] + mxl[((rt << 1) | 1)]);
    mxr[rt] = max(mxr[((rt << 1) | 1)], mxr[(rt << 1)] + bsu[((rt << 1) | 1)]);
    mxf[rt] = max(max(mxf[(rt << 1)], mxf[((rt << 1) | 1)]),
                  mxr[(rt << 1)] + mxl[((rt << 1) | 1)]);
    mnl[rt] = min(mnl[(rt << 1)], bsu[(rt << 1)] + mnl[((rt << 1) | 1)]);
    mnr[rt] = min(mnr[((rt << 1) | 1)], mnr[(rt << 1)] + bsu[((rt << 1) | 1)]);
    mnf[rt] = min(min(mnf[(rt << 1)], mnf[((rt << 1) | 1)]),
                  mnr[(rt << 1)] + mnl[((rt << 1) | 1)]);
  }
  void cover(int rt) {
    tag[rt] ^= 1;
    RV(bsu[rt]);
    swap(mxl[rt], mnl[rt]);
    RV(mxl[rt]);
    RV(mnl[rt]);
    swap(mxr[rt], mnr[rt]);
    RV(mxr[rt]);
    RV(mnr[rt]);
    swap(mxf[rt], mnf[rt]);
    RV(mxf[rt]);
    RV(mnf[rt]);
  }
  void mdown(int rt) {
    if (!tag[rt]) return;
    tag[rt] = 0;
    cover((rt << 1));
    cover(((rt << 1) | 1));
  }
  void build(int rt, int l, int r) {
    if (l == r) {
      bsu[rt] = (Node){l, l, a[l]};
      mxl[rt] = mxf[rt] = (a[l] > 0 ? (Node){l, l, a[l]} : (Node){l, l - 1, 0});
      mxr[rt] = (a[l] > 0 ? (Node){l, l, a[l]} : (Node){l + 1, l, 0});
      mnl[rt] = mnf[rt] = (a[l] < 0 ? (Node){l, l, a[l]} : (Node){l, l - 1, 0});
      mnr[rt] = (a[l] < 0 ? (Node){l, l, a[l]} : (Node){l + 1, l, 0});
      return;
    }
    int mid = (l + r) >> 1;
    build((rt << 1), l, mid);
    build(((rt << 1) | 1), mid + 1, r);
    mup(rt);
  }
  void chg(int rt, int l, int r, int x, int w) {
    if (l == r) {
      a[l] = w;
      bsu[rt] = (Node){l, l, a[l]};
      mxl[rt] = mxf[rt] = (a[l] > 0 ? (Node){l, l, a[l]} : (Node){l, l - 1, 0});
      mxr[rt] = (a[l] > 0 ? (Node){l, l, a[l]} : (Node){l + 1, l, 0});
      mnl[rt] = mnf[rt] = (a[l] < 0 ? (Node){l, l, a[l]} : (Node){l, l - 1, 0});
      mnr[rt] = (a[l] < 0 ? (Node){l, l, a[l]} : (Node){l + 1, l, 0});
      return;
    }
    int mid = (l + r) >> 1;
    mdown(rt);
    if (mid >= x)
      chg((rt << 1), l, mid, x, w);
    else
      chg(((rt << 1) | 1), mid + 1, r, x, w);
    mup(rt);
  }
  void qry(int rt, int l, int r, int x, int y, int &spo, int &svl) {
    if (l >= x && r <= y) {
      if (svl + mxl[rt].w > now)
        now = svl + mxl[rt].w, bl = spo, br = mxl[rt].r;
      if (mxf[rt].w > now) now = mxf[rt].w, bl = mxf[rt].l, br = mxf[rt].r;
      svl += bsu[rt].w;
      if (mxr[rt].w > svl) svl = mxr[rt].w, spo = mxr[rt].l;
      return;
    }
    int mid = (l + r) >> 1;
    mdown(rt);
    if (mid >= x) qry((rt << 1), l, mid, x, y, spo, svl);
    if (mid < y) qry(((rt << 1) | 1), mid + 1, r, x, y, spo, svl);
    mup(rt);
  }
  void modify(int rt, int l, int r, int x, int y) {
    if (l >= x && r <= y) {
      cover(rt);
      return;
    }
    int mid = (l + r) >> 1;
    mdown(rt);
    if (mid >= x) modify((rt << 1), l, mid, x, y);
    if (mid < y) modify(((rt << 1) | 1), mid + 1, r, x, y);
    mup(rt);
  }
} sgt;
int main() {
  int i, op, l, r, k, x, vl, suf, pos, ans;
  n = rd();
  for (i = 1; i <= n; i++) a[i] = rd();
  sgt.build(1, 1, n);
  Q = rd();
  while (Q--) {
    op = rd();
    if (op == 0) {
      x = rd();
      vl = rd();
      sgt.chg(1, 1, n, x, vl);
    } else {
      l = rd();
      r = rd();
      k = rd();
      ans = 0;
      top = 0;
      for (i = 1; i <= k; i++) {
        suf = now = 0;
        pos = l;
        sgt.qry(1, 1, n, l, r, pos, suf);
        if (now == 0) break;
        sgt.modify(1, 1, n, bl, br);
        top++;
        pl[top] = bl;
        pr[top] = br;
        ans += now;
      }
      while (top > 0) {
        sgt.modify(1, 1, n, pl[top], pr[top]);
        top--;
      }
      printf("%d\n", ans);
    }
  }
  return 0;
}
