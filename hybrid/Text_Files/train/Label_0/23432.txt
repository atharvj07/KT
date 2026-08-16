#include <bits/stdc++.h>
using namespace std;
double a[100001];
int n;
double k;
int isbalance(double val) {
  double inc = 0.0;
  double dec = 0.0;
  for (int i = 0; i < n; i++)
    if (a[i] > val)
      dec += (a[i] - val);
    else
      inc += (val - a[i]);
  dec -= dec * (k / 100.0);
  if (dec >= inc)
    return 0;
  else
    return 1;
}
int main() {
  cin >> n >> k;
  for (int i = 0; i < n; i++) cin >> a[i];
  double l = 0, r = 1000;
  double ans = 0;
  while (r - l > 1e-7) {
    double mid = (l + r) / 2.0;
    int cho = isbalance(mid);
    if (cho == 0)
      ans = mid, l = mid;
    else
      r = mid;
  }
  cout << fixed << setprecision(7) << l << endl;
  return 0;
}
