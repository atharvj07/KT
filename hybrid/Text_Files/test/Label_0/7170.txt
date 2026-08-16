#include <bits/stdc++.h>
using namespace std;
int n, idx;
long long mn = 1000000001, tmp, cnt;
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%I64d", &tmp);
    if (tmp < mn) {
      mn = tmp;
      idx = i + 1;
      cnt = 1;
    } else if (tmp == mn) {
      cnt++;
    }
  }
  if (cnt == 1)
    printf("%d", idx);
  else
    printf("Still Rozdil");
  return 0;
}
