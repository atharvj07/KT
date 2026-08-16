#include <bits/stdc++.h>
using namespace std;
string its(long long x) {
  string s;
  while (x >= 1) s.push_back(x % 10 + 48), x = x / 10;
  reverse(s.begin(), s.end());
  return s;
}
int32_t main() {
  string t;
  for (long long i = 1; i < 1000; i++) {
    string s = its(i);
    t += s;
  }
  long long k;
  cin >> k;
  k--;
  cout << t[k];
}
