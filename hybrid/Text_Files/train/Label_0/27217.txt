#include <bits/stdc++.h>
using namespace std;
void IOS() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}
void solve() {
  string str;
  cin >> str;
  long long n = str.length();
  vector<long long> v;
  long long sum = 0;
  for (long long i = 0; i < str.length(); i++) {
    if (str[i] == 'b') {
      if (i + 3 < str.length() && str[i + 1] == 'e' && str[i + 2] == 'a' &&
          str[i + 3] == 'r')
        v.push_back(i);
    }
  }
  for (long long i = 0; i < v.size(); i++) {
    long long end = v[i] + 3;
    long long ct = n - end;
    if (i == 0)
      sum += (v[i] + 1) * ct;
    else
      sum += (v[i] - v[i - 1]) * ct;
  }
  cout << sum;
  cout << endl;
}
int32_t main() {
  IOS();
  long long t = 1;
  while (t--) {
    solve();
  }
  return 0;
}
