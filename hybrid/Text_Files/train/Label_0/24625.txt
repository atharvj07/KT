#include <bits/stdc++.h>
using namespace std;
const int INF = 1 << 30;
int main() {
  int n, m;
  while (cin >> n >> m) {
    map<int, int> x, y;
    for (int i = 0; i < n; ++i) {
      string s;
      cin >> s;
      for (int j = 0; j < m; ++j) {
        if (s[j] == '*') {
          ++x[j + 1];
          ++y[i + 1];
        }
      }
    }
    int px, py;
    for (map<int, int>::iterator it = x.begin(); it != x.end(); ++it) {
      if (it->second == 1) px = it->first;
    }
    for (map<int, int>::iterator it = y.begin(); it != y.end(); ++it) {
      if (it->second == 1) py = it->first;
    }
    cout << py << " " << px << endl;
  }
  return 0;
}
