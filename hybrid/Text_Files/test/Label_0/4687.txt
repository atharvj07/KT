#include <bits/stdc++.h>
using namespace std;
const int maxx = 5000;
int a[2222], n;
double b[11111], d[11111];
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  sort(a, a + n);
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      b[a[j] - a[i]] += 1.0;
    }
  }
  for (int i = 0; i <= maxx; i++) {
    for (int j = i + 1; j <= maxx; j++) {
      d[i + j] += 2.0 * b[i] * b[j];
    }
    d[i + i] += b[i] * b[i];
  }
  double sum = 0.0;
  for (int i = 0; i <= maxx * 2; i++) {
    sum += d[i];
    d[i] = sum;
  }
  double res = 0.0;
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      res += d[a[j] - a[i] - 1];
    }
  }
  res *= 8;
  res /= 1.0 * n * n * n;
  res /= 1.0 * (n - 1) * (n - 1) * (n - 1);
  printf("%.10lf\n", res);
  return 0;
}
