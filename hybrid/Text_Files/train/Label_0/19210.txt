#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  vector<int> vec(n);
  int a, b;
  scanf("%d%d", &a, &b);
  vec[0] = a * b;
  for (int i = 1; i < n; i++) {
    scanf("%d%d", &a, &b);
    vec[i] = vec[i - 1] + a * b;
  }
  int l = 0;
  for (int i = 0; i < m; i++) {
    int v;
    scanf("%d", &v);
    for (int j = l; j < n; j++) {
      if (v <= vec[j]) {
        j++;
        printf("%d\n", j);
        l = j - 1;
        break;
      }
    }
  }
  return 0;
}
