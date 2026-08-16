#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int a[n];
  int sum = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    sum += a[i];
  }
  if (sum != 0) {
    puts("YES\n1");
    printf("%d %d", 1, n);
    return 0;
  }
  int p;
  for (p = 0; p < n; p++)
    if (a[p] != 0) break;
  if (p == n) {
    cout << "NO";
  } else {
    puts("YES\n2");
    printf("%d %d\n", 1, p + 1);
    printf("%d %d\n", p + 2, n);
  }
  return 0;
}
