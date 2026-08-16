#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  scanf("%d", &n);
  int m;
  scanf("%d", &m);
  char s[n + 1];
  scanf("%s", &s);
  int no[n + 1];
  for (int i(0); i < n; ++i) {
    no[i + 1] = static_cast<int>(s[i]) - 97;
  }
  no[0] = 0;
  int i(n);
  while (i > 0 && no[i] == m - 1) {
    i = i - 1;
  }
  no[i] = no[i] + 1;
  int j(i + 1);
  while (j <= n - 2) {
    no[j] = 0;
    no[j + 1] = 1;
    no[j + 2] = 2;
    j = j + 3;
  }
  no[j] = 0;
  if (j + 1 == n) {
    no[j + 1] = 1;
  };
  j = 2;
  while (no[0] == 0 && j <= n) {
    if (j < 2) {
      j = 2;
    };
    if (no[j] == no[j - 1]) {
      if (no[j] != m - 1) {
        no[j] = no[j] + 1;
        int k(j + 1);
        while (k <= n - 2) {
          no[k] = 0;
          no[k + 1] = 1;
          no[k + 2] = 2;
          k = k + 3;
        }
        no[k] = 0;
        if (k + 1 == n) {
          no[k + 1] = 1;
        };
        j = j - 1;
      } else {
        no[j - 2] = no[j - 2] + 1;
        int k(j - 1);
        while (k <= n - 2) {
          no[k] = 0;
          no[k + 1] = 1;
          no[k + 2] = 2;
          k = k + 3;
        }
        no[k] = 0;
        if (k + 1 == n) {
          no[k + 1] = 1;
        };
        j = j - 3;
      }
    };
    if (j > 2 && no[j] == no[j - 2]) {
      if (no[j] != m - 1) {
        no[j] = no[j] + 1;
        int k(j + 1);
        while (k <= n - 2) {
          no[k] = 0;
          no[k + 1] = 1;
          no[k + 2] = 2;
          k = k + 3;
        }
        no[k] = 0;
        if (k + 1 == n) {
          no[k + 1] = 1;
        };
        j = j - 1;
      } else {
        no[j - 1] = no[j - 1] + 1;
        int k(j);
        while (k <= n - 2) {
          no[k] = 0;
          no[k + 1] = 1;
          no[k + 2] = 2;
          k = k + 3;
        }
        no[k] = 0;
        if (k + 1 == n) {
          no[k + 1] = 1;
        };
        j = j - 2;
      }
    }
    j = j + 1;
  };
  if (m == 2) {
    if (s[0] == 'a' && s[1] == 'b') {
      printf("%s", "ba");
    } else if (s[0] == 'a') {
      printf("%s", "b");
    } else {
      printf("NO");
    }
  } else if (m == 1) {
    printf("NO");
  } else {
    if (no[0] == 1) {
      printf("NO");
    } else {
      for (int i(0); i < n; ++i) {
        s[i] = no[i + 1] + 97;
      }
      printf("%s", s);
    }
  }
  return (0);
}
