#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
pair<int, int> a[N];
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n, k;
  cin >> n >> k;
  long long num = -1, temp = 1e18, ans = 0;
  for (int i = 0; i < k; ++i) {
    long long x;
    cin >> x;
    if ((n % x) < temp) {
      num = i;
      ans = n / x;
      temp = n % x;
    }
  }
  cout << num + 1 << " " << ans;
  return 0;
}
