#include <bits/stdc++.h>
using namespace std;
int main() {
  int t, n;
  int x;
  cin >> t;
  while (t--) {
    cin >> n;
    map<int, int> m;
    for (int i = 0; i < n; i++) {
      cin >> x;
      m[x] = 1;
    }
    cout << m.size() << endl;
  }
}
