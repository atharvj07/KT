#include <bits/stdc++.h>
using namespace std;
long long mas1[100000], mas2[100000];
int main() {
  int n;
  long long p;
  cin >> n >> p;
  long long sumc = 0, sumz = 0;
  for (int i = 0; i < n; ++i) {
    cin >> mas1[i] >> mas2[i];
    sumc += mas1[i];
    sumz += mas2[i];
  }
  if (sumc <= p) {
    cout << -1 << endl;
    return 0;
  }
  double mintime = 0, maxtime = 1e14;
  for (int i = 0; i < 100; ++i) {
    double m = (maxtime + mintime) / 2;
    double totalNeed = 0;
    for (int j = 0; j < n; ++j) {
      totalNeed += max(0., mas1[j] * 1.0 * m - mas2[j]);
    }
    if (totalNeed > m * p) {
      maxtime = m;
    } else {
      mintime = m;
    }
  }
  printf("%.6lf\n", mintime);
  return 0;
}
