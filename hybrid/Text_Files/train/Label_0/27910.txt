#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, x, y;
  long long minimum = INT_MAX;
  cin >> n >> x >> y;
  vector<long long> A(n + 1);
  for (int i = 1; i <= n; i++) cin >> A[i];
  for (int i = 1; i <= n; i++) {
    int flag = 1;
    for (int j = i - 1; j >= i - x; j--) {
      if (j > 0 && A[j] <= A[i]) flag = 0;
    }
    for (int j = i + 1; j <= i + y; j++) {
      if (j <= n && A[j] <= A[i]) flag = 0;
    }
    if (flag == 1) {
      cout << i << endl;
      break;
    }
  }
}
