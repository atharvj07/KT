#include <bits/stdc++.h>
using namespace std;
template <class T>
T sqr(const T &a) {
  return a * a;
}
int n, a[100][100], used[100];
int main() {
  scanf("%d", &n);
  for (int i = 0; i < (n); i++)
    for (int j = 0; j < (n); j++) scanf("%d", &a[i][j]), a[i][j]--;
  for (int i = 0; i < (n); i++) {
    int ok = 0;
    for (int j = 0; j < (n); j++) {
      int cnt = 0;
      for (int k = 0; k < (n); k++)
        if (a[j][k] == i) cnt++;
      if (cnt == n - i - 1 && !used[j]) {
        used[j] = i + 1;
        break;
      }
    }
  }
  for (int j = 0; j < (n); j++) printf("%d ", used[j]);
}
