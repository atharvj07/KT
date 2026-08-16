#include <bits/stdc++.h>
using namespace std;
int main() {
  int x, y;
  cin >> x >> y;
  int vasat = (x + y) / 2;
  x = abs(vasat - x);
  y = abs(y - vasat);
  cout << (y * (y + 1)) / 2 + (x * (x + 1)) / 2;
}
