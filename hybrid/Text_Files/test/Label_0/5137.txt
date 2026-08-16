#include <bits/stdc++.h>
using namespace std;
namespace mine {
long long qread() {
  long long ans = 0, f = 1;
  char c = getchar();
  while (c < '0' or c > '9') {
    if (c == '-') f = -1;
    c = getchar();
  }
  while ('0' <= c and c <= '9') ans = ans * 10 + c - '0', c = getchar();
  return ans * f;
}
void write(long long num) {
  if (num < 0) putchar('-'), num = -num;
  if (num >= 10) write(num / 10);
  putchar('0' + num % 10);
}
void write1(long long num) {
  write(num);
  putchar(' ');
}
void write2(long long num) {
  write(num);
  putchar('\n');
}
template <typename T>
void chmax(T &x, const T y) {
  x = (x > y ? x : y);
}
template <typename T>
void chmin(T &x, const T y) {
  x = (x < y ? x : y);
}
long long gcd(long long x, long long y) { return y ? gcd(y, x % y) : x; }
const int INF = 0x3f3f3f3f;
const int MOD = 998244353;
inline int mm(const int x) { return x >= MOD ? x - MOD : x; }
template <typename T>
inline void add(T &x, const T y) {
  x = mm(x + y);
}
inline long long qpower(long long x, long long e, int mod = MOD) {
  long long ans = 1;
  if (e < 0) {
    puts("error");
    exit(666);
  }
  while (e) {
    if (e & 1) ans = ans * x % mod;
    x = x * x % mod;
    e >>= 1;
  }
  return ans;
}
long long invm(long long x) { return qpower(x, MOD - 2); }
const int N = 2e5 + 10;
int n;
namespace SGT {
int mxc[N * 4];
void change_cnt(int x, int l, int r, int pos, int num) {
  if (l == r) {
    mxc[x] = num;
    return;
  }
  if (pos <= (l + r) / 2)
    change_cnt(x << 1, l, (l + r) / 2, pos, num);
  else
    change_cnt(x << 1 | 1, (l + r) / 2 + 1, r, pos, num);
  mxc[x] = max(mxc[x << 1], mxc[x << 1 | 1]);
}
int ask_cnt(int x, int l, int r, int fl, int fr) {
  if (fl > fr) return 0;
  if (l == fl and r == fr) return mxc[x];
  if (fr <= (l + r) / 2) return ask_cnt(x << 1, l, (l + r) / 2, fl, fr);
  if (fl > (l + r) / 2) return ask_cnt(x << 1 | 1, (l + r) / 2 + 1, r, fl, fr);
  return max(ask_cnt(x << 1, l, (l + r) / 2, fl, (l + r) / 2),
             ask_cnt(x << 1 | 1, (l + r) / 2 + 1, r, (l + r) / 2 + 1, fr));
}
int mif[N * 4], tag[N * 4], mifl[N * 4], mifr[N * 4], sum[N * 4];
void init(int x, int l, int r) {
  mifl[x] = l;
  mifr[x] = r;
  if (l < r) init(x << 1, l, (l + r) / 2), init(x << 1 | 1, (l + r) / 2 + 1, r);
}
void pushdown(int x) {
  if (tag[x] != 0)
    mif[x << 1] += tag[x], mif[x << 1 | 1] += tag[x], tag[x << 1] += tag[x],
        tag[x << 1 | 1] += tag[x], tag[x] = 0;
}
void pushup(int x, int l, int r) {
  if (l == r) {
    sum[x] = ask_cnt(x, l, r, l, l);
    return;
  }
  pushdown(x);
  if (mif[x << 1] == mif[x << 1 | 1]) {
    mif[x] = mif[x << 1];
    mifl[x] = mifl[x << 1];
    mifr[x] = mifr[x << 1 | 1];
    sum[x] = sum[x << 1] + sum[x << 1 | 1] -
             ask_cnt(x, l, r, mifr[x << 1] + 1, (l + r) / 2) -
             ask_cnt(x, l, r, (l + r) / 2 + 1, mifl[x << 1 | 1]) +
             ask_cnt(x, l, r, mifr[x << 1] + 1, mifl[x << 1 | 1]);
  } else if (mif[x << 1] < mif[x << 1 | 1]) {
    mif[x] = mif[x << 1];
    mifl[x] = mifl[x << 1];
    mifr[x] = mifr[x << 1];
    sum[x] = sum[x << 1] - ask_cnt(x, l, r, mifr[x << 1] + 1, (l + r) / 2) +
             ask_cnt(x, l, r, mifr[x << 1] + 1, r);
  } else {
    mif[x] = mif[x << 1 | 1];
    mifl[x] = mifl[x << 1 | 1];
    mifr[x] = mifr[x << 1 | 1];
    sum[x] = sum[x << 1 | 1] -
             ask_cnt(x, l, r, (l + r) / 2 + 1, mifl[x << 1 | 1]) +
             ask_cnt(x, l, r, l, mifl[x << 1 | 1]);
  }
}
void add_f(int x, int l, int r, int fl, int fr, int val) {
  if (l == fl and r == fr) {
    mif[x] += val;
    tag[x] += val;
    pushup(x, l, r);
    return;
  }
  pushdown(x);
  if (fr <= (l + r) / 2)
    add_f(x << 1, l, (l + r) / 2, fl, fr, val);
  else if (fl > (l + r) / 2)
    add_f(x << 1 | 1, (l + r) / 2 + 1, r, fl, fr, val);
  else
    add_f(x << 1, l, (l + r) / 2, fl, (l + r) / 2, val),
        add_f(x << 1 | 1, (l + r) / 2 + 1, r, (l + r) / 2 + 1, fr, val);
  pushup(x, l, r);
}
void add_f(int l, int r, int val) {
  if (l <= r) add_f(1, 1, n, l, r, val);
}
void change_cnt(int pos, int num) {
  change_cnt(1, 1, n, pos, num);
  add_f(pos, pos, 0);
}
};  // namespace SGT
int a[N];
set<int> pos[N];
void main() {
  n = qread();
  int q = qread();
  SGT::init(1, 1, n);
  for (int i = (1), I = (n); i <= I; i++) a[i] = qread(), pos[a[i]].insert(i);
  for (int num = (1), I = (N - 1); num <= I; num++)
    if (((int)(pos[num]).size()))
      SGT::change_cnt(*pos[num].begin(), ((int)(pos[num]).size())),
          SGT::add_f(*pos[num].begin(), *(--pos[num].end()) - 1, 1);
  write2(n - SGT::sum[1]);
  while (q--) {
    int x = qread(), val = qread();
    set<int>::iterator now = pos[a[x]].find(x);
    SGT::change_cnt(*pos[a[x]].begin(), 0);
    if (((int)(pos[a[x]]).size()) > 1) {
      if (now == pos[a[x]].begin())
        SGT::add_f(x, *(++now) - 1, -1);
      else if (now == --pos[a[x]].end())
        SGT::add_f(*(--now), x - 1, -1);
    }
    pos[a[x]].erase(x);
    if (((int)(pos[a[x]]).size()))
      SGT::change_cnt(*pos[a[x]].begin(), ((int)(pos[a[x]]).size()));
    a[x] = val;
    pos[a[x]].insert(x);
    SGT::change_cnt(*pos[a[x]].begin(), ((int)(pos[a[x]]).size()));
    now = pos[a[x]].find(x);
    if (((int)(pos[a[x]]).size()) > 1) {
      if (now == pos[a[x]].begin()) {
        now++;
        SGT::add_f(x, *now - 1, 1);
        SGT::change_cnt(*now, 0);
      } else if (now == --pos[a[x]].end())
        SGT::add_f(*(--now), x - 1, 1);
    }
    write2(n - SGT::sum[1]);
  }
}
};  // namespace mine
signed main() {
  srand(time(0));
  mine::main();
}
