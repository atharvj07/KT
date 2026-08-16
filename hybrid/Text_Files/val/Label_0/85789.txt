#include <bits/stdc++.h>
using namespace std;
long long int a[100010], b[100010], c[100010];
int main() {
  long long int n;
  cin >> n;
  if (n % 2 == 0)
    cout << "-1" << endl;
  else {
    for (long long int i = 0; i < n; i++) {
      a[i] = i % n;
      b[i] = i % n;
      c[i] = (a[i] + b[i]) % n;
    }
    for (long long int i = 0; i < n; i++) cout << a[i] << " ";
    for (long long int i = 0; i < n; i++) cout << b[i] << " ";
    for (long long int i = 0; i < n; i++) cout << c[i] << " ";
  }
  return 0;
}
