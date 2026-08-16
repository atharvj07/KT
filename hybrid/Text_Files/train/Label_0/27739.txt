#include <bits/stdc++.h>
using namespace std;
long long a, n, vv[10000001];
int main() {
  cin >> a >> n;
  for (int i = a; i < a + n; i++) vv[i] = i;
  for (int i = 2; i * i < (a + n); i++) {
    for (int j = 1; j * i * i < (a + n); j++) vv[j * i * i] = j;
  }
  long long sum = 0;
  for (int i = a; i < a + n; i++) sum += vv[i];
  cout << sum;
  return 0;
}
