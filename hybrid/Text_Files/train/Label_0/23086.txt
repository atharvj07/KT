#include <bits/stdc++.h>
using namespace std;
int zerk(char s) {
  char k = 0;
  for (int i = 0; i < 4; i++)
    k = k + (s / ((int)(pow(2.0, i))) % 2) * pow(2.0, 7 - i) +
        (s / ((int)(pow(2.0, 7 - i))) % 2) * pow(2.0, i);
  if (k < 0)
    return k + 256;
  else
    return k;
}
int main() {
  char *s = new char[101];
  int i, k, b;
  gets(s);
  int n = strlen(s);
  for (i = 0; i < n; i++) {
    b = zerk(s[i - 1]) - zerk(s[i]) % 256;
    if (b < 0) b += 256;
    cout << b << endl;
  }
  return 0;
}
