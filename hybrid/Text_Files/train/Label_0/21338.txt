#include <bits/stdc++.h>
using namespace std;
const int N = 100100;
int m[N];
int a[N];
int level[N];
long long sums[N];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> m[i];
  }
  sums[0] = 0;
  for (int i = 1; i < N; ++i) {
    sums[i] = i + sums[i - 1];
  }
  long long marks = 0;
  long long sum = 0;
  for (int i = 0; i < n; ++i) {
    if (m[i] + 1 > marks) {
      marks = m[i] + 1;
    }
    level[i] = marks;
  }
  int currently_building = level[n - 1];
  for (int i = n - 1; i >= 0; --i) {
    currently_building = max(currently_building, level[i]);
    a[i] = currently_building;
    currently_building--;
    sum += a[i] - 1 - m[i];
  }
  cout << sum;
  return 0;
}
