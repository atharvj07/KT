#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  int a = s.length();
  int i = 0;
  if (a % 2 == 0) {
    cout << a / 2;
  } else {
    int count = 0, z = 0;
    for (i = 1; i <= 99; i += 2) {
      z++;
      if (a == i) {
        for (int j = 1; j < a; j++) {
          if (s[j] == '0') {
            count++;
          }
        }
        if (count == a - 1) {
          cout << z - 1;
          break;
        } else {
          cout << z;
          break;
        }
      }
    }
  }
  return 0;
}
