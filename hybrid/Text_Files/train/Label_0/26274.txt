#include <bits/stdc++.h>
using namespace std;
long long tree[5 * 200000 + 10];
long long flag[5 * 200000 + 10];
void lazy(int idx, int start, int end) {
  if (flag[idx] == 0) return;
  tree[idx] += (end - start + 1) * flag[idx];
  if (start < end) {
    flag[2 * idx + 1] += flag[idx];
    flag[2 * idx + 2] += flag[idx];
  }
  flag[idx] = 0;
}
void update(int idx, int start, int end, int l, int r, int add) {
  if (l > end || r < start) {
    lazy(idx, start, end);
    return;
  }
  if (l <= start && r >= end) {
    flag[idx] += add;
    lazy(idx, start, end);
  } else {
    lazy(idx, start, end);
    if (start < end) {
      update(2 * idx + 1, start, (start + end) / 2, l, r, add);
      update(2 * idx + 2, (start + end) / 2 + 1, end, l, r, add);
      tree[idx] = tree[2 * idx + 1] + tree[2 * idx + 2];
    }
  }
}
long long query(int idx, int start, int end, int l, int r) {
  if (l > end || r < start) return 0;
  lazy(idx, start, end);
  if (l <= start && r >= end) return tree[idx];
  return query(2 * idx + 1, start, (start + end) / 2, l, r) +
         query(2 * idx + 2, (start + end) / 2 + 1, end, l, r);
}
int main() {
  int N = 0, Q, C, a, b;
  long long res;
  scanf("%d", &Q);
  while (Q--) {
    scanf("%d", &C);
    switch (C) {
      case 1:
        scanf("%d %d", &a, &b);
        update(0, 0, 200000, 0, a - 1, b);
        res = query(0, 0, 200000, 0, N);
        printf("%lf\n", (double)res / (double)(N + 1));
        break;
      case 2:
        scanf("%d", &a);
        N++;
        update(0, 0, 200000, N, N, a);
        res = query(0, 0, 200000, 0, N);
        printf("%lf\n", (double)res / (double)(N + 1));
        break;
      case 3:
        int val = (int)query(0, 0, 200000, N, N);
        update(0, 0, 200000, N, N, -val);
        N--;
        res = query(0, 0, 200000, 0, N);
        printf("%lf\n", (double)res / (double)(N + 1));
        break;
    }
  }
  return 0;
}
