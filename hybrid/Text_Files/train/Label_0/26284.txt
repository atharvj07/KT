#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long int llINF = 0x3f3f3f3f3f3f3f;
int main() {
  int n;
  cin >> n;
  long long int a = 0, b = 0;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    a += x;
  }
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    b += x;
  }
  if (a >= b)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
}
