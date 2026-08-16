#include <bits/stdc++.h>
using namespace std;
char *pt;
long get_int() {
  long temp = 0;
  while (*pt < '0' && *pt > '9') pt++;
  while (*pt >= '0' && *pt <= '9') {
    temp = temp * 10 + (*pt - '0');
    pt++;
  }
  pt++;
  return temp;
}
long long gcd(long long a, long long b) {
  if (b == 1 || a == 1) return 1;
  if (a % b == 0)
    return b;
  else
    return gcd(b, a % b);
}
long long fastPower(long long a, long long b) {
  if (b == 0) return 1;
  if (b == 1) return a % 747474747;
  long long ans = fastPower(a, b / 2);
  ans *= ans;
  ans %= 747474747;
  if (b % 2) ans *= a;
  return ans % 747474747;
}
long long fastPowerCustomMod(long long a, long long b, long long c) {
  if (b == 0) return 1;
  if (b == 1) return a % c;
  long long ans = fastPower(a, b / 2);
  ans *= ans;
  ans %= c;
  if (b % 2) ans *= a;
  return ans % c;
}
int is_prime(long long num) {
  if (num == 2 || num == 3) return 1;
  if (num % 2 == 0 || num % 3 == 0) return 0;
  long long i = 5, w = 2;
  while (i * i <= num) {
    if (num % i == 0) return 0;
    i += w;
    w = 6 - w;
  }
  return 1;
}
int compare(const void *a, const void *b) {
  return (*(long long *)a - *(long long *)b);
}
int dec_compare(const void *a, const void *b) {
  return (-*(int *)a + *(int *)b);
}
long long eularTotient(long long n) {
  long long result = n;
  for (long long i = 2; i * i <= n; i++) {
    if (n % i == 0) result -= result / i;
    while (n % i == 0) n /= i;
  }
  if (n > 1) result -= result / n;
  return result;
}
FILE *in, *out;
char str[1000000];
int main() {
  scanf("%s", str);
  int h, min;
  h = (str[0] - '0') * 10 + str[1] - '0';
  min = (str[3] - '0') * 10 + str[4] - '0';
  float a, b;
  a = h * 30.0 + (min * 30.0) / 60.0;
  b = min * 6.0;
  while (a >= 360.0) a -= 360.0;
  while (b >= 360.0) b -= 360.0;
  cout << a << " " << b << endl;
  return 0;
}
