#include <bits/stdc++.h>
using namespace std;
bool mask[1006][1006];
void gen(int x) {
  int dl = (1 << (x - 1));
  for (int i = 0; i < dl; i++)
    for (int j = 0; j < dl; j++) {
      mask[i + dl][j] = mask[i][j];
      mask[i][j + dl] = mask[i][j];
      mask[i + dl][j + dl] = !mask[i][j];
    }
}
void wypisz(int k) {
  for (int i = 0; i < (1 << k); i++) {
    for (int j = 0; j < (1 << k); j++)
      if (mask[i][j])
        printf("+");
      else
        printf("*");
    puts("");
  }
}
int main() {
  int k;
  scanf("%d", &k);
  mask[0][0] = true;
  for (int i = 1; i <= k; i++) gen(i);
  wypisz(k);
  return 0;
}
