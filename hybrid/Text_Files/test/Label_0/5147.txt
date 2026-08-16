#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long int t;
  cin >> t;
  while (t--) {
    long long int a, b;
    cin >> a >> b;
    if (a == b) {
      cout << "0\n";
      continue;
    }
    if (a < b) {
      long long int temp = a;
      a = b;
      b = temp;
    }
    long long int c = 0, f = 1;
    while (a % 8 == 0 && f == 1 && a / 8 >= b) {
      if (a == b && f == 1) {
        cout << c << endl;
        f = 0;
        break;
      }
      a /= 8;
      ++c;
    }
    if (a == b && f == 1) {
      cout << c << endl;
      f = 0;
    }
    while (a % 4 == 0 && f == 1 && a / 4 >= b) {
      if (a == b && f == 1) {
        cout << c << endl;
        f = 0;
        break;
      }
      a /= 4;
      ++c;
    }
    if (a == b && f == 1) {
      cout << c << endl;
      f = 0;
    }
    while (a % 2 == 0 && f == 1 && a / 2 >= b) {
      if (a == b && f == 1) {
        cout << c << endl;
        f = 0;
        break;
      }
      a /= 2;
      ++c;
    }
    if (a == b && f == 1) {
      cout << c << endl;
      f = 0;
    }
    if (f == 1) cout << "-1\n";
  }
}
