#include <bits/stdc++.h>
using namespace std;
map<string, int> h;
int n;
string m[1000 + 10];
int main() {
  cin >> n;
  int ans = 0;
  string anss;
  for (int i = 1; i <= n; i++) {
    cin >> m[i], h[m[i]]++;
    if (h[m[i]] > ans) {
      ans = h[m[i]];
      anss = m[i];
    }
  }
  cout << anss;
  return 0;
}
