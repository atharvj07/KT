#include <bits/stdc++.h>
using namespace std;
template <class _T>
inline _T sqr(const _T& x) {
  return x * x;
}
template <class _T>
inline string tostr(const _T& a) {
  ostringstream os("");
  os << a;
  return os.str();
}
const long double PI = 3.1415926535897932384626433832795;
const long double EPS = 1e-11;
int n;
int a[1024];
int main() {
  cout << setiosflags(ios::fixed) << setprecision(10);
  scanf("%d", &n);
  for (int i = 0; i < (int)(n); i++) {
    scanf("%d", a + i);
  }
  if (n < 3) {
    puts("-1");
    return 0;
  }
  reverse(a, a + n);
  const int INF = 2100000000;
  int ans = INF;
  for (int i = (2); i <= (int)(n - 1); i++) {
    for (int j = (1); j <= (int)(i - 1); j++) {
      int t = a[i] - 1;
      int cnt = 0;
      for (int k = (n - 1); k >= (int)(j); k--) {
        cnt += t / a[k];
        t %= a[k];
      }
      int x = a[i] + a[j] - t - 1;
      if (x > ans) continue;
      int y = x;
      for (int k = (n)-1; k >= 0; k--) {
        cnt -= y / a[k];
        y %= a[k];
      }
      cnt++;
      if (cnt < 0) {
        ans = x;
      }
    }
  }
  if (ans == INF)
    puts("-1");
  else
    cout << ans << endl;
  return 0;
}
