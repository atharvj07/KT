#include <bits/stdc++.h>
long long int i, j;
using namespace std;
int main() {
  int a, b, c, n, n1, n2, n3, x;
  cin >> a >> b >> c >> n;
  n1 = a - c;
  n2 = b - c;
  n3 = c;
  x = n - n1 - n2 - n3;
  if (n1 >= 0 && n2 >= 0 && n3 >= 0 && x > 0) {
    cout << x << endl;
  } else
    cout << -1;
  return 0;
}
