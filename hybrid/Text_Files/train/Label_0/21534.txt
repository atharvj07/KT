#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  ;
  string s;
  cin >> s;
  long long k;
  cin >> k;
  long long cnt = 0;
  for (long long i = 0; i < k; i++) {
    string t;
    cin >> t;
    long long m1 = 0, m2 = 0;
    for (long long i = 0; i < s.length(); i++) {
      if (t[0] == s[i]) {
        m1++;
      } else if (t[1] == s[i]) {
        m2++;
      } else {
        cnt += min(m1, m2);
        m1 = 0;
        m2 = 0;
      }
    }
    cnt += min(m1, m2);
  }
  cout << cnt << '\n';
  return 0;
}
