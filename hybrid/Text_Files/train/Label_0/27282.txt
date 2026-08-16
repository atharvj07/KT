#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
  ll n, k;
  cin >> n >> k;
  vector<int> id(n);
  for (int& v : id) cin >> v;
  ll s = 1;
  ll i = 1;
  while (s < k) {
    i++;
    s += i;
  }
  i--;
  k -= (i * (i + 1)) / 2;
  cout << id[k - 1] << '\n';
}
