#include <bits/stdc++.h>
using namespace std;
const int N = 5e6 + 10;
int n, k, m, A[N], c[N], tlen, z[N << 1];
char s[N], t[N], S[N], T[N], SS[N << 1];
void check(int len) {
  for (int i = 1; i <= len; i++) {
    if (T[i] < S[i]) return;
    if (T[i] > S[i]) break;
  }
  for (int i = 1; i <= len; i++) T[i] = S[i];
  return;
}
int main() {
  scanf("%s%d", s + 1, &k);
  n = strlen(s + 1);
  reverse(s + 1, s + n + 1);
  if (k == 1) {
    for (int i = 1; i <= n; i++) t[i] = s[n - i + 1];
    for (int i = 1; i <= n; i++) {
      if (s[i] < t[i]) return printf("%s", s + 1), 0;
      if (t[i] < s[i]) return printf("%s", t + 1), 0;
    }
    return printf("%s", s + 1), 0;
  }
  for (int i = 1; i <= n;) {
    int j = i, k = i + 1;
    while (k <= n && s[j] <= s[k]) {
      if (s[j] < s[k])
        j = i;
      else
        j++;
      k++;
    }
    A[++m] = i;
    c[m] = k - j;
    while (i <= j) i += k - j;
  }
  A[m + 1] = n + 1;
  while (m > 0 && k >= 3) {
    for (int i = A[m]; i <= A[m + 1] - 1; i++) t[++tlen] = s[i];
    if (c[m] != 1 || c[m - 1] != 1) k--;
    m--;
  }
  if (m == 0) return printf("%s", t + 1), 0;
  T[1] = 'z' + 1;
  for (int i = 1; i <= A[m + 1] - 1; i++) S[i] = s[A[m + 1] - i];
  check(A[m + 1] - 1);
  for (int i = 1; i <= A[m + 1] - 1; i++) SS[i] = SS[i + A[m + 1] - 1] = s[i];
  int x = 1, y = 2, k = 0;
  for (; x <= A[m + 1] - 1 && y <= A[m + 1] - 1 && k <= A[m + 1] - 2;) {
    if (SS[x + k] == SS[y + k])
      k++;
    else if (SS[x + k] < SS[y + k])
      y += k + 1, k = 0;
    else
      x += k + 1, k = 0;
    if (x == y) y++;
  }
  for (int i = 1; i <= A[m + 1] - 1; i++) S[i] = SS[min(x, y) + i - 1];
  check(A[m + 1] - 1);
  for (int i = 1; i <= A[m + 1] - 1; i++) SS[i] = s[i];
  for (int i = 1; i <= A[m + 1] - 1; i++)
    SS[i + A[m + 1] - 1] = s[A[m + 1] - i];
  int len = 2 * (A[m + 1] - 1);
  for (int i = 2, mr = 1, ml; i <= len; i++) {
    z[i] = (i < mr ? min(z[i - ml + 1], mr - i) : 0);
    while (SS[z[i] + 1] == SS[i + z[i]]) z[i]++;
    if (i + z[i] > mr) mr = i + z[i], ml = i;
  }
  z[1] = len;
  k = A[m + 1];
  for (int i = A[m + 1] - 1; i >= 1; i--) {
    int l = A[m + 1] - i, r = A[m + 1] - k + 1;
    int op = z[r + A[m + 1] - 1];
    if (op < l - r + 1) {
      if (SS[op + 1] > SS[k - op - 1]) k = i;
    } else {
      op = k - i;
      l = op + 1, r - k - 1;
      if (SS[z[l] + 1] < SS[z[l] + l]) k = i;
    }
  }
  int tot = 0;
  for (int i = A[m + 1] - 1; i >= k; i--) S[++tot] = SS[i];
  for (int i = 1; i <= k - 1; i++) S[++tot] = SS[i];
  check(A[m + 1] - 1);
  for (int i = 1; i <= A[m + 1] - 1; i++) SS[i] = s[i];
  int p = m;
  while ((A[p + 1] - A[p]) * 2 <= (A[p] - A[p - 1]) + 1) {
    bool flag = 0;
    for (int i = A[p] - 1; i >= A[p - 1]; i--) {
      if (SS[i] < SS[A[m + 1] - 1 - i + A[p - 1]]) {
        flag = 1;
        break;
      }
      if (SS[i] > SS[A[m + 1] - 1 - i + A[p - 1]]) break;
    }
    if (flag) break;
    p--;
  }
  p = A[p];
  tot = 0;
  for (int i = p; i <= A[m + 1] - 1; i++) S[++tot] = SS[i];
  for (int i = p - 1; i >= 1; i--) S[++tot] = SS[i];
  check(A[m + 1] - 1);
  for (int i = 1; i <= A[m + 1] - 1; i++) t[++tlen] = T[i];
  printf("%s", t + 1);
  return 0;
}
