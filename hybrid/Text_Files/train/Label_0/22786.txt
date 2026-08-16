#include <bits/stdc++.h>
using namespace std;
int N;
char S[2000005];
unsigned long long p[2000005], a[2000005];
unsigned long long get(int l, int r) { return a[r] - a[l - 1] * p[r - l + 1]; }
void makehash() {
  for (int i = 1; i <= N; i++) a[i] = a[i - 1] * 31415927 + S[i];
}
int lcp(int l1, int r1, int l2, int r2) {
  r2 = min(r2, N);
  if (l2 > r2) return 0;
  if (S[l1] != S[l2]) return 0;
  int l = 0, r = r1 - l1 + 1;
  for (; l <= r;) {
    int m = (l + r) >> 1;
    if (get(l1, l1 + m - 1) == get(l2, l2 + m - 1))
      l = m + 1;
    else
      r = m - 1;
  }
  return r;
}
int lcs(int l1, int r1, int l2, int r2) {
  r2 = min(r2, N);
  if (l2 > r2) return 0;
  if (S[r1] != S[r2]) return 0;
  int l = 0, r = r1 - l1 + 1;
  for (; l <= r;) {
    int m = (l + r) >> 1;
    if (get(r1 - m + 1, r1) == get(r2 - m + 1, r2))
      l = m + 1;
    else
      r = m - 1;
  }
  return r;
}
bool can(int l) {
  for (int i = 2; l * i <= N; i++)
    if (lcs(l * (i - 2) + 1, l * (i - 1), l * (i - 1) + 1, l * i) +
            lcp(l * (i - 1) + 1, l * i, l * i + 1, l * (i + 1)) >=
        l)
      return 1;
  return 0;
}
void doit() {
  scanf("%s", S + 1), N = strlen(S + 1), p[0] = 1;
  for (int i = 1; i <= N; i++) p[i] = p[i - 1] * 31415927;
  makehash();
  for (int l = 1; l <= N; l++)
    if (can(l)) {
      int n = 0;
      for (int i = 1; i <= N; i++)
        if (i + 2 * l - 1 <= N &&
            get(i, i + l - 1) == get(i + l, i + 2 * l - 1))
          i += l - 1;
        else
          S[++n] = S[i];
      N = n, makehash(), S[N + 1] = 0;
    }
  S[N + 1] = 0, puts(S + 1);
}
int main() {
  doit();
  return 0;
}
