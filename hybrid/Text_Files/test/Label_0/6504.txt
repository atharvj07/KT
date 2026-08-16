#include <bits/stdc++.h>
using namespace std;
int arr[100009];
int main(void) {
  int n, k;
  scanf("%d %d", &n, &k);
  for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
  int temp, pos = 0;
  while (arr[pos] < 0) {
    pos++;
  }
  for (int i = 0, j = pos - 1; i < pos / 2; i++, j--) {
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  for (int i = n - 1; i >= 0; i--) {
    if (arr[i] < 0 && k > 0) {
      k--;
      arr[i] = arr[i] * (-1);
    }
  }
  sort(arr, arr + n);
  while (k > 0) {
    arr[0] = arr[0] * (-1);
    k--;
  }
  int ans = 0;
  for (int i = 0; i < n; i++) ans += arr[i];
  printf("%d\n", ans);
  return 0;
}
