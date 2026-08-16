#include <bits/stdc++.h>
using namespace std;
long long int sqr(long long int x) { return x * x; }
inline long long int add(long long int a, long long int b) {
  long long int c = a + b;
  if (c >= 1000000007) c -= 1000000007;
  return c;
}
inline long long int mul(long long int a, long long int b) {
  return (a * 1ll * b) % 1000000007;
}
inline long long int sub(long long int a, long long int b) {
  long long int c = a - b;
  if (c < 0) c += 1000000007;
  return c;
}
const long long int nax = 300 * 1000 + 10;
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int t;
  cin >> t;
  while (t--) {
    long long int n;
    cin >> n;
    vector<long long int> a(n);
    for (long long int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    vector<long long int> b(n);
    for (long long int i = 0; i < n; ++i) {
      cin >> b[i];
    }
    vector<long long int> use;
    for (long long int i = 0; i < n; ++i) {
      if (b[i] == 0) {
        use.push_back(a[i]);
      }
    }
    sort(use.begin(), use.end());
    for (long long int i = 0; i < n; ++i) {
      if (b[i] == 0) {
        a[i] = use.back();
        use.pop_back();
      }
    }
    for (long long int i = 0; i < a.size(); ++i) cout << a[i] << " ";
    cout << "\n";
  }
  return 0;
}
