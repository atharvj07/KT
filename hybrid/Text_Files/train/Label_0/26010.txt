#include <bits/stdc++.h>
using namespace std;
inline int getint() {
  int f = 1, x = 0;
  char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (isdigit(c)) {
    x = x * 10 + c - '0';
    c = getchar();
  }
  return x * f;
}
inline long long getll() {
  long long f = 1, x = 0;
  char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (isdigit(c)) {
    x = x * 10 + c - '0';
    c = getchar();
  }
  return x * f;
}
int a0;
long long ans;
int main() {
  a0 = getint();
  for (int(i) = (1); (i) <= (a0); ++(i)) ans += (i * getint());
  printf("%lld\n", ans);
  return 0;
}
