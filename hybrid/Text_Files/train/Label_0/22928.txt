#include <bits/stdc++.h>
using namespace std;
template <class T>
inline bool isLeap(T y) {
  return (y % 400 == 0) || (y % 100 ? y % 4 == 0 : false);
}
template <class T>
inline T gcd(T a, T b) {
  return (b) == 0 ? (a) : gcd((b), ((a) % (b)));
}
template <class T>
inline T lcm(T a, T b) {
  return ((a) / gcd((a), (b)) * (b));
}
template <class T>
inline T BigMod(T Base, T power, T M = 1000000007) {
  if (power == 0) return 1;
  if (power & 1)
    return ((Base % M) * (BigMod(Base, power - 1, M) % M)) % M;
  else {
    T y = BigMod(Base, power / 2, M) % M;
    return (y * y) % M;
  }
}
template <class T>
inline T ModInv(T A, T M = 1000000007) {
  return BigMod(A, M - 2, M);
}
int fx[] = {-1, +0, +1, +0, +1, +1, -1, -1, +0};
int fy[] = {+0, -1, +0, +1, +1, -1, +1, -1, +0};
int day[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int main() {
  int n;
  scanf("%d", &n);
  if (n % 2 != 0) {
    printf("0\n");
  } else {
    n /= 2;
    printf("%d\n", (n - 1) / 2);
  }
  return 0;
}
