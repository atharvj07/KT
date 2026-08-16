#include <bits/stdc++.h>
using namespace std;
struct vec {
  int x, y;
  friend long long operator/(const vec& a, const vec& b) {
    return 1LL * a.x * b.y - 1LL * a.y * b.x;
  }
  friend long long operator*(const vec& a, const vec& b) {
    return 1LL * a.x * b.x + 1LL * a.y * b.y;
  }
};
struct meg {
  int g, x, y;
} a[500005];
struct met {
  vec v;
  int pos;
} b0[500005], b1[500005];
struct its {
  int x, y;
} s[500005];
struct itv {
  vec x, y;
} d[500005];
struct Que {
  priority_queue<int> A, B;
  void push(int x) { A.push(x); }
  void dele(int x) { B.push(x); }
  int top() {
    while (!B.empty() && A.top() == B.top()) A.pop(), B.pop();
    if (!A.empty())
      return A.top();
    else
      return 0;
  }
} q[500005];
int m, MQ, tin, b0in, b1in, ra, t[1100005];
inline int read() {
  int n = 0, f = 1;
  char c = getchar();
  while (c < '0' || c > '9') {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    n = n * 10 + c - '0';
    c = getchar();
  }
  return n * f;
}
inline void getcg(int x, int z) {
  for (t[x += MQ] = z, x >>= 1; x; x >>= 1)
    t[x] = max(t[(x << 1)], t[(x << 1 | 1)]);
}
inline int getmax(int L, int R) {
  int sum = 0;
  for (L += MQ, R += MQ; L <= R; L >>= 1, R >>= 1) {
    if (L & 1) sum = max(sum, t[L++]);
    if (~R & 1) sum = max(sum, t[R--]);
  }
  return sum;
}
void cghp(int x, int y, int g) {
  int lt = q[x].top();
  if (g == 1)
    q[x].push(y);
  else
    q[x].dele(y);
  if (lt != q[x].top()) getcg(x, q[x].top());
}
bool check(int x, int y) {
  int cs1, cs2;
  if (s[x].x > s[y].x)
    cs1 = x;
  else
    cs1 = y;
  if (s[x].y < s[y].y)
    cs2 = x;
  else
    cs2 = y;
  if (d[cs2].y * d[cs1].x < 0)
    return true;
  else
    return false;
}
bool cmp(const met& a, const met& b) { return a.v / b.v > 0; }
int main() {
  register int i, x, y;
  ra = read();
  m = read();
  for (i = 1; i <= m; ++i) {
    a[i].g = read();
    if (a[i].g == 1) {
      x = read();
      y = read();
      a[i].x = ++tin;
      d[tin].x.x = x - ra;
      d[tin].x.y = y;
      d[tin].y.x = x + ra;
      d[tin].y.y = y;
      b0[++b0in] = (met){d[tin].x, tin};
      b1[++b1in] = (met){d[tin].y, tin};
    } else if (a[i].g == 2)
      a[i].x = read();
    else if (a[i].g == 3)
      a[i].x = read(), a[i].y = read();
  }
  sort(b0 + 1, b0 + b0in + 1, cmp);
  sort(b1 + 1, b1 + b1in + 1, cmp);
  b0[0].pos = b1[0].pos = s[0].x = s[0].y = 0;
  for (i = 1; i <= b0in; ++i)
    if (i > 1 && b0[i - 1].v / b0[i].v == 0)
      s[b0[i].pos].x = s[b0[i - 1].pos].x;
    else
      s[b0[i].pos].x = s[b0[i - 1].pos].x + 1;
  for (i = 1; i <= b1in; ++i)
    if (i > 1 && b1[i - 1].v / b1[i].v == 0)
      s[b1[i].pos].y = s[b1[i - 1].pos].y;
    else
      s[b1[i].pos].y = s[b1[i - 1].pos].y + 1;
  b0in = s[b0[b0in].pos].x;
  for (MQ = 1; MQ < b0in; MQ <<= 1)
    ;
  --MQ;
  for (i = 1; i <= m; ++i) {
    if (a[i].g < 3)
      cghp(s[a[i].x].x, s[a[i].x].y, a[i].g);
    else if (a[i].g == 3) {
      if (check(a[i].x, a[i].y)) {
        puts("NO");
        continue;
      }
      x = max(s[a[i].x].x, s[a[i].y].x);
      y = min(s[a[i].x].y, s[a[i].y].y);
      cghp(s[a[i].x].x, s[a[i].x].y, 2);
      cghp(s[a[i].y].x, s[a[i].y].y, 2);
      if (getmax(1, x) >= y)
        puts("NO");
      else
        puts("YES");
      cghp(s[a[i].x].x, s[a[i].x].y, 1);
      cghp(s[a[i].y].x, s[a[i].y].y, 1);
    }
  }
  return 0;
}
