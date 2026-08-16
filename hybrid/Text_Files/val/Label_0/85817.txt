#include <bits/stdc++.h>
using namespace std;
const int MAXN = 18;
int n, r;
double sum;
double a[(1 << MAXN) + 1];
int main(void) {
  scanf("%d%d", &n, &r);
  for (int i = 0; i < 1 << n; ++i) {
    scanf("%lf", &a[i]);
    sum += a[i];
  }
  printf("%.8lf\n", sum / (1 << n));
  for (int i = 0; i < r; ++i) {
    int z;
    double g;
    scanf("%d%lf", &z, &g);
    sum += g - a[z];
    a[z] = g;
    printf("%.8lf\n", sum / (1 << n));
  }
  return 0;
}
