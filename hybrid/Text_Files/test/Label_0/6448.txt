#include <bits/stdc++.h>
using namespace std;
int n;
double k, b;
set<long double> a;
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%lf%lf", &k, &b);
    if (k != 0) a.insert(b / k);
  }
  printf("%d\n", a.size());
  return 0;
}
