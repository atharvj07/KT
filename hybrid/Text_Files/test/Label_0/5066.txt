#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, a, b, c;
  cin >> n >> a >> b >> c;
  int i, j;
  j = n % 4;
  if (j == 1) {
    cout << min(min(3 * a, b + a), c);
  } else if (j == 2) {
    cout << min(min(2 * a, b), 2 * c) << endl;
  } else if (j == 3) {
    cout << min(min(a, 3 * c), b + c) << endl;
  } else {
    cout << 0 << endl;
  }
  return 0;
}
