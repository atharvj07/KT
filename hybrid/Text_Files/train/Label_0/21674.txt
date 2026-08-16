#include <bits/stdc++.h>
int a[10000];
int m, n;
void quicksort(int b[], int low, int high) {
  int i = low;
  int j = high;
  int key = a[i];
  if (i < j) {
    while (i < j) {
      while (a[j] >= key && j > i) j--;
      a[i] = a[j];
      while (a[i] <= key && i < j) i++;
      a[j] = a[i];
    }
    a[i] = key;
    quicksort(a, low, i - 1);
    quicksort(a, i + 1, high);
  }
}
int main() {
  while (~scanf("%d %d", &m, &n)) {
    int i, j, t, sum = 0;
    for (i = 0; i < m; i++) scanf("%d", a + i);
    quicksort(a, 0, m - 1);
    for (i = 0; i < n; i++) sum += a[i];
    printf("%d\n", sum);
  }
  return 0;
}
