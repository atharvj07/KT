#include <bits/stdc++.h>
using namespace std;
int n, i, j, a[200005];
long long sum[200005];
pair<int, int> t;
vector<int> sol;
long long f(int u) {
  long long sum1 = sum[n - 1] - sum[n - 1 - u];
  long long sum2 = sum[i - 1];
  if (i - 1 - u >= 0) sum2 -= sum[i - 1 - u];
  return sum1 + sum2 + a[i];
}
int main() {
  scanf("%d", &n);
  for (i = 0; i < n; i++) scanf("%d", &a[i]);
  sort(a, a + n);
  for (i = 0; i < n; i++) {
    sum[i] = a[i];
    if (i) sum[i] += sum[i - 1];
  }
  double ans = 0;
  for (i = 0; i < n; i++) {
    int median = a[i];
    int lb = -1;
    int ub = min(i, n - 1 - i);
    while (ub - lb > 1) {
      int mid = (lb + ub) / 2;
      if (f(mid) * (2LL * (mid + 1) + 1) < f(mid + 1) * (2LL * mid + 1))
        lb = mid;
      else
        ub = mid;
    }
    double val = f(lb + 1) * 1.0 / (2LL * (lb + 1) + 1) - median;
    if (ans < val) {
      ans = val;
      t = make_pair(i, lb + 1);
    }
  }
  sol.push_back(a[t.first]);
  for (i = 0; i < t.second; i++) {
    sol.push_back(a[t.first - i - 1]);
    sol.push_back(a[n - 1 - i]);
  }
  printf("%d\n", sol.size());
  for (i = 0; i < sol.size(); i++) {
    if (i == 0)
      printf("%d", sol[i]);
    else
      printf(" %d", sol[i]);
  }
  printf("\n");
}
