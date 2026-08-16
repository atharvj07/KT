#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int xi;
  set<int> sw;
  for (int i = 0; i < n; i++) {
    cin >> xi;
    int yij;
    for (int j = 0; j < xi; j++) {
      cin >> yij;
      sw.insert(yij);
    }
  }
  if (sw.size() == m)
    cout << "YES";
  else
    cout << "NO";
  return 0;
}
