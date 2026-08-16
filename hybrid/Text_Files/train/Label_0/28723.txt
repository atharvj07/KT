#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,sse3,sse4,popcnt,abm,mmx")
const int N = (int)5e5 + 7, inf = (int)1e9 + 7, mod = (int)1e9 + 7;
const long long linf = (long long)1e18 + 7;
const int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1},
          dy[] = {0, 1, 0, -1, 1, -1, 1, -1};
using namespace std;
int n, k;
int a[N];
long long cnk(int x, int y) {
  long long res = 1;
  for (int i = x - y + 1; i <= x; i++) res *= i;
  for (int i = 2; i <= y; i++) res /= i;
  return res;
}
namespace get2 {
long long get(long long x) { return cnk(x, 2) + 1; }
}  // namespace get2
namespace get3 {
long long get(long long x) {
  if (x == 4) return 15;
  long long res = 15;
  for (int i = 4; i < x; i++) {
    res += ((i)*1ll * (i));
  }
  return res;
}
}  // namespace get3
namespace get4 {
long long get(long long x) { return cnk(x, 4) * 9; }
}  // namespace get4
int ans;
void go() {
  int cur = 0;
  for (int i = 1; i <= n; i++) {
    if (a[i] == i) {
      cur++;
    }
  }
  if (cur >= n - k) {
    ans++;
    for (int i = 1; i <= n; i++) {
    }
  }
}
void full() {
  for (int i = 1; i <= n; i++) {
    a[i] = i;
  }
  ans = 0;
  do {
    go();
  } while (next_permutation(a + 1, a + 1 + n));
}
int main() {
  ios_base ::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  ios_base ::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  cin >> n >> k;
  if (k == 1)
    cout << 1;
  else if (k == 2)
    cout << get2 ::get(n);
  else if (k == 3)
    cout << get3 ::get(n);
  else
    cout << get3 ::get(n) + get4 ::get(n);
  exit(0);
}
