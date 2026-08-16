#include <bits/stdc++.h>
using namespace std;
const int N = 5e5;
const int TN = N << 2;
const int inf = 0x3f3f3f3f;
namespace IO {
inline int read() {
  int s = 0, ww = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') ww = -1;
    ch = getchar();
  }
  while ('0' <= ch && ch <= '9') {
    s = 10 * s + ch - '0';
    ch = getchar();
  }
  return s * ww;
}
inline void write(int x) {
  if (x < 0) putchar('-'), x = -x;
  if (x > 9) write(x / 10);
  putchar('0' + x % 10);
}
}  // namespace IO
using namespace IO;
int n, cnt;
int id[N + 5], a[N + 5];
pair<int, int> p[N + 5];
struct OrdSegTree {
  int minn[TN + 5], num[TN + 5], flag[TN + 5];
  bool found;
  int i;
  inline void pushup(int u) {
    if (minn[(u << 1)] < minn[((u << 1) | 1)])
      minn[u] = minn[(u << 1)], num[u] = num[(u << 1)];
    else if (minn[(u << 1)] > minn[((u << 1) | 1)])
      minn[u] = minn[((u << 1) | 1)], num[u] = num[((u << 1) | 1)];
    else
      minn[u] = minn[(u << 1)], num[u] = num[(u << 1)] + num[((u << 1) | 1)];
  }
  inline void pushdown(int u) {
    if (flag[u] == 0) return;
    flag[(u << 1)] += flag[u];
    minn[(u << 1)] += flag[u];
    flag[((u << 1) | 1)] += flag[u];
    minn[((u << 1) | 1)] += flag[u];
    flag[u] = 0;
  }
  void build(int u, int l, int r) {
    if (l == r) {
      minn[u] = inf;
      num[u] = 1;
      return;
    }
    int m = (l + r) >> 1;
    build((u << 1), l, m);
    build(((u << 1) | 1), m + 1, r);
    pushup(u);
  }
  void assign(int u, int l, int r, int pos, int x) {
    if (l == r) {
      minn[u] = x, num[u] = 1;
      return;
    }
    pushdown(u);
    int m = (l + r) >> 1;
    if (pos <= m)
      assign((u << 1), l, m, pos, x);
    else
      assign(((u << 1) | 1), m + 1, r, pos, x);
    pushup(u);
  }
  void ud(int u, int l, int r, int ql, int qr, int d) {
    if (ql > qr) return;
    if (l == ql && r == qr) {
      minn[u] += d;
      flag[u] += d;
      return;
    }
    pushdown(u);
    int m = (l + r) >> 1;
    if (qr <= m)
      ud((u << 1), l, m, ql, qr, d);
    else if (ql > m)
      ud(((u << 1) | 1), m + 1, r, ql, qr, d);
    else
      ud((u << 1), l, m, ql, m, d), ud(((u << 1) | 1), m + 1, r, m + 1, qr, d);
    pushup(u);
  }
  void search(int u, int l, int r) {
    if (found || minn[u] > 1) return;
    if (l == r) {
      found = 1;
      i = l;
      return;
    }
    pushdown(u);
    int m = (l + r) >> 1;
    if (minn[(u << 1)] <= 1)
      search((u << 1), l, m);
    else
      search(((u << 1) | 1), m + 1, r);
  }
  void find_first1(int u, int l, int r, int ql, int qr) {
    if (ql > qr) return;
    if (ql == l && qr == r) {
      search(u, l, r);
      return;
    }
    pushdown(u);
    int m = (l + r) >> 1;
    if (qr <= m)
      find_first1((u << 1), l, m, ql, qr);
    else if (ql > m)
      find_first1(((u << 1) | 1), m + 1, r, ql, qr);
    else
      find_first1((u << 1), l, m, ql, m),
          find_first1(((u << 1) | 1), m + 1, r, m + 1, qr);
  }
  int flip_first1_after(int pos) {
    found = 0;
    i = 0;
    find_first1(1, 1, n, pos + 1, n);
    if (!found) {
      ud(1, 1, n, pos + 1, n, -1);
      return 0;
    }
    ud(1, 1, n, pos + 1, i - 1, -1);
    assign(1, 1, n, i, inf);
    return i;
  }
  inline void print(int u, int l, int r) {
    cout << "u=" << u << " l=" << l << " r=" << r << " minn=" << minn[u]
         << " num=" << num[u] << " flag=" << flag[u] << endl;
    if (l == r) return;
    pushdown(u);
    int m = (l + r) >> 1;
    print((u << 1), l, m);
    print(((u << 1) | 1), m + 1, r);
  }
} Td;
struct SegTree {
  int type[TN + 5], sum[TN + 5][2];
  inline void pushup(int u) {
    sum[u][0] = sum[(u << 1)][0] + sum[((u << 1) | 1)][0];
    sum[u][1] = sum[(u << 1)][1] + sum[((u << 1) | 1)][1];
  }
  void build(int u, int l, int r) {
    if (l == r) {
      type[u] = 2;
      sum[u][0] = sum[u][1] = 0;
      return;
    }
    int m = (l + r) >> 1;
    build((u << 1), l, m);
    build(((u << 1) | 1), m + 1, r);
    pushup(u);
  }
  void ud(int u, int l, int r, int pos, int x) {
    if (l == r) {
      type[u] = x;
      sum[u][0] = (type[u] == 0);
      sum[u][1] = (type[u] == 1);
      return;
    }
    int m = (l + r) >> 1;
    if (pos <= m)
      ud((u << 1), l, m, pos, x);
    else
      ud(((u << 1) | 1), m + 1, r, pos, x);
    pushup(u);
  }
  void flip_first0(int u, int l, int r) {
    if (sum[u][0] < 1) return;
    if (l == r) {
      Td.ud(1, 1, n, 1, l - 1, 1);
      Td.assign(1, 1, n, l, 1);
      type[u] = 1;
      sum[u][0] = 0;
      sum[u][1] = 1;
      return;
    }
    int m = (l + r) >> 1;
    if (sum[(u << 1)][0] >= 1)
      flip_first0((u << 1), l, m);
    else
      flip_first0(((u << 1) | 1), m + 1, r);
    pushup(u);
  }
  void flip(int u, int l, int r) {
    if (sum[u][0] < 1) {
      Td.ud(1, 1, n, 1, n, 1);
      return;
    } else
      flip_first0(u, l, r);
  }
  int getsum(int u, int l, int r, int ql, int qr) {
    if (ql > qr) return 0;
    if (l == ql && r == qr) return sum[u][1];
    int m = (l + r) >> 1;
    if (qr <= m)
      return getsum((u << 1), l, m, ql, qr);
    else if (ql > m)
      return getsum(((u << 1) | 1), m + 1, r, ql, qr);
    else
      return getsum((u << 1), l, m, ql, m) +
             getsum(((u << 1) | 1), m + 1, r, m + 1, qr);
  }
  inline int query() { return sum[1][1]; }
  inline void print(int u, int l, int r) {
    cout << "u=" << u << " l=" << l << " r=" << r << " type=" << type[u]
         << " sum0=" << sum[u][0] << " sum1=" << sum[u][1] << endl;
    if (l == r) return;
    int m = (l + r) >> 1;
    print((u << 1), l, m);
    print(((u << 1) | 1), m + 1, r);
  }
} T;
void solve() {
  int ans = cnt + T.query();
  write(ans), putchar('\n');
}
struct cmp {
  bool operator()(int x, int y) { return id[x] < id[y]; }
};
priority_queue<int, vector<int>, cmp> pq;
int main() {
  n = read();
  for (register int i = 1; i <= n; i++) {
    a[i] = read();
    p[i] = make_pair(a[i], i);
  }
  sort(p + 1, p + n + 1);
  for (register int i = 1; i <= n; i++) id[p[i].second] = i;
  cnt = 0;
  T.build(1, 1, n);
  Td.build(1, 1, n);
  for (register int i = 1; i <= n; i++) {
    if (a[i] < cnt) {
      if (pq.empty()) {
        pq.push(i);
        cnt--;
        T.flip(1, 1, n);
      } else {
        int j = pq.top();
        if (cnt == a[j]) {
          pq.pop();
          T.ud(1, 1, n, id[j], 0);
        } else {
          cnt--;
          T.flip(1, 1, n);
        }
        pq.push(i);
      }
    } else {
      int cur = cnt + T.getsum(1, 1, n, 1, id[i] - 1);
      if (cur == a[i]) {
        T.ud(1, 1, n, id[i], 0);
      } else {
        T.ud(1, 1, n, id[i], 1);
        Td.assign(1, 1, n, id[i], a[i] - cur);
        int pos = Td.flip_first1_after(id[i]);
        if (pos) T.ud(1, 1, n, pos, 0);
      }
    }
    solve();
  }
  return 0;
}
