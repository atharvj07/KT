#include <bits/stdc++.h>
using namespace std;
int main(void) {
  int k, a, b;
  char vowel[5] = {'a', 'e', 'i', 'o', 'u'};
  scanf("%d", &k);
  for (int i = 5; i * i <= k; ++i) {
    if (k % i == 0 && k / i >= 5) {
      a = i;
      b = k / i;
      for (int j = 0; j < a; ++j) {
        for (int k = 0; k < b; ++k) {
          printf("%c", vowel[(j + k) % 5]);
        }
      }
      return 0;
    }
  }
  puts("-1");
  return 0;
}
