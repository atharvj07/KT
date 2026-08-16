#include <bits/stdc++.h>
using namespace std;
int n;
pair<int, int> inp[210000];
int a, b, c;
char t;
map<pair<int, int>, int> arr;
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    cin >> t >> a >> t >> b >> t >> t >> c;
    int gd = gcd(a + b, c);
    arr[{(a + b) / gd, c / gd}]++;
    inp[i] = {(a + b) / gd, c / gd};
  }
  for (int i = 0; i < n; i++) {
    cout << arr[inp[i]] << " ";
  }
  cout << "\n";
  return 0;
}
