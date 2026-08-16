#include <bits/stdc++.h>
using namespace std;
using lli = long long int;
using pii = pair<int, int>;
using vi = vector<int>;
using vb = vector<bool>;
using vvi = vector<vector<int>>;
using vlli = vector<long long int>;
using vpii = vector<pair<int, int>>;
lli fast_exp(lli base, lli exp) {
  lli res = 1;
  while (exp > 0) {
    if (exp % 2 == 1) res = (res * base) % 1000000007;
    base = (base * base) % 1000000007;
    exp /= 2;
  }
  return res % 1000000007;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  lli x, k, ans;
  cin >> x >> k;
  if (!x)
    cout << 0;
  else
    cout << ((fast_exp(2, k + 1) * (x % 1000000007)) % 1000000007 -
             fast_exp(2, k) + 1 + 1000000007) %
                1000000007;
}
