#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long sum = 0, f = 1;
  char ch = getchar();
  while (ch != '-' && (ch < '0' || ch > '9')) ch = getchar();
  if (ch == '-') ch = getchar(), f = -1;
  while (ch <= '9' && ch >= '0') sum = sum * 10 + ch - '0', ch = getchar();
  return sum * f;
}
long long n, m;
long long val[500010];
long long gcd(long long a, long long b) { return !b ? a : gcd(b, a % b); }
const long long ch = 10097;
pair<unsigned long long, long long> f[500010];
vector<long long> from[500010];
map<pair<unsigned long long, long long>, long long> A;
long long fa[500010];
long long sum[500010];
long long find(long long w) { return fa[w] ? fa[w] = find(fa[w]) : w; }
signed main() {
  long long T = read();
  while (T--) {
    n = read(), m = read();
    for (long long i = 1; i <= n; i++)
      val[i] = read(), from[i].clear(), fa[i] = 0, sum[i] = 0;
    for (long long i = 1; i <= m; i++) {
      long long l = read(), r = read();
      from[r].push_back(l);
    }
    long long ans = 0;
    for (long long i = 1; i <= n; i++)
      if (from[i].size()) {
        ans += val[i];
        sort(from[i].begin(), from[i].end());
        unsigned long long g = 0;
        for (long long j = 0; j < from[i].size(); j++) {
          long long v = from[i][j];
          g *= ch;
          g += (v * 29 + 97);
        }
        f[i] = make_pair(g, from[i].size());
      }
    A.clear();
    for (long long i = 1; i <= n; i++)
      if (from[i].size()) {
        if (A.count(f[i]))
          fa[i] = A[f[i]];
        else
          A[f[i]] = i;
      }
    for (long long i = 1; i <= n; i++)
      if (from[i].size()) {
        long long gg = find(i);
        sum[gg] += val[i];
      }
    for (long long i = 1; i <= n; i++)
      if (sum[i]) ans = gcd(ans, sum[i]);
    cout << ans << '\n';
  }
  return 0;
}
