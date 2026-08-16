#include <bits/stdc++.h>
using namespace std;
const int MAXN = (int)5050 * 144;
const char nxtl = '\n';
const int mod = (int)1e9 + 7;
const double eps = (double)1e-7;
template <typename T>
inline bool updmin(T &a, const T &b) {
  return a > b ? a = b, 1 : 0;
}
template <typename T>
inline bool updmax(T &a, const T &b) {
  return a < b ? a = b, 1 : 0;
}
string s;
int cnt[(int)2e5][30];
inline bool check(int mid) {
  int whole = (1 << 26) - 1;
  for (int i = 0; i <= ((int)(s.size())) - mid; ++i) {
    int cur = 0;
    for (int j = 0; j <= 25; ++j) {
      if (cnt[i + mid - 1][j] - (i > 0 ? cnt[i - 1][j] : 0) > 0)
        cur |= (1 << j);
    }
    whole &= cur;
  }
  return whole > 0;
}
int main() {
  srand(time(0));
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> s;
  for (int i = 0; i <= ((int)(s.size())) - 1; ++i) {
    cnt[i][s[i] - 'a']++;
    if (i > 0) {
      for (int j = 0; j <= 25; ++j) cnt[i][j] += cnt[i - 1][j];
    }
  }
  int l = 0, r = ((int)(s.size())) + 1;
  while (r - l > 1) {
    int mid = l + r >> 1;
    if (check(mid))
      r = mid;
    else
      l = mid;
  }
  cout << r << endl;
  return 0;
}
