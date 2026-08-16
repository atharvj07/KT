#include <bits/stdc++.h>
using namespace std;
char s[200005];
int main() {
  int k, n;
  int zk;
  int yk;
  while (~scanf("%d%d", &n, &k)) {
    zk = 0;
    yk = 0;
    scanf("%s", s);
    int lens = strlen(s);
    for (int i = 0; i < lens; i++) {
      if (s[i] == '(' && zk < k / 2) {
        zk++;
        printf("(");
      } else if (s[i] == ')' && yk < k / 2) {
        yk++;
        printf(")");
      }
    }
    printf("\n");
  }
  return 0;
}
