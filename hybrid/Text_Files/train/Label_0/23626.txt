#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, a, b, c, num = 0;
  while (cin >> n >> a >> b >> c) {
    for (int i = 0; i <= a; i++) {
      for (int j = 0; j <= b; j++) {
        if ((n - i / 2 - j) >= 0 && ((n - i / 2 - j) / 2) <= c &&
            (2 * n - i - 2 * j) % 4 == 0) {
          num++;
        }
      }
    }
    cout << num << endl;
    num = 0;
  }
}
