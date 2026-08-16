#include <bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
inline int getint() {
  int x;
  scanf("%d", &x);
  return x;
}
inline long long getlng() {
  long long x;
  scanf("%lld", &x);
  return x;
}
int dx4[] = {-1, 0, 1, 0};
int dy4[] = {0, 1, 0, -1};
int dx8[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy8[] = {-1, 0, 1, -1, 1, -1, 0, 1};
const double eps = (double)1e-9;
int main() {
  int ans = 1, curr = 1;
  int n = getint();
  for (int i = 0; i < n; ++i) {
    int s = getint(), d = getint();
    for (long long j = 0;; ++j) {
      if ((long long)s + j * (long long)d >= ans) {
        ans = (long long)s + j * (long long)d;
        break;
      }
    }
    ans++;
  }
  cout << ans - 1;
  return 0;
}
