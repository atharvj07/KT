#include <bits/stdc++.h>
using namespace std;
int main() {
  double x, y;
  cin >> x >> y;
  double r = sqrt(x * x + y * y);
  if (x == 0 || y == 0 || fmod(r, 1) == 0) {
    cout << "black" << endl;
  } else {
    int c_ra = (int)r;
    if ((x * y > 0 && c_ra % 2 == 0) || (x * y < 0 && c_ra % 2 == 1)) {
      cout << "black" << endl;
    } else {
      cout << "white" << endl;
    }
  }
  return 0;
}
