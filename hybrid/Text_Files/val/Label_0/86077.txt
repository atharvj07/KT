#include <bits/stdc++.h>
using namespace std;
int main() {
  char s[100007];
  scanf("%s", &s);
  int l = strlen(s), one = 0, zero = 0, x = 0;
  for (int i = 0; i < l; i++)
    if (s[i] == '0')
      zero++;
    else if (s[i] == '1')
      one++;
    else
      x++;
  int n = l;
  if (l & 1) zero++, n = l + 1;
  if (zero + x > one) printf("00\n");
  if (min(one, zero) + x >= n / 2) {
    if (s[l - 1] == '1' || s[l - 1] == '?' && zero + x - 1 >= n / 2)
      printf("01\n");
    if (s[l - 1] == '0' || s[l - 1] == '?' && one + x - 1 >= n / 2)
      printf("10\n");
  }
  if (one + x > zero) printf("11\n");
  return 0;
}
