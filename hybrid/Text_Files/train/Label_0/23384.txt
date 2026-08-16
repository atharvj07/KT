#include <bits/stdc++.h>
using namespace std;
int arr[4];
int main() {
  int n, a;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a);
    arr[a]++;
  }
  return printf("%d\n", n - max(max(arr[1], arr[2]), arr[3])), 0;
}
