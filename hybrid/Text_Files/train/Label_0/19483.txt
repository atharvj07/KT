#include <bits/stdc++.h>
template <class t>
inline void read(t &s) {
  s = 0;
  register int f = 1;
  register char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (isdigit(c)) s = (s << 3) + (s << 1) + (c ^ 48), c = getchar();
  s *= f;
  return;
}
template <class t, class... A>
inline void read(t &x, A &...a) {
  read(x);
  read(a...);
}
template <class t>
inline void write(t x) {
  if (x < 0) putchar('-'), x = -x;
  int buf[21], top = 0;
  while (x) buf[++top] = x % 10, x /= 10;
  if (!top) buf[++top] = 0;
  while (top) putchar(buf[top--] ^ '0');
  return;
}
inline void setIn(std::string s) {
  freopen(s.c_str(), "r", stdin);
  return;
}
inline void setOut(std::string s) {
  freopen(s.c_str(), "w", stdout);
  return;
}
inline void setIO(std::string s = "") {
  setIn(s + ".in");
  setOut(s + ".out");
  return;
}
template <class t>
inline bool checkmin(t &x, t y) {
  if (x > y) {
    x = y;
    return 1;
  }
  return 0;
}
template <class t>
inline bool checkmax(t &x, t y) {
  if (x < y) {
    x = y;
    return 1;
  }
  return 0;
}
inline int lowbit(int x) { return x & (-x); }
const int MaxN = 1e5 + 50;
std::unordered_set<int> S[MaxN], d;
int p[MaxN], to[MaxN], n, K;
struct Answer {
  int x, y, z;
  Answer() { x = y = z = 0; }
  Answer(int a, int b, int c) { x = a, y = b, z = c; }
};
std::vector<Answer> ans;
inline void go(int x, int y, int z) {
  assert(S[p[x]].count(z)), assert(!S[p[y]].count(z));
  S[p[x]].erase(z), S[p[y]].insert(z);
  ans.push_back(Answer(p[x], p[y], z));
}
signed main(void) {
  read(n, K);
  register int all = 0;
  for (int i = 1; i <= n; ++i) {
    int x, y;
    read(x);
    all += x, p[i] = i;
    while (x--) read(y), S[i].insert(y);
  }
  std::sort(p + 1, p + n + 1,
            [&](int a, int b) { return S[a].size() > S[b].size(); });
  for (int i = 1; i <= all; ++i) ++to[(i - 1) % n + 1];
  register int L = 1, R = n;
  if (L < R) {
    d = S[p[L]];
    for (auto i : S[p[R]])
      if (d.count(i)) d.erase(i);
  }
  while (L < R) {
    while ((int)S[p[L]].size() == to[L]) {
      if (++L == R) break;
      d = S[p[L]];
      for (auto i : S[p[R]])
        if (d.count(i)) d.erase(i);
    }
    while ((int)S[p[R]].size() == to[R]) {
      for (auto i : S[p[R]])
        if (S[p[L]].count(i) && !d.count(i)) d.insert(i);
      if (--R == L) break;
      for (auto i : S[p[R]])
        if (d.count(i)) d.erase(i);
    }
    if (L >= R) break;
    register int x = *d.begin();
    go(L, R, x);
    d.erase(d.begin());
  }
  write((int)ans.size()), std::puts("");
  for (auto i : ans)
    write(i.x), std::putchar(32), write(i.y), std::putchar(32), write(i.z),
        std::puts("");
  return 0;
}
