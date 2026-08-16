#include <bits/stdc++.h>
using namespace std;
long long int assign[100], done[100];
int main() {
  ios::sync_with_stdio(false);
  ;
  cin.tie(0);
  ;
  long long int i, j, n, m, k, l, f = 0;
  cin >> n;
  for (i = 1; i <= n; i++) {
    for (j = 1; j < 1000; j++) {
      if (done[j]) continue;
      f = 0;
      for (k = 1; k < i; k++) {
        for (l = k + 1; l < i; l++) {
          for (m = 1; m < i; m++) {
            if (assign[k] + assign[l] == assign[m] + j) {
              f = 1;
              break;
            }
          }
          if (f) break;
        }
        if (f) break;
      }
      if (f) continue;
      for (k = 1; k < i; k++) {
        if (assign[k] + j > 1000) {
          f = 1;
          break;
        }
      }
      if (f) continue;
      assign[i] = j;
      done[j] = 1;
      break;
    }
  }
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
      if (i == j)
        cout << "0"
             << " ";
      else
        cout << assign[i] + assign[j] << " ";
    }
    cout << "\n";
  }
  return 0;
}
