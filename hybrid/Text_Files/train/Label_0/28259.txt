#include <bits/stdc++.h>
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
struct hash_pair {
  template <class T1, class T2>
  size_t operator()(const pair<T1, T2>& p) const {
    auto hash1 = hash<T1>{}(p.first);
    auto hash2 = hash<T2>{}(p.second);
    return hash1 ^ hash2;
  }
};
struct comp {
  bool operator()(pair<pair<long long, long long>, long long> a,
                  pair<pair<long long, long long>, long long> b) {
    if (a.second == b.second) return a.first.first < b.first.first;
    return a.second > b.second;
  }
};
long long fb(long long n) {
  if (n == 0) return 0;
  n |= n >> 1;
  n |= n >> 2;
  n |= n >> 4;
  n |= n >> 8;
  n |= n >> 16;
  n = n + 1;
  return (n >> 1);
}
void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) {
  cerr << ' ' << H;
  dbg_out(T...);
}
long long M = 1e9 + 7;
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  auto StArT = chrono::high_resolution_clock::now();
  {
    long long n;
    cin >> n;
    vector<long long> a(n);
    for (long long i = 0; i < n; i++) cin >> a[i];
    long long j = 0;
    while (a[j] <= a[j + 1] && j < n - 1) j++;
    if (j == n - 1) {
      cout << '0';
      return 0;
    } else {
      long long j1 = j;
      j++;
      while (a[j] <= a[j + 1] && j < n - 1) j++;
      if (j == n - 1 && a[n - 1] <= a[0])
        cout << n - j1 - 1;
      else {
        cout << "-1";
        return 0;
      }
    }
  }
  auto eNd = chrono::high_resolution_clock::now();
  double time__taken =
      chrono::duration_cast<chrono::nanoseconds>(eNd - StArT).count();
  time__taken *= 1e-9;
  cerr << "Time taken by program is : " << fixed << time__taken
       << setprecision(9);
  cerr << " sec" << endl;
}
