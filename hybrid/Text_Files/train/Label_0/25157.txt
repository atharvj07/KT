#include <bits/stdc++.h>
using namespace std;
double absolute(int a, int b) {
  cout << setprecision(20);
  return sqrt(a * a + b * b);
}
int main() {
  int n, k;
  cin >> n >> k;
  int a, b, pa = 0, pb = 0;
  double len = 0;
  for (size_t i = 0; i < n; i++) {
    cin >> a >> b;
    if (i != 0) len += absolute(abs(a - pa), abs(b - pb));
    pa = a;
    pb = b;
  }
  cout << (len * k) / 50;
}
