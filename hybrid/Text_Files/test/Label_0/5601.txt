#include <bits/stdc++.h>
using namespace std;
const long long N = 2e5 + 10;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  string s, s1;
  cin >> s >> s1;
  reverse(s.begin(), s.end());
  reverse(s1.begin(), s1.end());
  s1.resize(N + 5, '0');
  s.resize(N + 5, '0');
  for (long long i = N - 1; i > 0; --i) {
    while (s[i] == '1' && s[i - 1] == '1') {
      s[i] = '0';
      s[i - 1] = '0';
      s[i + 1] = '1';
      i += 2;
    }
  }
  for (long long i = N - 1; i > 0; --i) {
    while (s1[i] == '1' && s1[i - 1] == '1') {
      s1[i] = '0';
      s1[i - 1] = '0';
      s1[i + 1] = '1';
      i += 2;
    }
  }
  reverse(s1.begin(), s1.end());
  reverse(s.begin(), s.end());
  if (s == s1)
    cout << "=";
  else if (s > s1)
    cout << ">";
  else
    cout << "<";
}
