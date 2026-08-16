#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int two = 0, three = 0;
    while (n % 2 == 0) two++, n /= 2;
    while (n % 3 == 0) three++, n /= 3;
    if (n != 1 || two > three)
      cout << -1 << endl;
    else {
      cout << 2 * three - two << endl;
    }
  }
}
