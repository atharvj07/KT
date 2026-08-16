#include <bits/stdc++.h>
#pragma GCC optimize(2)
#pragma GCC optimize("Ofast")
using namespace std;
namespace Base {
inline char gc(void) {
  static char buf[100000], *p1 = buf, *p2 = buf;
  return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 100000, stdin), p1 == p2)
             ? EOF
             : *p1++;
}
template <class T>
inline void read(T &x) {
  T flag = (T)1;
  x = 0;
  static char ch = gc();
  for (; ch > '9' || ch < '0'; ch = gc()) flag = ch == '-' ? -1 : 1;
  for (; ch >= '0' && ch <= '9'; ch = gc()) x = (x << 1) + (x << 3) + (ch & 15);
  x *= flag;
  return;
}
inline void readstr(string &x) {
  x = "";
  static char ch;
  while (isspace(ch = gc()))
    ;
  while (x += ch, !isspace(ch = gc()))
    ;
}
inline void readstr(char *s) {
  do *s = gc();
  while ((*s == ' ') || (*s == '\n') || (*s == '\r'));
  do *(++s) = gc();
  while ((~*s) && (*s != ' ') && (*s != '\n') && (*s != '\r'));
  *s = 0;
  return;
}
inline void printstr(string x, int num = 0, char ch = '\n') {
  for (int i = num; i < x.size(); ++i) putchar(x[i]);
  putchar(ch);
}
inline void readch(char &x) {
  while (isspace(x = gc()))
    ;
}
char pf[100000], *o1 = pf, *o2 = pf + 100000;
template <class T>
inline void println(T x, char c = '\n') {
  if (x < 0)
    (o1 == o2 ? fwrite(pf, 1, 100000, stdout), *(o1 = pf)++ = 45 : *o1++ = 45),
        x = -x;
  static char s[15], *b;
  b = s;
  if (!x) *b++ = 48;
  for (; x; *b++ = x % 10 + 48, x /= 10)
    ;
  for (; b-- != s; (o1 == o2          ? fwrite(pf, 1, 100000, stdout),
                    *(o1 = pf)++ = *b : *o1++ = *b))
    ;
  (o1 == o2 ? fwrite(pf, 1, 100000, stdout), *(o1 = pf)++ = c : *o1++ = c);
}
int wbuf[25], _wl = 0;
template <class T>
inline void write(T x) {
  if (x == 0) {
    putchar(48);
    return;
  }
  if (x < 0) putchar('-'), x = -x;
  _wl = 0;
  while (x) wbuf[++_wl] = x % 10, x /= 10;
  for (int i = _wl; i >= 1; i--) putchar(wbuf[i] + 48);
}
template <class T>
inline void writeln(T x) {
  write(x);
  puts("");
}
template <class T>
inline void writeln(T x, char c) {
  write(x);
  putchar(c);
}
template <class T>
inline void writeln(char c, T x) {
  putchar(c);
  write(x);
}
template <class T>
inline void chkmax(T &x, const T y) {
  x > y ? x = x : x = y;
}
template <class T>
inline void chkmin(T &x, const T y) {
  x < y ? x = x : x = y;
}
template <class T>
inline T max(const T &x, const T &y, const T &z) {
  return x > y ? (x > z ? x : z) : (y > z ? y : z);
}
inline void file(string str) {
  freopen((str + ".in").c_str(), "r", stdin);
  freopen((str + ".out").c_str(), "w", stdout);
}
struct Vector {
  double x, y;
  Vector(double _x = 0, double _y = 0) : x(_x), y(_y) {}
  inline Vector Vary(void) { return Vector(x, -y); }
  inline bool operator<(const Vector &rhs) const {
    return x == rhs.x ? y < rhs.y : x < rhs.x;
  }
  inline Vector operator-(const Vector &rhs) const {
    return Vector(x - rhs.x, y - rhs.y);
  }
  inline Vector operator+(const Vector &rhs) const {
    return Vector(x + rhs.x, y + rhs.y);
  }
  inline Vector operator*(const double &rhs) const {
    return Vector(x * rhs, y * rhs);
  }
  inline Vector operator/(const double &rhs) const {
    return Vector(x / rhs, y / rhs);
  }
  inline Vector operator*(const Vector &rhs) const {
    return Vector(x * rhs.x - y * rhs.y, x * rhs.y + y * rhs.x);
  }
};
}  // namespace Base
using namespace Base;
const int N = 1e6 + 100;
int x[N], y[N], w[N], s[N], v[N];
bool in[N * 2];
vector<pair<int, int> > e[N];
vector<int> res;
int n, m;
int main() {
  read(n);
  read(m);
  for (register int i = (1); i <= (m); i++) {
    read(x[i]);
    read(y[i]);
    w[i] = 1;
    s[x[i]]++;
    s[y[i]]++;
    e[max(x[i], y[i])].push_back(make_pair(min(x[i], y[i]), i));
  }
  for (register int i = (1); i <= (n); i++) {
    for (register int it = (0); it < (int(e[i].size())); it++) {
      if (!v[e[i][it].first]) {
        v[e[i][it].first] = 1;
        w[e[i][it].second] = 0;
        s[i]--;
      }
      in[s[e[i][it].first]] = 1;
    }
    for (register int it = (0); it < (int(e[i].size())); it++) {
      if (!in[s[i]]) break;
      s[i]++;
      v[e[i][it].first] = 0;
      w[e[i][it].second]++;
    }
    for (register int it = (0); it < (int(e[i].size())); it++)
      in[s[e[i][it].first]] = 0;
  }
  for (register int i = (1); i <= (n); i++)
    if (v[i]) res.push_back(i);
  writeln(int(res.size()));
  for (register int it = (0); it < (int(res.size())); it++)
    writeln(res[it], ' ');
  puts("");
  for (register int i = (1); i <= (m); i++) {
    writeln(x[i], ' ');
    writeln(y[i], ' ');
    writeln(w[i]);
  }
  return 0;
}
