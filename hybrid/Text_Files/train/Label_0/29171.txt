#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
char a[N];
int main() {
  scanf("%s", a);
  int n = strlen(a);
  int cnt1 = 0, cnt2 = 0;
  int flag1 = 0, flag2 = 0;
  char last = '0';
  for (int i = 0; i < n; i++) {
    int cnt = 1;
    int t = i;
    while (i + 1 < n && a[i] == a[i + 1]) {
      i++;
      cnt++;
    }
    if (cnt % 2 == 0) continue;
    if (a[t] == '+') {
      if (a[t] != last) {
        cnt1++;
        last = a[t];
      } else {
        cnt1--;
        last = '-';
      }
    } else {
      if (a[t] != last) {
        cnt2++;
        last = a[t];
      } else {
        cnt2--;
        last = '+';
      }
    }
  }
  if (cnt1 + cnt2 == 0)
    printf("Yes\n");
  else
    printf("No\n");
  return 0;
}
