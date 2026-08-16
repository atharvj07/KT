#include <bits/stdc++.h>
using namespace std;
int main() {
  int k;
  cin >> k;
  int cnt = 0;
  for (unsigned long long i = 19;; i++) {
    unsigned long long j = i;
    int val = 0;
    while (j > 0) val += j % 10, j /= 10;
    if (val == 10) cnt++;
    if (cnt == k) {
      cout << i << "\n";
      break;
    }
  }
  return 0;
}
