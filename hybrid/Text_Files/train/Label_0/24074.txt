#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double PI = acos(-1);
const double EPS = 1e-10;
const int N = 1000010;
long long n, d, b;
long long s[N];
long long pref[N];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> n >> d >> b;
  for (int i = 1; i <= n; ++i) {
    cin >> s[i];
    pref[i] = pref[i - 1] + s[i];
  }
  long long low = 0, high = n, res = 0;
  while (low <= high) {
    long long mid = (low + high) / 2;
    long long cnt = 0;
    bool fail = 0;
    for (int i = 1; i <= n; ++i) {
      if (2 * i <= n + 1) {
        if (i > mid) {
          ++cnt;
          if (pref[min(n, i * (d + 1))] < cnt * b) {
            fail = true;
          }
        }
      }
    }
    cnt = 0;
    for (int i = n; i >= 1; --i) {
      if (2 * i <= n + 1) {
        break;
      }
      if (i + mid <= n) {
        ++cnt;
        if (pref[n] - pref[max(0LL, n - (long long)(n - i + 1) * (d + 1))] <
            cnt * b) {
          fail = true;
        }
      }
    }
    if (fail) {
      low = mid + 1;
    } else {
      res = mid;
      high = mid - 1;
    }
  }
  cout << res;
}
