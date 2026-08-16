#include <bits/stdc++.h>
using namespace std;

#define SHEEP 0
#define WOLF 1

const char OUT[] = "SW";

int N;
char S[114514];
int ans[114514];

int main() {
  scanf("%d", &N);
  scanf("%s", S);

  for (int a=0; a<2; a++) {
    for (int b=0; b<2; b++) {
      ans[0] = a;
      ans[1] = b;
      for (int i=1; i<N-1; i++) {
        ans[i+1] = ans[i-1] ^ (ans[i] == SHEEP) ^ (S[i] == 'o');
      }

      bool failed = false;
      for (int i=0; i<N; i++) {
        int t = ans[(i+N-1)%N] ^ ans[(i+1)%N];
        int s = (ans[i] == SHEEP) ^ (S[i] == 'o');
        if (s != t) {
          failed = true;
          break;
        }
      }

      if (!failed) {
        for (int i=0; i<N; i++) {
          printf("%c", OUT[ans[i]]);
        }
        puts("");
        return 0;
      }
    }
  }
  puts("-1");
}
