#include <stdio.h>

int main()
{
  int n;
  scanf("%d", &n);
  long long int N[n], max = 1e18, prod = 1, flag = 0, zero = 0;
  
  for (int i = 0; i < n; i++)
  {
    scanf("%lld", &N[i]);
    flag = (N[i] > max) ? 1 : flag;
    prod *= N[i];
    (N[i]) ? max /= N[i] : zero = 1;
  }

  (zero) ? puts("0") : ((flag) ? puts("-1") : printf("%lld\n", prod));
  return 0;
}