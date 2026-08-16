#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, pos = 0, neg = 0;
  cin >> n;
  long long a[n];
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    pos += (a[i] > 0);
    neg += (a[i] < 0);
  }
  long long lim = (n + 1) / 2;
  if (pos >= lim)
    cout << "1" << endl;
  else if (neg >= lim)
    cout << "-1" << endl;
  else
    cout << "0" << endl;
  return 0;
}
