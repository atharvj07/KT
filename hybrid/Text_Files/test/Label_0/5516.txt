#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f, MAXN = 2e5 + 50;
const long long LINF = 0x3f3f3f3f3f3f3f3f, MOD = 1004535809;
const double Pi = acos(-1), EPS = 1e-6;
void test() { cerr << "\n"; }
template <typename T, typename... Args>
void test(T x, Args... args) {
  cerr << x << " ";
  test(args...);
}
inline long long qpow(long long a, long long b) {
  return b ? ((b & 1) ? a * qpow(a * a % MOD, b >> 1) % MOD
                      : qpow(a * a % MOD, b >> 1)) %
                 MOD
           : 1;
}
inline long long qpow(long long a, long long b, long long c) {
  return b ? ((b & 1) ? a * qpow(a * a % c, b >> 1) % c
                      : qpow(a * a % c, b >> 1)) %
                 c
           : 1;
}
inline long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
inline long long cede(long long a, long long b) {
  if (b < 0) return cede(-a, -b);
  if (a < 0) return a / b;
  return (a + b - 1) / b;
}
inline long long flde(long long a, long long b) {
  if (b < 0) return flde(-a, -b);
  if (a < 0) return (a - b + 1) / b;
  return a / b;
}
inline int sign(double x) { return x < -EPS ? -1 : x > EPS; }
inline int dbcmp(double l, double r) { return sign(l - r); }
namespace Fast_IO {
const int MAXL((1 << 18) + 1);
int iof, iotp;
char ioif[MAXL], *ioiS, *ioiT, ioof[MAXL],
    *iooS = ioof, *iooT = ioof + MAXL - 1, ioc, iost[55];
char Getchar() {
  if (ioiS == ioiT) {
    ioiS = ioif;
    ioiT = ioiS + fread(ioif, 1, MAXL, stdin);
    return (ioiS == ioiT ? EOF : *ioiS++);
  } else
    return (*ioiS++);
}
void Write() {
  fwrite(ioof, 1, iooS - ioof, stdout);
  iooS = ioof;
}
void Putchar(char x) {
  *iooS++ = x;
  if (iooS == iooT) Write();
}
inline int read() {
  int x = 0;
  for (iof = 1, ioc = Getchar(); ioc < '0' || ioc > '9';)
    iof = ioc == '-' ? -1 : 1, ioc = Getchar();
  for (x = 0; ioc <= '9' && ioc >= '0'; ioc = Getchar())
    x = (x << 3) + (x << 1) + (ioc ^ 48);
  return x * iof;
}
inline long long read_ll() {
  long long x = 0;
  for (iof = 1, ioc = Getchar(); ioc < '0' || ioc > '9';)
    iof = ioc == '-' ? -1 : 1, ioc = Getchar();
  for (x = 0; ioc <= '9' && ioc >= '0'; ioc = Getchar())
    x = (x << 3) + (x << 1) + (ioc ^ 48);
  return x * iof;
}
template <class Int>
void Print(Int x, char ch = '\0') {
  if (!x) Putchar('0');
  if (x < 0) Putchar('-'), x = -x;
  while (x) iost[++iotp] = x % 10 + '0', x /= 10;
  while (iotp) Putchar(iost[iotp--]);
  if (ch) Putchar(ch);
}
void Getstr(char *s, int &l) {
  for (ioc = Getchar(); ioc < 'a' || ioc > 'z';) ioc = Getchar();
  for (l = 0; ioc <= 'z' && ioc >= 'a'; ioc = Getchar()) s[l++] = ioc;
  s[l] = 0;
}
void Putstr(const char *s) {
  for (int i = 0, n = strlen(s); i < n; ++i) Putchar(s[i]);
}
}  // namespace Fast_IO
using namespace Fast_IO;
vector<int> to[MAXN];
int maxv;
vector<pair<int, int> > ans;
void dfs(int u, int fa, int tim) {
  int tmp = tim;
  ans.push_back({u, tim});
  for (int i = 0; i < to[u].size(); i++) {
    if (to[u][i] == fa) continue;
    if (tim == maxv) tim = maxv - to[u].size(), ans.push_back({u, tim});
    dfs(to[u][i], u, ++tim);
    ans.push_back({u, tim});
  }
  if (u != 1 && tim != tmp - 1) ans.push_back({u, tmp - 1});
}
void work() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i < n; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    to[u].push_back(v);
    to[v].push_back(u);
  }
  for (int i = 1; i <= n; i++) {
    maxv = max(maxv, (int)to[i].size());
  }
  dfs(1, -1, 0);
  printf("%d\n", ans.size());
  for (auto x : ans) printf("%d %d\n", x.first, x.second);
}
int main() { work(); }
