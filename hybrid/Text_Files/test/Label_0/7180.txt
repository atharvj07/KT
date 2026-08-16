#include <bits/stdc++.h>
using namespace std;
int binsearch(int x, vector<int> vec) {
  int k = 0;
  for (int b = vec.size() / 2; b >= 1; b /= 2)
    while (k + b < vec.size() && vec[k + b] <= x) k += b;
  if (vec[k] == x) return 1;
  return 0;
}
int is_good_case01(string s, int from, int to) {
  while (from <= to && s[from] == '0') from++;
  while (from <= to) {
    if (s[from] == '0') return 0;
    from++;
  }
  return 1;
}
int is_good_case10(string s, int from, int to) {
  while (from <= to && s[from] == '1') from++;
  while (from <= to) {
    if (s[from] == '1') return 0;
    from++;
  }
  return 1;
}
int main() {
  ios_base::sync_with_stdio(0);
  cout.tie(0);
  iostream::sync_with_stdio(0);
  cin.tie(0);
  int test, ans, total1, total0, done1, done0, n;
  string s;
  cin >> test;
  while (test--) {
    cin >> s;
    n = s.length();
    ans = 10e8;
    total0 = total1 = done0 = done1 = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '1')
        total1++;
      else
        total0++;
    }
    for (int i = 0; i < n; i++) {
      ans = min(ans, (done0 + total1 - done1));
      ans = min(ans, (done1 + total0 - done0));
      if (s[i] == '1')
        done1++;
      else
        done0++;
    }
    cout << ans << "\n";
  }
  return 0;
}
