#include <bits/stdc++.h>
using namespace std;
const int SIZE = 1 << 19;
const int LOGS = 19;
int n;
int arr[SIZE];
pair<int, int> rmq[2 * SIZE];
int nxt[LOGS + 1][SIZE];
pair<int, int> RMQMin(int left, int right) {
  left += SIZE - 1;
  right += SIZE - 1;
  pair<int, int> res = min(rmq[left], rmq[right]);
  if (left == right) return res;
  while (1) {
    int lf = (left - 1) >> 1;
    int rf = (right - 1) >> 1;
    if (lf == rf) break;
    if (left & 1) res = min(res, rmq[left + 1]);
    if (!(right & 1)) res = min(res, rmq[right - 1]);
    left = lf;
    right = rf;
  }
  return res;
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
  for (int i = 0; i < n; i++) arr[i + n] = arr[i];
  memset(rmq, 63, sizeof(rmq));
  for (int i = 0; i < 2 * n; i++)
    rmq[SIZE - 1 + i] = pair<int, int>(max(i - arr[i], 0), i);
  for (int i = SIZE - 2; i >= 0; i--)
    rmq[i] = min(rmq[2 * i + 1], rmq[2 * i + 2]);
  for (int i = 0; i < 2 * n; i++) {
    int left = rmq[SIZE - 1 + i].first;
    pair<int, int> tmin = RMQMin(left, i);
    nxt[0][i] = tmin.second;
  }
  for (int i = 1; i <= LOGS; i++)
    for (int j = 0; j < 2 * n; j++) {
      int t = nxt[i - 1][j];
      t = nxt[i - 1][t];
      nxt[i][j] = t;
    }
  long long ans = 0;
  for (int i = 2 * n - 1; i >= n; i--) {
    int curr = i;
    int end = curr - n + 1;
    int sum = 0;
    if (rmq[SIZE - 1 + curr].first > end) {
      for (int v = LOGS; v >= 0;) {
        int g = nxt[v][curr];
        if (rmq[SIZE - 1 + g].first <= end)
          v--;
        else {
          curr = nxt[v][curr];
          sum += (1 << v);
        }
      }
      sum++;
    }
    sum++;
    ((void)0);
    ans += sum;
  }
  printf("%I64d\n", ans);
  return 0;
}
