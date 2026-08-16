#include <bits/stdc++.h>
using namespace std;
int main() {
  long long leftsum = 0, rightsum = 0;
  long n, index = -1;
  cin >> n;
  int left[n], right[n];
  for (long i = 0; i < n; ++i) {
    cin >> left[i];
    cin >> right[i];
    leftsum += left[i];
    rightsum += right[i];
  }
  int max = abs(leftsum - rightsum);
  int ans;
  for (int i = 0; i < n; ++i) {
    leftsum -= left[i];
    leftsum += right[i];
    rightsum -= right[i];
    rightsum += left[i];
    if (abs(leftsum - rightsum) > max) {
      index = i;
      max = abs(leftsum - rightsum);
    }
    leftsum -= right[i];
    leftsum += left[i];
    rightsum -= left[i];
    rightsum += right[i];
  }
  if (index != -1)
    cout << index + 1 << endl;
  else
    cout << "0" << endl;
}
