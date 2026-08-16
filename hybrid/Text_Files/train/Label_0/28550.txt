#include <bits/stdc++.h>
using namespace std;
const int N = 755;
int n, Q, cnt;
long long a[N], b[N];
priority_queue<long long> q;
int main() {
  scanf("%d%d", &n, &Q);
  for (int i = 1; i <= n; ++i) scanf("%lld", a + i);
  for (int i = n; i; --i)
    if (a[i] < 0)
      q.push(a[i]);
    else if (a[i] > 0) {
      while (!q.empty() && a[i] > 0) a[i] += q.top(), q.pop();
      if (a[i] < 0) q.push(a[i]);
    }
  while (!q.empty()) b[++cnt] = q.top(), q.pop(), b[cnt] = -b[cnt] + b[cnt - 1];
  while (Q--) {
    long long x;
    scanf("%lld", &x);
    cout << cnt - (upper_bound(b + 1, b + cnt + 1, x) - b - 1) << endl;
  }
  return 0;
}
