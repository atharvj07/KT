#include <bits/stdc++.h>
typedef long long ll;
typedef long double ld;
using namespace std;
vector<ll> prime_factors(ll num) {
  vector<ll> ans;
  while (num % 2) {
    ans.push_back(2);
    num /= 2;
  }
  for (int i = 3; i * i <= num; i += 2) {
    while (num % i == 0) {
      ans.push_back(i);
      num /= i;
    }
  }
  if (num > 2) ans.push_back(num);
  return ans;
}
const ld pi = 3.14159265358979323846;
void tests() {
  int n, k;
  cin >> n >> k;
  vector<int> arr(n);
  for (auto &_ : arr) cin >> _;
  int sum = 0;
  pair<int, int> ans;
  for (int i = 0; i < k; ++i) {
    sum += arr[i];
  }
  ans = make_pair(sum, 0);
  for (int i = 0, j = k; j < n; ++i, ++j) {
    sum -= arr[i];
    sum += arr[j];
    if (sum < ans.first) ans.first = sum, ans.second = i + 1;
  }
  cout << ans.second + 1 << char(10);
}
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t = 1;
  while (t--) {
    tests();
  }
  return 0;
}
