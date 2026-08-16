#include <bits/stdc++.h>
template <class T>
inline void readInt(T &w) {
  char c, p = 0;
  while (!isdigit(c = getchar())) p = c == '-';
  for (w = c & 15; isdigit(c = getchar()); w = w * 10 + (c & 15))
    ;
  if (p) w = -w;
}
template <class T, class... Args>
inline void readInt(T &w, Args &...args) {
  readInt(w), readInt(args...);
}
template <class T, class U>
inline bool smin(T &x, const U &y) {
  return y < x ? x = y, 1 : 0;
}
template <class T, class U>
inline bool smax(T &x, const U &y) {
  return x < y ? x = y, 1 : 0;
}
constexpr int N(1e5 + 5), P(1e9 + 7);
inline int fpow(int x, int k = P - 2) {
  assert(k >= 0);
  int r = 1;
  for (; k; k >>= 1, x = 1LL * x * x % P)
    if (k & 1) r = 1LL * r * x % P;
  return r;
}
constexpr std::array<int, 87> pr{
    2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
    53,  59,  61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
    383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449};
int n, m, a[N];
struct Node {
  Node *ls, *rs;
  int w;
  Node() {}
} buf[N * 100], *ptr = buf;
class SegmentTree {
 private:
  Node *rt;
  void ins(Node *&o, int l, int r, int x, int y) {
    if (!o) o = ptr++;
    smax(o->w, y);
    if (l == r) return;
    int mid = l + r >> 1;
    x <= mid ? ins(o->ls, l, mid, x, y) : ins(o->rs, mid + 1, r, x, y);
  }
  int ask(Node *o, int l, int r, int x, int y) {
    if (!o) return 0;
    if (x <= l && r <= y) return o->w;
    int mid = l + r >> 1;
    if (y <= mid) return ask(o->ls, l, mid, x, y);
    if (x > mid) return ask(o->rs, mid + 1, r, x, y);
    return std::max(ask(o->ls, l, mid, x, y), ask(o->rs, mid + 1, r, x, y));
  }

 public:
  inline void ins(int x, int y) { ins(rt, 1, n, x, y); }
  inline int ask(int l, int r) { return ask(rt, 1, n, l, r); }
} t[87];
Node *rt[N], *null = new Node();
void ins(Node *&o, int l, int r, int x, int y) {
  *ptr = *o, o = ptr++;
  o->w = 1LL * o->w * y % P;
  if (l == r) return;
  int mid = l + r >> 1;
  x <= mid ? ins(o->ls, l, mid, x, y) : ins(o->rs, mid + 1, r, x, y);
}
int ask(Node *x, Node *y, int l, int r, int z) {
  if (r <= z) return 1LL * fpow(x->w) * y->w % P;
  int mid = l + r >> 1;
  if (z <= mid) return ask(x->ls, y->ls, l, mid, z);
  return 1LL * ask(x->ls, y->ls, l, mid, z) * ask(x->rs, y->rs, mid + 1, r, z) %
         P;
}
std::map<int, int> pos;
std::mt19937_64 ha(
    std::chrono::high_resolution_clock::now().time_since_epoch().count());
void gen() {
  n = 1e5;
  for (int i = 1; i <= n; i++) a[i] = ha() % 200000 + 1;
}
int main() {
  readInt(n);
  for (int i = 1; i <= n; i++) readInt(a[i]);
  null->ls = null->rs = null, null->w = 1;
  rt[0] = null;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < 87; j++) {
      if (pr[j] > a[i]) break;
      int c = 0;
      while (a[i] % pr[j] == 0) a[i] /= pr[j], c++;
      if (c) t[j].ins(i, c);
    }
    int &u = pos[a[i]];
    ins(rt[i] = rt[i - 1], 0, n - 1, u, a[i]);
    u = i;
  }
  int ans = 0;
  readInt(m);
  while (m--) {
    int l, r;
    readInt(l, r);
    l = (ans + l) % n + 1, r = (ans + r) % n + 1;
    if (l > r) std::swap(l, r);
    ans = ask(rt[l - 1], rt[r], 0, n - 1, l - 1);
    for (int i = 0; i < 87; i++) {
      ans = 1LL * ans * fpow(pr[i], t[i].ask(l, r)) % P;
    }
    printf("%d\n", ans);
  }
  return 0;
}
