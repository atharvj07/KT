#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    long long maxi = arr[n - 1], mini = arr[n - 1];
    int x = 0;
    for (int i = n - 2; i >= 0; i--) {
      x = max((long long)x,
              (long long)ceil(log((double)(arr[i] - mini + 1)) / log(2.0)));
      mini = min(mini, arr[i]);
    }
    cout << x << endl;
  }
}
