#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 5;
const long long mod = 1e9 + 7;
const int alphabet = 26;
const int inf = INT_MAX;
const long long linf = 1e18 + 9;
namespace util {
inline long long cnm(char ch) { return (ch - '0'); }
inline long long cap(char ch) { return (ch - 'a'); }
inline void instr(string& s, long long& n) {
  cin >> s;
  n = s.length();
}
inline void instr(string& s) { cin >> s; }
template <typename T>
T gcd(T a, T b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
template <typename T>
bool min(T a, T b, T c) {
  return std::min(a, std::min(b, c));
}
}  // namespace util
using namespace util;
void solve() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long i, j, k, m, n;
  string a, b, ans = "";
  instr(a, n);
  instr(b, m);
  int onesa = 0, onesb = 0;
  for (i = 0; i < n; i++) {
    if (a[i] == '1') onesa++;
  }
  for (i = 0; i < m; i++) {
    if (b[i] == '1') onesb++;
  }
  if ((onesa + onesa % 2) >= onesb) {
    ans = "YES";
  } else
    ans = "NO";
  cout << ans;
  return;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t = 1;
  while (t--) {
    solve();
  }
  return 0;
}
