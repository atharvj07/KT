#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int max = -10000001;
  int a;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (a < 0) {
      if (a > max) {
        max = a;
      }
    } else {
      int root = sqrt(a);
      if (root * root != a) {
        if (a > max) {
          max = a;
        }
      }
    }
  }
  cout << max << "\n";
  return 0;
}
