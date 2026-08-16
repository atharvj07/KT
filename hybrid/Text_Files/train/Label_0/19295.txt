#include <bits/stdc++.h>
#pragma GCC target("avx")
#pragma GCC optimize(3)
#pragma GCC optimize("Ofast")
#pragma GCC optimize("inline")
#pragma GCC optimize("-fgcse")
#pragma GCC optimize("-fgcse-lm")
#pragma GCC optimize("-fipa-sra")
#pragma GCC optimize("-ftree-pre")
#pragma GCC optimize("-ftree-vrp")
#pragma GCC optimize("-fpeephole2")
#pragma GCC optimize("-ffast-math")
#pragma GCC optimize("-fsched-spec")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("-falign-jumps")
#pragma GCC optimize("-falign-loops")
#pragma GCC optimize("-falign-labels")
#pragma GCC optimize("-fdevirtualize")
#pragma GCC optimize("-fcaller-saves")
#pragma GCC optimize("-fcrossjumping")
#pragma GCC optimize("-fthread-jumps")
#pragma GCC optimize("-funroll-loops")
#pragma GCC optimize("-fwhole-program")
#pragma GCC optimize("-freorder-blocks")
#pragma GCC optimize("-fschedule-insns")
#pragma GCC optimize("inline-functions")
#pragma GCC optimize("-ftree-tail-merge")
#pragma GCC optimize("-fschedule-insns2")
#pragma GCC optimize("-fstrict-aliasing")
#pragma GCC optimize("-fstrict-overflow")
#pragma GCC optimize("-falign-functions")
#pragma GCC optimize("-fcse-skip-blocks")
#pragma GCC optimize("-fcse-follow-jumps")
#pragma GCC optimize("-fsched-interblock")
#pragma GCC optimize("-fpartial-inlining")
#pragma GCC optimize("no-stack-protector")
#pragma GCC optimize("-freorder-functions")
#pragma GCC optimize("-findirect-inlining")
#pragma GCC optimize("-fhoist-adjacent-loads")
#pragma GCC optimize("-frerun-cse-after-loop")
#pragma GCC optimize("inline-small-functions")
#pragma GCC optimize("-finline-small-functions")
#pragma GCC optimize("-ftree-switch-conversion")
#pragma GCC optimize("-foptimize-sibling-calls")
#pragma GCC optimize("-fexpensive-optimizations")
#pragma GCC optimize("-funsafe-loop-optimizations")
#pragma GCC optimize("inline-functions-called-once")
#pragma GCC optimize("-fdelete-null-pointer-checks")
#pragma GCC optimize(3)
using namespace std;
struct ios {
  inline char gc() {
    static const long long IN_LEN = 1 << 18 | 1;
    static char buf[IN_LEN], *s, *t;
    return (s == t) && (t = (s = buf) + fread(buf, 1, IN_LEN, stdin)),
           s == t ? -1 : *s++;
  }
  template <typename _Tp>
  inline ios& operator>>(_Tp& x) {
    static char ch, sgn;
    ch = gc(), sgn = 0;
    for (; !isdigit(ch); ch = gc()) {
      if (ch == -1) return *this;
      sgn |= ch == '-';
    }
    for (x = 0; isdigit(ch); ch = gc()) x = x * 10 + (ch ^ '0');
    sgn && (x = -x);
    return *this;
  }
} io;
const long long maxn = 100005;
const long long mod = 1e9 + 7;
long long n, val[maxn], mi[maxn], mx[maxn], sta[maxn], stb[maxn], topa, topb,
    last[maxn], nxt[maxn], tong[maxn], s[maxn], top, ans, sigr[maxn << 2], gg,
    sigl[maxn << 2], sig[maxn << 2];
struct node {
  long long x, lazy;
};
node lg[maxn << 2], rg[maxn << 2];
long long tree1[maxn << 2], tree2[maxn << 2];
void change(long long l, long long r, long long rt, long long x,
            long long flag) {
  if (!flag) {
    lg[rt].x = lg[rt].lazy = x;
  } else {
    rg[rt].x = rg[rt].lazy = x;
  }
  if (rg[rt].x < l) {
    tree1[rt] = tree2[rt] = sigr[rt] = sigl[rt] = sig[rt] = 0;
    return;
  }
  long long a = min(r, rg[rt].x);
  long long y = a - l + 1;
  if (l == r) {
    sigl[rt] = lg[rt].x;
    sigr[rt] = rg[rt].x;
    sig[rt] = rg[rt].x - l;
    if (sig[rt] < 0) sig[rt] += mod;
    tree1[rt] = (1LL * lg[rt].x * rg[rt].x % mod);
    tree2[rt] = (1LL * l * lg[rt].x % mod);
    return;
  }
  if (!flag) {
    sigl[rt] = 1LL * lg[rt].x * y % mod;
    tree1[rt] = 1LL * sigr[rt] * lg[rt].x % mod;
    tree2[rt] = 1LL * (1LL * (l + a) * y / 2) % mod * lg[rt].x;
  } else {
    sig[rt] =
        (1LL * y * rg[rt].x % mod - (1LL * (a + l) * y / 2) % mod + mod) % mod;
    sigr[rt] = 1LL * y * rg[rt].x % mod;
    tree1[rt] = 1LL * sigl[rt] * rg[rt].x % mod;
  }
}
void pushdown(long long l, long long r, long long rt) {
  long long mid = (l + r) >> 1;
  if (lg[rt].lazy) {
    change(l, mid, rt << 1, lg[rt].lazy, 0);
    change(mid + 1, r, rt << 1 | 1, lg[rt].lazy, 0);
    lg[rt].lazy = 0;
  }
  if (rg[rt].lazy) {
    change(l, mid, rt << 1, rg[rt].lazy, 1);
    change(mid + 1, r, rt << 1 | 1, rg[rt].lazy, 1);
    rg[rt].lazy = 0;
  }
}
void pushup(long long rt) {
  tree1[rt] = tree1[rt << 1] + tree1[rt << 1 | 1];
  if (tree1[rt] >= mod) tree1[rt] -= mod;
  tree2[rt] = tree2[rt << 1] + tree2[rt << 1 | 1];
  if (tree2[rt] >= mod) tree2[rt] -= mod;
  sigr[rt] = sigr[rt << 1] + sigr[rt << 1 | 1];
  if (sigr[rt] >= mod) sigr[rt] -= mod;
  sigl[rt] = sigl[rt << 1] + sigl[rt << 1 | 1];
  if (sigl[rt] >= mod) sigl[rt] -= mod;
  sig[rt] = sig[rt << 1] + sig[rt << 1 | 1];
  if (sig[rt] >= mod) sig[rt] -= mod;
}
void update(long long L, long long R, long long x, long long flag, long long l,
            long long r, long long rt) {
  if (L <= l && R >= r) {
    change(l, r, rt, x, flag);
    return;
  }
  long long mid = (l + r) >> 1;
  pushdown(l, r, rt);
  if (L <= mid) update(L, R, x, flag, l, mid, rt << 1);
  if (R > mid) update(L, R, x, flag, mid + 1, r, rt << 1 | 1);
  pushup(rt);
}
long long query(long long L, long long R, long long l, long long r,
                long long rt) {
  if (L > R) return 0;
  if (L <= l && R >= r) {
    return ((-tree1[rt] + tree2[rt] + 1LL * sig[rt] * gg % mod) % mod + mod) %
           mod;
  }
  long long mid = (l + r) >> 1;
  pushdown(l, r, rt);
  long long ans = 0;
  if (L <= mid) {
    ans += query(L, R, l, mid, rt << 1);
    if (ans >= mod) ans -= mod;
  }
  if (R > mid) {
    ans += query(L, R, mid + 1, r, rt << 1 | 1);
    if (ans >= mod) ans -= mod;
  }
  return ans;
}
signed main() {
  scanf("%lld", &n);
  ans = 0;
  for (long long i = 1; i <= n; ++i) scanf("%lld", &val[i]), s[++top] = val[i];
  for (long long i = 1; i <= (n << 2); ++i) rg[i].x = 1061109567;
  sort(s + 1, s + top + 1);
  top = unique(s + 1, s + top + 1) - s - 1;
  for (long long i = 1; i <= n; ++i)
    val[i] = lower_bound(s + 1, s + top + 1, val[i]) - s;
  for (long long i = 1; i <= n; ++i) {
    last[i] = tong[val[i]] + 1;
    tong[val[i]] = i;
  }
  for (long long i = 1; i <= n; ++i) tong[i] = n + 1;
  for (long long i = n; i >= 1; --i) {
    nxt[i] = tong[val[i]] - 1;
    tong[val[i]] = i;
  }
  topa = topb = 0;
  sta[0] = n + 1;
  stb[0] = n + 1;
  mi[0] = 1061109567;
  for (long long i = n; i >= 1; --i) {
    gg = i;
    while (topa && mi[topa] <= last[i]) topa--;
    while (topb && mx[topb] >= nxt[i]) topb--;
    sta[++topa] = i;
    mi[topa] = last[i];
    stb[++topb] = i;
    mx[topb] = nxt[i];
    update(i, sta[topa - 1] - 1, mi[topa], 0, 1, n, 1);
    update(i, stb[topb - 1] - 1, mx[topb], 1, 1, n, 1);
    long long l = 0, r = topa, res = -1;
    while (l <= r) {
      long long mid = (l + r) >> 1;
      if (mi[mid] > i) {
        res = sta[mid];
        l = mid + 1;
      } else
        r = mid - 1;
    }
    ans += query(i, res - 1, 1, n, 1);
    if (ans >= mod) ans -= mod;
  }
  cout << ans << endl;
}
