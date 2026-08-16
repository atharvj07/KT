#include <bits/stdc++.h>
using namespace std;
long long n;
int main() {
  scanf("%lld", &n);
  long long f[3] = {1, 1, 2};
  int idx = 1;
  while (f[2] < n) {
    f[0] = f[1];
    f[1] = f[2];
    f[2] = f[0] + f[1];
    idx++;
  }
  if (f[2] > n) idx--;
  printf("%d\n", idx);
}
