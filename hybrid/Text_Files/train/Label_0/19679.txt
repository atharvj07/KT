#include <bits/stdc++.h>
using namespace std;
long long n;
vector<long long> v;
long long solve(long long x) {
  long long sol = 0, cnt = 0;
  for (long long i = 0; i < n - 1; i++) {
    cnt += v[i];
    sol += min(cnt % x, x - cnt % x);
  }
  return sol;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long a, summ = 0, sol = LLONG_MAX;
  cin >> n;
  for (long long i = 0; i < n; i++) {
    cin >> a;
    summ += a;
    v.push_back(a);
  }
  for (long long i = 2; i * i <= summ; i++) {
    if (summ % i) continue;
    sol = min(sol, solve(i));
    while (summ % i == 0) summ /= i;
  }
  if (summ > 1) sol = min(sol, solve(summ));
  if (sol == LLONG_MAX) sol = -1;
  cout << sol << "\n";
  return 0;
}
