#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int n, a, b, k, count = 0, sum = 0;
  cin >> n >> a >> b >> k;
  vector<long long int> v;
  long long int x[n], r[n];
  for (long long int i = 0; i < n; i++) {
    cin >> x[i];
    r[i] = x[i] % (a + b);
  }
  for (long long int i = 0; i < n; i++) {
    if (r[i] >= 1 && r[i] <= a) {
      count++;
    } else if (r[i] == 0) {
      v.push_back(ceil((double)b / a));
    } else if (r[i] > a) {
      v.push_back(ceil((double)(r[i] - a) / a));
    }
  }
  sort(v.begin(), v.end());
  for (long long int i = 0; i < v.size(); i++) {
    sum += v[i];
    if (sum > k) {
      break;
    }
    count++;
  }
  cout << count;
  return 0;
}
