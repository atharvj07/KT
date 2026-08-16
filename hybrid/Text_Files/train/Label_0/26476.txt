#include <bits/stdc++.h>
using namespace std;
int arr[100];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n;
  int a, b, best;
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> arr[i];
  a = b = -1;
  best = INT_MAX;
  for (int i = 0; i < n - 1; ++i) {
    if (abs(arr[i] - arr[i + 1]) < best) {
      a = i;
      b = i + 1;
      best = abs(arr[i] - arr[i + 1]);
    }
  }
  if (abs(arr[n - 1] - arr[0]) < best) {
    a = n - 1;
    b = 0;
  }
  cout << a + 1 << ' ' << b + 1 << '\n';
}
