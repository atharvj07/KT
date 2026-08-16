#include <bits/stdc++.h>
#pragma GCC optimize("O3")
using namespace std;
struct custom_hash {
  static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
  }
  size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM =
        chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
  }
};
int main(int argc, char** argv) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long q;
  cin >> q;
  while (q--) {
    long long n, k, d;
    cin >> n >> k >> d;
    unordered_map<long long, long long, custom_hash> m;
    long long a[n];
    for (long long i = 0, max_i = n; i < max_i; ++i) cin >> a[i];
    long long ans = 0, temp = 0;
    for (long long i = 0, max_i = d; i < max_i; ++i) {
      auto it = m.find(a[i]);
      if (it == m.end() || !it->second) {
        ++temp;
        m[a[i]] = 1;
      } else
        ++it->second;
    }
    ans = temp;
    for (long long i = d, max_i = n; i < max_i; ++i) {
      auto it = m.find(a[i]);
      if (it == m.end() || !it->second) {
        ++temp;
        m[a[i]] = 1;
      } else
        ++it->second;
      if (!(--m[a[i - d]])) --temp;
      ans = min(temp, ans);
    }
    cout << ans << "\n";
  }
}
