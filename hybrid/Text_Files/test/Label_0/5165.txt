#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) {
  if (a)
    return gcd(b % a, a);
  else
    return b;
}
int main() {
  long long a, b;
  cin >> a >> b;
  string s, t;
  cin >> s >> t;
  vector<char> S(s.size(), false);
  long long rans = 0;
  for (long long i = 0; i < s.size() && !S[i]; ++i) {
    long long js = 1, jt = 1;
    vector<long long> in_s(26, 0), in_t(26, 0);
    ++in_s[s[i] - 'a'];
    S[i] = true;
    for (long long j = t.size() % s.size(); j; j = (j + t.size()) % s.size()) {
      ++in_s[s[(i + j) % s.size()] - 'a'];
      S[(i + j) % s.size()] = true;
      ++js;
    }
    ++in_t[t[i] - 'a'];
    for (long long j = s.size() % t.size(); j; j = (j + s.size()) % t.size()) {
      ++in_t[t[(i + j) % t.size()] - 'a'];
      ++jt;
    }
    long long ans = js * jt;
    for (int j = 0; j < 26; ++j) ans -= in_s[j] * in_t[j];
    rans += ans;
  }
  cout << rans * (a / (t.size() / gcd(s.size(), t.size())));
  return 0;
}
