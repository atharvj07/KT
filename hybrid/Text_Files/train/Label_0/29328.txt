#include <bits/stdc++.h>
const int N = 100005;
using namespace std;
int main() {
  int arr[N] = {0};
  int n, i;
  cin >> n;
  for (i = 0; i < n; i++) {
    int a;
    cin >> a;
    arr[a]++;
  }
  int ans = 1;
  for (i = 2; i < N; i++) {
    int maxi = 0;
    for (int j = i; j < N; j += i) maxi += arr[j];
    ans = max(ans, maxi);
  }
  cout << ans << endl;
}
