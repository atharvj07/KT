#include <bits/stdc++.h>
using namespace std;
vector<long long> v1;
long long power(long long x, long long y) {
  if (y == 0)
    return 1;
  else if (y % 2 == 0)
    return power(x, y / 2) * power(x, y / 2);
  else
    return x * power(x, y / 2) * power(x, y / 2);
}
int main() {
  long long n;
  long long num, i;
  for (i = 1; i <= 30; i++) {
    num = (power(2, i) - 1) * power(2, i - 1);
    v1.push_back(num);
  }
  cin >> n;
  for (i = 29; i >= 0; i--) {
    if ((n % v1[i]) == 0) {
      break;
    }
  }
  cout << v1[i] << endl;
  return 0;
}
