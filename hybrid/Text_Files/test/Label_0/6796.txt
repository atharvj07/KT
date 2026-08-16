#include <bits/stdc++.h>
using namespace std;
int arr[1000000 + 5];
int main() {
  int n, q;
  scanf("%d %d", &n, &q);
  int pos1 = 0, pos2 = 1, rev = 0;
  for (int i = 0; i < q; i++) {
    int op;
    scanf("%d", &op);
    if (op == 1) {
      int shift;
      scanf("%d", &shift);
      pos1 = (pos1 + shift) % n;
      pos2 = (pos2 + shift) % n;
      if (pos1 < 0) pos1 = pos1 + n;
      if (pos2 < 0) pos2 = pos2 + n;
    } else if (op == 2) {
      if (pos1 % 2 == 0)
        pos1 = (pos1 + 1);
      else
        pos1 = (pos1 - 1);
      if (pos2 % 2 == 0)
        pos2 = (pos2 + 1);
      else
        pos2 = (pos2 - 1);
    }
  }
  int i = pos1;
  int data = 1;
  while (data <= n) {
    arr[i] = data;
    data += 2;
    i = (i + 2) % n;
  }
  i = pos2;
  data = 2;
  while (data <= n) {
    arr[i] = data;
    data += 2;
    i = (i + 2) % n;
  }
  for (int j = 0; j < n; j++) {
    printf("%d ", arr[j]);
  }
  return 0;
}
