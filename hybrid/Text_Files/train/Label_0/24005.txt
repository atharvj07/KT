#include <cstdio>
int main() {
  int n, k;
  scanf("%d %d", &n, &k);
  if (k > ((n + 1) / 2)) puts("NO");
  else puts("YES");
  return 0;
}
