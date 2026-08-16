#include <stdio.h>
#include <stdbool.h>
#define rep(i, n) for(int i = 0; i < n; ++i)

bool flag[4000000];

int main(void) {
  int i, j, k, n;
  scanf("%d", &n);
  rep(i, 4000000) flag[i] = false;
  rep(i, n) {
    int a, b;
    scanf("%d%d", &a, &b);
    a += b;
    if(!flag[a]) flag[a] = true;
    else {
      for(j = a; i < 4000000; ++j) {
        if(flag[j]) flag[j] = false;
        else {
          flag[j] = true;
          break;
        }
      }
    }
    /*rep(j, 9) printf("%d ", flag[j] ? 1 : 0);
    printf("\n");*/
  }
  rep(i, 4000000) if(flag[i]) printf("%d 0\n", i);
  return 0;
}
