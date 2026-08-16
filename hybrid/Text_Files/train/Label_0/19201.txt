#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 10;
int n, m, k;
string s;
bool check(const string& s, int j) {
  return (j > 0 && s[j - 1] + 1 == s[j]) || (j < n - 1 && s[j + 1] + 1 == s[j]);
}
void solve() {
  for (int i = 25; i >= 0; i--) {
    for (int k = 0; k < n + 20; k++) {
      for (int j = 0; j < n; j++) {
        if (s[j] - 'a' == i && check(s, j)) {
          s.erase(s.begin() + j);
        }
      }
    }
  }
  cout << n - s.length();
}
void getData() { cin >> n >> s; }
void preprocessing() {}
int main() {
  int t = 1;
  for (int i = 1; i <= t; i++) {
    getData();
    preprocessing();
    solve();
  }
  return 0;
}
