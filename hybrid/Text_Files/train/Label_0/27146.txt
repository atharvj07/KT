#include <bits/stdc++.h>
using namespace std;
char str[300005];
int main() {
  int n;
  scanf("%d", &n);
  scanf("%s", str);
  int flag = 0, pos = 1;
  for (int i = 0; i < n - 1; i++) {
    if (str[i + 1] >= str[i])
      flag++;
    else
      pos = i;
  }
  if (flag != n - 1) {
    printf("YES\n");
    printf("%d %d\n", pos + 1, pos + 2);
  } else
    printf("NO\n");
}
