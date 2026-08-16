#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-11;
int t;
double a, b;
int main() {
  cin >> t;
  while (t--) {
    scanf("%lf%lf", &a, &b);
    if (b == 0)
      printf("1\n");
    else if (4 * b >= a) {
      printf("%.10f\n", 0.5 + a / (b * 16.0));
    } else
      printf("%.10f\n", 1 - 1.0 * b / (a));
  }
  return 0;
}
