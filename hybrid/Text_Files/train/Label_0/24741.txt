#include <bits/stdc++.h>
using namespace std;
int main() {
  map<char, char> b;
  b['R'] = 'L';
  b['L'] = 'R';
  b['U'] = 'D';
  b['D'] = 'U';
  char s, p1, p2;
  int n, ans = 0;
  cin >> n;
  if (n == 1) {
    cout << 1;
    return 0;
  }
  int i = 0;
  set<char> a;
  while (i < n) {
    cin >> s;
    if (a.count(b[s]) == 0) {
      a.insert(s);
    } else {
      ans++;
      a.clear();
      a.insert(s);
    }
    i++;
  }
  cout << ans + 1;
  return 0;
}
