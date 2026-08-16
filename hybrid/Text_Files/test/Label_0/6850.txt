#include <bits/stdc++.h>
using namespace std;
long long int n, x, y, sum;
int main() {
  cin >> n >> x >> y;
  if ((x >= n && y >= n) || (x % n == 0 && x != 0) || (y % n == 0 && y != 0)) {
    sum += (int)(x / n);
    sum += (int)(y / n);
    cout << sum << endl;
  } else {
    cout << "-1" << endl;
  }
  return 0;
}
