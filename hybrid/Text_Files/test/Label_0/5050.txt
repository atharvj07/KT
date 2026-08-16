#include <bits/stdc++.h>
using namespace std;
int main() {
  long int x, t, a, b, da, db;
  scanf("%ld %ld %ld %ld %ld %ld", &x, &t, &a, &b, &da, &db);
  if (x == 0) {
    printf("%s \n", "YES");
    goto exit;
  } else {
    for (int tz = 0; tz < t; ++tz) {
      for (int tu = 0; tu < t; ++tu) {
        if (a - da * tz == x) {
          printf("%s \n", "YES");
          goto exit;
        }
      }
    }
    for (int tz = 0; tz < t; ++tz) {
      for (int tu = 0; tu < t; ++tu) {
        if (b - db * tu == x) {
          printf("%s \n", "YES");
          goto exit;
        }
      }
    }
    for (int tz = 0; tz < t; ++tz) {
      for (int tu = 0; tu < t; ++tu) {
        if (a - da * tz + b - db * tu == x) {
          printf("%s \n", "YES");
          goto exit;
        }
      }
    }
    printf("%s \n", "NO");
  }
exit:
  return 0;
}
