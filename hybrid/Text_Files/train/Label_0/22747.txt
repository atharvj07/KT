#include <bits/stdc++.h>
using namespace std;
template <class C>
void mini(C &a4, C b4) {
  a4 = min(a4, b4);
}
template <class C>
void maxi(C &a4, C b4) {
  a4 = max(a4, b4);
}
template <class TH>
void _dbg(const char *sdbg, TH h) {
  cerr << sdbg << "=" << h << "\n";
}
template <class TH, class... TA>
void _dbg(const char *sdbg, TH h, TA... a) {
  while (*sdbg != ',') cerr << *sdbg++;
  cerr << "=" << h << ",";
  _dbg(sdbg + 1, a...);
}
template <class T>
ostream &operator<<(ostream &os, vector<T> V) {
  os << "[";
  for (auto vv : V) os << vv << ",";
  return os << "]";
}
template <class L, class R>
ostream &operator<<(ostream &os, pair<L, R> P) {
  return os << "(" << P.first << "," << P.second << ")";
}
const long long MAX = 51;
string t[MAX];
long long n, m;
vector<pair<long long, long long> > licz(long long x) {
  long long bil = 0;
  for (long long i = (0); i <= ((long long)(n)-1); i++) {
    cin >> t[i];
    for (long long j = (0); j <= ((long long)(m)-1); j++) {
      if (t[i][j] == 'U') bil++;
      if (t[i][j] == 'L') bil--;
    }
  }
  vector<pair<long long, long long> > res;
  bool co = 0;
  while (bil != x) {
    if (co) {
      for (long long i = (0); i <= ((long long)(n - 1) - 1); i++)
        for (long long j = (0); j <= ((long long)(m - 1) - 1); j++) {
          if (t[i][j] == 'L' && t[i][j + 1] == 'R' && t[i + 1][j] == 'L' &&
              t[i + 1][j + 1] == 'R') {
            t[i][j] = t[i][j + 1] = 'U';
            t[i + 1][j] = t[i + 1][j + 1] = 'D';
            bil += 4;
            res.push_back({i, j});
          }
        }
    } else {
      for (long long i = (0); i <= ((long long)(n - 1) - 1); i++)
        for (long long j = (0); j <= ((long long)(m - 1) - 1); j++) {
          if (t[i][j] == 'U' && t[i][j + 1] == 'U' && t[i + 1][j] == 'D' &&
              t[i + 1][j + 1] == 'D') {
            t[i][j] = 'L';
            t[i][j + 1] = 'R';
            t[i + 1][j] = 'L';
            t[i + 1][j + 1] = 'R';
            bil -= 4;
            res.push_back({i, j});
          }
        }
    }
    co = !co;
  }
  return res;
}
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  if (0) cout << fixed << setprecision(6);
  cin >> n >> m;
  long long pom = n * m / 2;
  if (n & 1) pom *= -1;
  (pom);
  vector<pair<long long, long long> > a = licz(pom);
  ("xxx");
  vector<pair<long long, long long> > b = licz(pom);
  cout << ((long long)(a).size()) + ((long long)(b).size()) << "\n";
  for (pair<long long, long long> el : a) {
    cout << el.first + 1 << " " << el.second + 1 << "\n";
  }
  reverse((b).begin(), (b).end());
  for (pair<long long, long long> el : b) {
    cout << el.first + 1 << " " << el.second + 1 << "\n";
  }
}
