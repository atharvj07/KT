#include <bits/stdc++.h>
using namespace std;
void solver(void);
long long int MOD = 1e9 + 7;
double pi = 2 * acos(0.0);
int main() {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  while (t--) solver();
}
void solver(void) {
  long long int n;
  cin >> n;
  string str;
  cin >> str;
  bool cycle = true;
  long long int indx = str.find('<');
  if (indx != string ::npos) {
    for (long long int i = 0; i < n; i++) {
      if (str[i] == '>') cycle = false;
    }
  }
  long long int indx1 = str.find('>');
  if (indx1 != string ::npos) {
    for (long long int i = 0; i < n; i++) {
      if (str[i] == '<') cycle = false;
    }
  }
  if (cycle) {
    cout << n << "\n";
    return;
  } else {
    long long int cnt = 0;
    for (long long int i = 0; i < n; i++) {
      if (i == 0) {
        if (str[0] == '-' || str[n - 1] == '-') cnt++;
      } else {
        if (str[i - 1] == '-' || str[i] == '-') cnt++;
      }
    }
    cout << cnt << "\n";
  }
}
