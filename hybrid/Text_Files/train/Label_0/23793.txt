#include <bits/stdc++.h>
using namespace std;
long long a, b, c, d, e, sum;
int main() {
  cin >> a >> b >> c >> d >> e;
  while (a >= 1 && b >= 1 && c >= 2 && d >= 7 && e >= 4) {
    sum++;
    a -= 1;
    b -= 1;
    c -= 2;
    d -= 7;
    e -= 4;
  }
  cout << sum << endl;
  return 0;
}
