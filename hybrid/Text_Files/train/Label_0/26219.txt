#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  while (cin >> n) {
    vector<int> v;
    int c[3] = {0};
    for (int i = 0; i < n; i++) {
      int x;
      scanf("%d", &x);
      v.push_back(x);
      c[x]++;
    }
    int flag = 0;
    if (c[1] >= 3) {
      flag = 1;
      printf("1 1 1");
      c[1] -= 3;
    } else if (c[2] >= 1 && c[1] >= 1) {
      flag = 1;
      printf("2 1");
      c[1] -= 1;
      c[2] -= 1;
    }
    while (c[2]) {
      if (flag) printf(" ");
      flag = 1;
      printf("2");
      c[2]--;
    }
    while (c[1]) {
      if (flag) printf(" ");
      flag = 1;
      printf("1");
      c[1]--;
    }
    printf("\n");
  }
}
