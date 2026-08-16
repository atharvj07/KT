#include <bits/stdc++.h>
using namespace std;
const int iinf = 1e9 + 7;
const long long linf = 1ll << 60;
const double dinf = 1e60;
template <typename T>
inline void scf(T &x) {
  bool f = 0;
  x = 0;
  char c = getchar();
  while ((c < '0' || c > '9') && c != '-') c = getchar();
  if (c == '-') {
    f = 1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    x = x * 10 + c - '0';
    c = getchar();
  }
  if (f) x = -x;
  return;
}
template <typename T1, typename T2>
void scf(T1 &x, T2 &y) {
  scf(x);
  return scf(y);
}
template <typename T1, typename T2, typename T3>
void scf(T1 &x, T2 &y, T3 &z) {
  scf(x);
  scf(y);
  return scf(z);
}
template <typename T1, typename T2, typename T3, typename T4>
void scf(T1 &x, T2 &y, T3 &z, T4 &w) {
  scf(x);
  scf(y);
  scf(z);
  return scf(w);
}
inline char mygetchar() {
  char c = getchar();
  while (c == ' ' || c == '\n') c = getchar();
  return c;
}
template <typename T>
void chkmax(T &x, const T &y) {
  if (y > x) x = y;
  return;
}
template <typename T>
void chkmin(T &x, const T &y) {
  if (y < x) x = y;
  return;
}
void TZL();
void RANK1();
int main() {
  TZL();
  RANK1();
  return 0;
}
const int N = 1e5 + 100;
const int mod = 1e9 + 7;
struct node {
  int f[3][3];
  node() { memset((f), (0), sizeof((f))); }
  node(int cntl, int cntr) {
    memset((f), (0), sizeof((f)));
    f[0][0] = cntl;
    f[2][2] = cntr;
    f[1][1] = 1;
    return;
  }
  node operator+(const node &a) const {
    node ret;
    memcpy((ret.f), (f), sizeof((f)));
    for (int l = 0, _end_ = (3); l < _end_; ++l)
      for (int r = 0, _end_ = (3); r < _end_; ++r)
        (ret.f[l][r] += a.f[l][r]) %= mod;
    for (int l = 0, _end_ = (2); l < _end_; ++l)
      for (int r = (l + 1), _end_ = (2); r <= _end_; ++r)
        for (int mid = (l), _end_ = (r - 1); mid <= _end_; ++mid) {
          ret.f[l][r] =
              (1ll * ret.f[l][r] + 1ll * f[l][mid] * a.f[mid + 1][r]) % mod;
        }
    return ret;
  }
};
struct seg {
  int n;
  struct node {
    ::node f;
    node *l, *r;
    void pull() {
      if (l && r) f = l->f + r->f;
      return;
    }
  } * root;
  void B(node *&cur, int l, int r, int *a, int *b) {
    cur = new node;
    if (l == r) {
      cur->f = ::node(a[l], b[l]);
      return;
    }
    int mid = l + r >> 1;
    B(cur->l, l, mid, a, b);
    B(cur->r, mid + 1, r, a, b);
    return cur->pull();
  }
  void M(node *&cur, int i, ::node x, int l, int r) {
    if (l == r) {
      cur->f = x;
      return;
    }
    int mid = l + r >> 1;
    if (i > mid)
      M(cur->r, i, x, mid + 1, r);
    else
      M(cur->l, i, x, l, mid);
    return cur->pull();
  }
  int Q() { return root->f.f[0][2]; }
  void B(int _n, int *cntl, int *cntr) {
    B(root, 1, n = _n, cntl, cntr);
    return;
  }
  void M(int i, ::node x) { return M(root, i, x, 1, n); }
  void out(node *cur, int l, int r, int dep = 1) {
    if (!cur) return;
    int mid = l + r >> 1;
    out(cur->l, l, mid, dep + 1);
    for (int i = 0, _end_ = (dep); i < _end_; ++i) putchar('\t');
    printf("[%d, %d]:\n", l, r);
    for (int i = 0, _end_ = (3); i < _end_; ++i) {
      for (int j = 0, _end_ = (dep + 1); j < _end_; ++j) putchar('\t');
      for (int j = 0, _end_ = (3); j < _end_; ++j)
        printf("%d ", cur->f.f[i][j]);
      putchar('\n');
    }
    for (int i = 0, _end_ = (dep); i < _end_; ++i) putchar('\t');
    puts("============");
    out(cur->r, mid + 1, r, dep + 1);
    return;
  }
  void out() { return out(root, 1, n); }
} rt[N];
int n, m, ans;
int a[N], cntl[N], cntr[N];
vector<int> apr[N];
namespace BIT {
int num[N];
int lowbit(int i) { return i & (-i); }
void M(int i) {
  for (; i <= m; i += lowbit(i)) num[i]++;
  return;
}
int Q(int i) {
  int ret = 0;
  for (; i; i ^= lowbit(i)) ret += num[i];
  return ret;
}
void B() {
  memset((num), (0), sizeof((num)));
  return;
}
}  // namespace BIT
void TZL() {
  map<int, int> M;
  M.clear();
  scf(n);
  for (int i = (1), _end_ = (n); i <= _end_; ++i) {
    scf(a[i]);
    M[a[i]];
  }
  for (auto it = M.begin(); it != M.end(); ++it) it->second = (++m);
  for (int i = (1), _end_ = (n); i <= _end_; ++i) a[i] = M[a[i]];
  for (int i = (1), _end_ = (n); i <= _end_; ++i) {
    cntl[i] = BIT::Q(a[i]);
    BIT::M(a[i]);
  }
  BIT::B();
  for (int i = (n), _end_ = (1); i >= _end_; --i) {
    cntr[i] = BIT::Q(a[i]);
    BIT::M(a[i]);
  }
  for (int i = (1), _end_ = (n); i <= _end_; ++i) apr[a[i]].push_back(i);
  static int foo[N], bar[N];
  for (int i = (1), _end_ = (m); i <= _end_; ++i) {
    int pnt = 0;
    for (int x : apr[i]) {
      ++pnt;
      foo[pnt] = cntl[x];
      bar[pnt] = cntr[x];
    }
    rt[i].B(pnt, foo, bar);
    (ans += rt[i].Q()) %= mod;
  }
  return;
}
void RANK1() {
  int q_n;
  scf(q_n);
  while (q_n--) {
    int typ, i;
    scf(typ, i);
    int x = a[i],
        j = lower_bound(apr[x].begin(), apr[x].end(), i) - apr[x].begin() + 1;
    (ans += mod - rt[x].Q()) %= mod;
    node nw;
    if (typ == 2) nw = node(cntl[i], cntr[i]);
    rt[x].M(j, nw);
    (ans += rt[x].Q()) %= mod;
    printf("%d\n", ans);
  }
  return;
}
