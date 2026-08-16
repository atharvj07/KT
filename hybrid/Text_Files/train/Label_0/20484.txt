#include <bits/stdc++.h>
using namespace std;
inline long long mod(long long n, long long m) {
  long long ret = n % m;
  if (ret < 0) ret += m;
  return ret;
}
long long gcd(long long a, long long b) { return (b == 0 ? a : gcd(b, a % b)); }
long long exp(long long a, long long b, long long m) {
  if (b == 0) return 1;
  if (b == 1) return mod(a, m);
  long long k = mod(exp(a, b / 2, m), m);
  if (b & 1) {
    return mod(a * mod(k * k, m), m);
  } else
    return mod(k * k, m);
}
long long n, m, a, b;
long long g[3010 * 3010];
long long M[3010][3010];
long long M2[3010][3010];
long long x, y, z;
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n >> m >> a >> b;
  cin >> g[0] >> x >> y >> z;
  for (long long i = 1; i <= n * m; i++) {
    g[i] = mod(mod(g[i - 1], z) * x + y, z);
  }
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= m; j++) {
      M[i][j] = g[(i - 1) * m + j - 1];
    }
  }
  for (long long i = 1; i <= n; i++) {
    deque<pair<long long, long long> > d;
    for (long long k = 1; k < b; k++) {
      long long atual = M[i][k];
      while (!d.empty() && d.back().first >= atual) d.pop_back();
      d.push_back(pair<long long, long long>(atual, k));
    }
    for (long long j = b; j <= m; j++) {
      long long atual = M[i][j];
      while (!d.empty() && d.front().second <= j - b) {
        d.pop_front();
      }
      while (!d.empty() && d.back().first >= atual) d.pop_back();
      d.push_back(pair<long long, long long>(atual, j));
      M2[i][j - b] = d.front().first;
    }
  }
  long long res = 0;
  for (long long i = 0; i <= m - b; i++) {
    deque<pair<long long, long long> > d;
    for (long long k = 1; k < a; k++) {
      long long atual = M2[k][i];
      while (!d.empty() && d.back().first >= atual) d.pop_back();
      d.push_back(pair<long long, long long>(atual, k));
    }
    for (long long j = a; j <= n; j++) {
      long long atual = M2[j][i];
      while (!d.empty() && d.front().second <= j - a) {
        d.pop_front();
      }
      while (!d.empty() && d.back().first >= atual) d.pop_back();
      d.push_back(pair<long long, long long>(atual, j));
      res += d.front().first;
    }
  }
  cout << res << "\n";
}
