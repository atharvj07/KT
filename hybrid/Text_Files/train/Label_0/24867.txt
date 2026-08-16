#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T bigmod(T p, T e, T M) {
  if (e == 0) return 1;
  if (e % 2 == 0) {
    T t = bigmod(p, e / 2, M);
    return (t * t) % M;
  }
  return (bigmod(p, e - 1, M) * p) % M;
}
template <class T>
inline T gcd(T a, T b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
template <class T>
inline T modinverse(T a, T M) {
  return bigmod(a, M - 2, M);
}
pair<int, int> arr[1000009];
int main() {
  int i, j, k;
  string str, inp;
  int cases = 1;
  int a, u, v, m, n;
  cin >> n >> m;
  for (i = 0; i < m; i++) {
    cin >> arr[i].second >> arr[i].first;
  }
  sort(arr, arr + m);
  reverse(arr, arr + m);
  int st = 1, ed = m;
  long long mid, ans;
  while (st <= ed) {
    mid = (st + ed) / 2;
    long long tot = mid * (mid - 1) / 2;
    if (mid % 2)
      tot++;
    else
      tot += mid / 2;
    if (tot <= n) {
      st = mid + 1;
      ans = mid;
    } else
      ed = mid - 1;
  }
  long long sum = 0ll;
  for (i = 0; i < ans; i++) sum += arr[i].first;
  cout << sum << endl;
  return 0;
}
