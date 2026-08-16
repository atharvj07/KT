#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using lli = long long int;
using ld = long double;
using ull = unsigned long long;
const int N = 2e5 + 5, inf = 2e9;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ll n, arr[N], sum = 1, ans = 0;
  cin >> n;
  vector<ll> two_pow;
  map<int, int> isfound;
  for (int i = 0; i < 40; i++) {
    two_pow.push_back(sum);
    sum *= 2;
  }
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
    for (auto j : two_pow) {
      ans += isfound[j - arr[i]];
    }
    isfound[arr[i]]++;
  }
  cout << ans << "\n";
  return 0;
}
