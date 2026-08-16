#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 7;
int data[N << 1];
int main() {
  int n, L, t;
  scanf("%d%d%d", &n, &L, &t);
  t <<= 1;
  for (int i = (0); i < (n); ++i) scanf("%d", &data[i]);
  double ans = 0;
  for (int l = 0, r = n, i = 0; i < n; i++, l++, r++) {
    ans += 0.5 * (t / L) * (n - 1);
    int now1 = upper_bound(data + l, data + r, data[i] + t % L) - data;
    ans += 0.25 * (now1 - l - 1);
    int now2 = lower_bound(data + l, data + r, data[i] + L - t % L) - data;
    ans += 0.25 * (r - now2);
    data[r] = data[i] + L;
  }
  printf("%.12lf\n", ans / 2);
  return 0;
}
