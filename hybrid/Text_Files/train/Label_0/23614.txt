#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:32000000")
using namespace std;
inline bool read(int& val) { return scanf("%d", &val) != -1; }
inline bool read(long long& val) { return scanf("%I64d", &val) != -1; }
inline bool read(double& val) { return scanf("%lf", &val) != -1; }
inline bool read(char* val) { return scanf("%s", val) != -1; }
template <class T1, class T2>
inline bool read(T1& a, T2& b) {
  return read(a) && read(b);
}
template <class T1, class T2, class T3>
inline bool read(T1& a, T2& b, T3& c) {
  return read(a) && read(b) && read(c);
}
template <class T1, class T2, class T3, class T4>
inline bool read(T1& a, T2& b, T3& c, T4& d) {
  return read(a) && read(b) && read(c) && read(d);
}
template <class T1, class T2, class T3, class T4, class T5>
inline bool read(T1& a, T2& b, T3& c, T4& d, T5& e) {
  return read(a) && read(b) && read(c) && read(d) && read(e);
}
const int N = 1111111;
const long long mod = 1000000007;
int A[N];
int cnt[N];
bool vis[N];
bitset<N> dp;
int main() {
  int n, k;
  read(n, k);
  for (int i = 1, _ = (n); i <= _; ++i) read(A[i]);
  int odd = 0;
  for (int i = 1, _ = (n); i <= _; ++i) {
    int len = 0;
    for (int j = i; !vis[j]; j = A[j]) len += (vis[j] = true);
    cnt[len]++;
    odd += len % 2;
  }
  for (int i = 1, _ = (n); i <= _; ++i)
    while (cnt[i] > 2) {
      cnt[i * ((cnt[i] + 1) / 2)]++;
      cnt[i] /= 2;
    }
  dp[0] = 1;
  for (int i = 1, _ = (n); i <= _; ++i)
    for (int j = 0, _ = (cnt[i]); j < _; ++j) dp |= dp << i;
  cout << (dp[k] ? k : k + 1) << ' ';
  if (k * 2 <= n - odd)
    cout << k * 2 << endl;
  else
    cout << min(n, k + (n - odd) / 2) << endl;
  return 0;
}
