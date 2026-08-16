#include <bits/stdc++.h>
using namespace std;
long long GCD(long long a, long long b) {
  long long c;
  while (a != 0) {
    c = a;
    a = b % a;
    b = c;
  }
  return b;
}
int main() {
  long long n;
  cin >> n;
  long long arr[n];
  long long sum = 0;
  for (long long i = 0; i < n; i++) {
    cin >> arr[i];
    sum = sum + arr[i];
  }
  sort(arr, arr + n);
  for (long long i = 0; i < n; i++) {
    sum = sum + 2 * (i * arr[i] - (n - i - 1) * arr[i]);
  }
  long long z = GCD(sum, n);
  cout << sum / z << " " << n / z << endl;
  return 0;
}
