#include <bits/stdc++.h>
using namespace std;
int main() {
  long long t, x, y;
  cin >> t;
  while (t--) {
    cin >> x >> y;
    if (x - y > 1) {
      cout << "yEs" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
