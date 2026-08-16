#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long int mod = 1e9 + 7;
  string str;
  cin >> str;
  int a = 0, b = 0, counter = 0;
  for (int i = str.size() - 1; i >= 0; i--) {
    if (str[i] == 'b') {
      b = (b + 1) % mod;
    } else {
      counter = (counter + b) % mod;
      b = (2 * b) % mod;
    }
  }
  cout << counter;
}
