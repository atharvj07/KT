#include <bits/stdc++.h>
using namespace std;
int T, N;
int main() {
  scanf("%d", &T);
  while (T--) {
    scanf("%d", &N);
    vector<int> a(N), b(N), c(N), ans(N, -1);
    for (int n = 0; n < N; n++) cin >> a[n];
    for (int n = 0; n < N; n++) cin >> b[n];
    for (int n = 0; n < N; n++) cin >> c[n];
    for (int n = 0; n < N; n++) {
      for (int j : {a[n], b[n], c[n]}) {
        if (ans[(N + n - 1) % N] != j && ans[(n + 1) % N] != j) {
          ans[n] = j;
          break;
        }
      }
    }
    for (int n = 0; n < N; n++) printf("%d ", ans[n]);
    printf("\n");
  }
}
