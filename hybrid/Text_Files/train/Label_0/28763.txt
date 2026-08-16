#include <bits/stdc++.h>
using namespace std;
int main() {
  long int n;
  cin >> n;
  long long count = 0;
  vector<long long int> a;
  long long int j;
  for (long int i = 0; i < n; i++) {
    cin >> j;
    a.push_back(j);
  }
  for (long int i = 0; i < n; i++) {
    cin >> j;
    a[i] -= j;
  }
  vector<long long int>::iterator it;
  sort(a.begin(), a.end());
  long long int m;
  vector<long long int>::iterator lower, upper;
  long int k;
  for (long int i = 0; i < n; i++) {
    if (a[i] > 0) {
      count += n - i - 1;
    } else {
      m = -a[i];
      it = a.begin() + i + 1;
      upper = upper_bound(a.begin(), a.end(), m);
      if (upper != a.end()) {
        k = (upper - a.begin());
        count += n - k;
      }
    }
  }
  cout << count << endl;
  return 0;
}
