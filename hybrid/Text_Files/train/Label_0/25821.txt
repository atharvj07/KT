#include <bits/stdc++.h>
int main(void) {
  long long t;
  scanf("%lld", &t);
  long long num, sub_num, i, j;
  while (t--) {
    int cnt = 1;
    scanf("%lld", &num);
    for (i = 2; (i * i) <= num; ++i) {
      if (!cnt) {
        break;
      }
      if (!(num % i)) {
        sub_num = (num / i);
        for (j = (i + 1); (j * j) < sub_num; ++j) {
          if (!(sub_num % j)) {
            printf("YES\n%lld %lld %lld\n", i, j, (sub_num / j));
            --cnt;
            break;
          }
        }
      }
    }
    if (cnt) {
      printf("NO\n");
    }
  }
  return 0;
}
