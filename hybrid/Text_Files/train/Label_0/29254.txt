#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, A;
  cin >> n >> A;
  std::vector<long long int> v;
  long long int sum = 0;
  for (long long int i = 0; i < n; ++i) {
    long long int temp;
    cin >> temp;
    v.push_back(temp);
    sum += temp;
  }
  long long int diff1 = A - (n - 1);
  for (long long int i = 0; i < n; ++i) {
    long long int tmpSum = sum - v[i];
    long long int diff2 = A - tmpSum;
    if (diff2 <= 0) {
      if (diff1 <= v[i]) {
        cout << v[i] - diff1;
      } else {
        cout << 0;
      }
    } else {
      long long int ans = 0;
      ans += diff2 - 1;
      if (diff1 < v[i]) {
        ans += v[i] - diff1;
      }
      cout << ans;
    }
    if (i != n - 1) cout << " ";
  }
  cout << endl;
}
