#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int c[n + 1], e[n - 1][2];
  for (int i = 0; i < n - 1; ++i) {
    cin >> e[i][0] >> e[i][1];
  }
  for (int i = 1; i <= n; ++i) {
    cin >> c[i];
  }
  vector<int> e1;
  vector<int> e2;
  for (int i = 0; i < n - 1; ++i) {
    if (c[e[i][1]] != c[e[i][0]]) {
      e1.push_back(e[i][1]);
      e2.push_back(e[i][0]);
    }
  }
  bool k = true;
  int v = 1;
  if (n > 2 && e1.size() > 1) {
    if (e1[0] == e1[1] || e1[0] == e2[1]) {
      v = e1[0];
    } else if (e2[0] == e1[1] || e2[0] == e2[1]) {
      v = e2[0];
    } else {
      k = false;
    }
    for (int i = 1; i < e1.size(); ++i) {
      if (e1[i] != v && e2[i] != v) {
        k = false;
        break;
      }
    }
  }
  if (e1.size() == 1) v = e1[0];
  if (k || n < 3)
    cout << "YES"
         << "\n"
         << v;
  else
    cout << "NO";
  return 0;
}
