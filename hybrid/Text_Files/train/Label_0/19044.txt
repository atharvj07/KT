#include <bits/stdc++.h>
using namespace std;
vector<int> v1, v2;
bool arr[1000001];
void seive() {
  int k = 1000000;
  for (int i = 1; i <= k; i++) {
    arr[i] = true;
  }
  arr[0] = false, arr[1] = false;
  for (int i = 2; i <= k; i++) {
    if (arr[i] == true) {
      for (int j = 2 * i; j <= k; j += i) {
        arr[j] = false;
      }
    }
  }
  for (int i = 3; i <= k; i++) {
    if (arr[i] == true) v1.push_back(i);
  }
  for (int i = 5; i <= k; i++) {
    if (arr[i] == true) v2.push_back(i);
  }
}
int main() {
  long long int n, k;
  cin >> n;
  k = n * (n + 1) / 2;
  cout << k % 2 << endl;
  return 0;
}
