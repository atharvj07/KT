#include <bits/stdc++.h>
using namespace std;
template <class T>
void cmax(T& a, T b) {
  a = max(a, b);
}
template <class T>
void cmin(T& a, T b) {
  a = min(a, b);
}
void _BG(const char* s) {}
template <class T, class... TT>
void _BG(const char* s, T a, TT... b) {
  for (int c = 0; *s && (c || *s != ','); ++s) {
    cerr << *s;
    for (char x : "([{") c += *s == x;
    for (char x : ")]}") c -= *s == x;
  }
  cerr << " = " << a;
  if (*s) {
    cerr << ", ";
    _BG(++s, b...);
  } else
    cerr << endl;
}
bool RD() { return 1; }
bool RD(char& a) { return scanf(" %c", &a) == 1; }
bool RD(char* a) { return scanf("%s", a) == 1; }
bool RD(double& a) { return scanf("%lf", &a) == 1; }
bool RD(int& a) { return scanf("%d", &a) == 1; }
bool RD(long long& a) { return scanf("%lld", &a) == 1; }
template <class T, class... TT>
bool RD(T& a, TT&... b) {
  return RD(a) && RD(b...);
}
void PT(const char& a) { putchar(a); }
void PT(char const* const& a) { fputs(a, stdout); }
void PT(const double& a) { printf("%.16f", a); }
void PT(const int& a) { printf("%d", a); }
void PT(const long long& a) { printf("%lld", a); }
template <char s = ' ', char e = '\n'>
void PL() {
  if (e) PT(e);
}
template <char s = ' ', char e = '\n', class T, class... TT>
void PL(const T& a, const TT&... b) {
  PT(a);
  if (sizeof...(b) && s) PT(s);
  PL<s, e>(b...);
}
const int N = 1e5 + 87;
const long long inf = 1e18;
long long a[N];
vector<pair<int, int> > g[N];
long long dfs(int u) {
  for (auto v : g[u]) {
    long long k = dfs(v.first);
    if (k >= 0)
      a[u] += k;
    else if (-k <= (inf + a[u]) / v.second)
      a[u] += k * v.second;
    else
      return a[u] = -inf;
  }
  return a[u];
}
int main() {
  int n;
  RD(n);
  for (int i(1); i < ((n) + 1); ++i) RD(a[i]);
  for (int i(1); i < ((n) + 1); ++i) {
    long long b;
    RD(b);
    a[i] -= b;
  }
  for (int i(2); i < ((n) + 1); ++i) {
    int p, k;
    RD(p, k);
    g[p].push_back({i, k});
  }
  PL(dfs(1) >= 0 ? "YES" : "NO");
}
