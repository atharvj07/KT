#include <bits/stdc++.h>
using namespace std;
void run() {
  int n;
  string a, b, c;
  map<string, int> m;
  m["void"] = 0;
  cin >> n;
  for (int it = 0; it < n; it++) {
    cin >> a >> b;
    int x = 0, y = 0;
    while (*b.rbegin() == '*') x++, b.erase(b.end() - 1);
    while (*b.begin() == '&') y++, b.erase(b.begin());
    if (a == "typedef") {
      cin >> c;
      if (!m.count(b) || m[b] == -1)
        m[c] = -1;
      else if (m[b] + x - y >= 0)
        m[c] = m[b] + x - y;
      else
        m[c] = -1;
    } else {
      if (!m.count(b) || m[b] == -1 || m[b] + x - y < 0)
        cout << "errtype" << endl;
      else {
        cout << "void";
        for (int i = 0; i < m[b] + x - y; i++) cout << "*";
        cout << endl;
      }
    }
  }
}
int main() {
  run();
  return 0;
}
