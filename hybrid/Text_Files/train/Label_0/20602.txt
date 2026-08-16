#include <bits/stdc++.h>
using namespace std;
int n;
int main() {
  scanf("%d", &n);
  int minday = n / 7 * 2, maxday = n;
  if (n % 7 == 6) minday++;
  if (n > 2) {
    maxday = 2;
    n -= 2;
    maxday += n / 7 * 2;
    if (n % 7 == 6) maxday++;
  }
  cout << minday << " " << maxday << endl;
  return 0;
}
