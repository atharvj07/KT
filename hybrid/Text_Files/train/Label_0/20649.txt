#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  long long a[n];
  long long sum = 0;
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    sum = sum + (i + 1) * (a[i] - 1) + 1;
  }
  cout << sum;
  return 0;
}
