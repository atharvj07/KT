#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
const int MAX = 100010;
const double eps = 1e-9;
long long int modexpo(long long int a, long long int b) {
  long long int x = 1, y = a;
  while (b > 0) {
    if (b & 1) x = (x * y) % MOD;
    y = (y * y) % MOD;
    b >>= 1;
  }
  return x;
}
long long int gcd(long long int a, long long int b) {
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}
long long int lcm(long long int a, long long int b) {
  return (a / gcd(a, b)) * b;
}
vector<pair<int, int> > neg, pos;
int main() {
  int x, a, n;
  cin >> n;
  for (int i = 0, _n = (n); i < _n; ++i) {
    cin >> x >> a;
    if (x < 0)
      neg.push_back(make_pair(-x, a));
    else
      pos.push_back(make_pair(x, a));
  }
  sort((pos).begin(), (pos).end());
  sort((neg).begin(), (neg).end());
  long long int ans = 0;
  for (int i = 0, _n = (min((int)(pos).size(), (int)(neg).size())); i < _n;
       ++i) {
    ans += pos[i].second + neg[i].second;
  }
  if ((int)(pos).size() < (int)(neg).size()) {
    ans += neg[(int)(pos).size()].second;
  } else if ((int)(pos).size() > (int)(neg).size()) {
    ans += pos[(int)(neg).size()].second;
  }
  cout << ans << endl;
  return 0;
}
