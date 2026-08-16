#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  vector<long long> v1(n + 1), dp1(n + 1), dp2(n + 1);
  for (long long i = 1; i <= n; ++i) {
    cin >> v1[i];
  }
  dp1[1] = 1;
  for (long long i = 2; i <= n; ++i) {
    if (v1[i] > v1[i - 1])
      dp1[i] = dp1[i - 1] + 1;
    else
      dp1[i] = 1;
  }
  dp2[1] = 1;
  bool de = false;
  for (long long i = 2; i <= n; ++i) {
    if (v1[i] < v1[i - 1]) {
      de = true;
      if (i - 2 >= 1) {
        if (v1[i] > v1[i - 2]) {
          dp2[i] = dp1[i - 2] + 1;
        } else {
          dp2[i] = dp1[i];
        }
      } else {
        dp2[i] = dp1[i];
      }
    } else if (v1[i] > v1[i - 1]) {
      if (de == true) {
        de = false;
        if (v1[i] > v1[i - 2]) {
          dp2[i] = dp1[i - 2] + 1;
        } else {
          dp2[i] = dp2[i - 1] + 1;
        }
      } else {
        dp2[i] = dp2[i - 1] + 1;
      }
    } else {
      de = false;
      dp2[i] = dp2[i - 1];
    }
  }
  long long maxi = *max_element(dp2.begin(), dp2.end());
  cout << maxi;
}
