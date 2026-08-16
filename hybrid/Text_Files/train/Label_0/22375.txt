#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline void ckmax(T& x, T y) {
  x = (y > x ? y : x);
}
template <typename T>
inline void ckmin(T& x, T y) {
  x = (y < x ? y : x);
}
const int MAXN = 2e5;
const int INF = 1e9;
const int BOUND = 448;
int n, mxa, a[MAXN + 5];
int cnt[MAXN + 5], mp[MAXN * 2 + 5];
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i];
    ckmax(mxa, a[i]);
    cnt[a[i]]++;
  }
  int mx = 0, semx = 0;
  for (int i = 1; i <= mxa; ++i) {
    if (cnt[i] > cnt[mx]) {
      semx = mx;
      mx = i;
    } else if (cnt[i] > cnt[semx]) {
      semx = i;
    }
  }
  if (!semx) {
    cout << 0 << endl;
    return 0;
  }
  if (cnt[semx] == cnt[mx]) {
    cout << n << endl;
    return 0;
  }
  int ans = 0;
  for (int v = 1; v <= mxa; ++v) {
    if (v == mx) continue;
    if (cnt[v] <= BOUND) continue;
    for (int i = 0; i <= n * 2; ++i) {
      mp[i] = INF;
    }
    mp[n] = 0;
    int presum = 0;
    for (int i = 1; i <= n; ++i) {
      int x = 0;
      if (a[i] == mx)
        x = 1;
      else if (a[i] == v)
        x = -1;
      presum += x;
      ckmax(ans, i - mp[presum + n]);
      ckmin(mp[presum + n], i);
    }
  }
  for (int frq = 1; frq <= BOUND; ++frq) {
    for (int i = 1; i <= mxa; ++i) {
      cnt[i] = 0;
    }
    for (int i = 1; i <= n; ++i) {
      mp[i] = 0;
    }
    int l = 1;
    for (int r = 1; r <= n; ++r) {
      mp[cnt[a[r]]]--;
      cnt[a[r]]++;
      mp[cnt[a[r]]]++;
      while (cnt[a[r]] > frq) {
        mp[cnt[a[l]]]--;
        cnt[a[l]]--;
        mp[cnt[a[l]]]++;
        ++l;
      }
      if (mp[frq] >= 2) {
        ckmax(ans, r - l + 1);
      }
    }
  }
  cout << ans << endl;
  return 0;
}
