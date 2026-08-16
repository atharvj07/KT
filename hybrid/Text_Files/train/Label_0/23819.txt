#include <bits/stdc++.h>
using namespace std;
int gcd(int a, int b) {
  if (a < b) swap(a, b);
  if (b == 0)
    return a;
  else
    return gcd(b, a % b);
}
int main() {
  int a, b, c;
  string s1, s2, s3, s4;
  cin >> s1 >> s2;
  a = ((int)s1.size()), b = ((int)s2.size());
  c = gcd(a, b);
  bool f = 1;
  s3 = s1.substr(0, c);
  for (int i = 0; i < a / c && f; i++) {
    s4 = s1.substr(i * c, c);
    if (s3 != s4) f = 0;
  }
  for (int i = 0; i < b / c && f; i++) {
    s4 = s2.substr(i * c, c);
    if (s3 != s4) f = 0;
  }
  if (!f) {
    cout << 0 << endl;
    return 0;
  }
  int ans = 1;
  priority_queue<int> q;
  map<int, int> mp;
  for (int i = 1; i * i <= c; i++)
    if (c % i == 0) q.push(i), q.push(c / i), mp[i] = c, mp[c / i] = c;
  mp[c] = -1;
  while (!q.empty()) {
    c = q.top(), q.pop();
    if (mp[c] == -1) continue;
    s3 = s1.substr(0, c);
    bool f = 1;
    for (int i = 0; i < mp[c] / c; i++) {
      s4 = s1.substr(i * c, c);
      if (s3 != s4) f = 0;
    }
    if (f) {
      ans++;
      for (int i = 1; i * i <= c; i++) {
        if (c % i == 0) {
          if (!mp[i]) mp[i] = c, q.push(i);
          if (!mp[c / i]) mp[c / i] = c, q.push(c / i);
          mp[i] = min(mp[i], c), mp[c / i] = min(mp[c / i], c);
        }
      }
    } else {
      for (int i = 1; i * i <= c; i++) {
        if (c % i == 0) mp[i] = -1, mp[c / i] = -1;
      }
    }
    mp[c] = -1;
  }
  cout << ans << endl;
}
