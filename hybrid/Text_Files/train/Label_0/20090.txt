#include <bits/stdc++.h>
using namespace std;
int main() {
  long long a, b, x;
  cin >> a >> b >> x;
  long long gr = 1, sm = 0;
  if (a > b) gr = 0, sm = 1, swap(a, b);
  long long ct = 0;
  while (x > 1 && a > 0 && b > 0) {
    if (ct % 2)
      a--, cout << sm;
    else
      b--, cout << gr;
    ct++;
    x--;
  }
  if (ct % 2 == 0) {
    while (b > 0) b--, cout << gr;
    while (a > 0) a--, cout << sm;
  } else {
    while (a > 0) a--, cout << sm;
    while (b > 0) b--, cout << gr;
  }
  return 0;
}
