#include <bits/stdc++.h>
using namespace std;
const int N = 5003;
int l[N], r[N];
int sum[N], ones[N], twos[N];
pair<int, int> getIntersection(int l1, int r1, int l2, int r2) {
  if (l2 < l1) {
    swap(l1, l2);
    swap(r1, r2);
  }
  pair<int, int> intersection = {1, 0};
  if (l2 <= r1) {
    intersection.first = l2;
    intersection.second = min(r1, r2);
  }
  return intersection;
}
int main() {
  int n, q;
  scanf("%d %d", &n, &q);
  for (int i = 0; i < q; ++i) {
    scanf("%d %d", l + i, r + i);
    ++sum[l[i]];
    --sum[r[i] + 1];
  }
  int nonzeros = 0;
  for (int i = 1; i <= n; ++i) {
    sum[i] += sum[i - 1];
    ones[i] = ones[i - 1] + (sum[i] == 1 ? 1 : 0);
    twos[i] = twos[i - 1] + (sum[i] == 2 ? 1 : 0);
    nonzeros += sum[i] > 0;
  }
  int res = 0;
  for (int i = 0; i < q; ++i) {
    for (int j = i + 1; j < q; ++j) {
      pair<int, int> intersection = getIntersection(l[i], r[i], l[j], r[j]);
      int cur = ones[r[i]] - ones[l[i] - 1];
      cur += ones[r[j]] - ones[l[j] - 1];
      cur += twos[intersection.second] - twos[intersection.first - 1];
      cur -= ones[intersection.second] - ones[intersection.first - 1];
      res = max(res, nonzeros - cur);
    }
  }
  printf("%d\n", res);
}
