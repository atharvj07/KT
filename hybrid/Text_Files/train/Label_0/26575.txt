#include <bits/stdc++.h>
using namespace std;
int main() {
  long long a, b, c, x;
  cin >> a >> b >> c;
  x = c * -1;
  if (c == 0) {
    if (a == b)
      cout << "YES";
    else
      cout << "NO";
  } else if (c > 0) {
    if (b < a)
      cout << "NO";
    else {
      if ((b - a) % c == 0)
        cout << "YES";
      else
        cout << "NO";
    }
  } else if (c < 0) {
    if (a < b)
      cout << "NO";
    else {
      if ((a - b) % x == 0)
        cout << "YES";
      else
        cout << "NO";
    }
  }
}
