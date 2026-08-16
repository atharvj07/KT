#include <bits/stdc++.h>
using namespace std;
void machayenge() {
  char arr[] = {'a', 'b', 'c', 'd'};
  long long int n;
  cin >> n;
  string s;
  long long int t = n / 4;
  t *= 4;
  long long int k = 0;
  for (long long int i = 0; i < t; ++i) {
    s += arr[i % 4];
    k = (k + 1) % 4;
  }
  t = n % 4;
  while (t--) {
    s += arr[k];
    k = (k + 1) % 4;
  }
  cout << s;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(0);
  machayenge();
  return 0;
}
