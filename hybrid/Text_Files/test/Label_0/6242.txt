#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string str;
  cin >> str;
  long long n = (int)str.size(), min_ind = 0;
  cout << "Mike"
       << "\n";
  char mini = str[0];
  for (int i = 1; i < n; i++) {
    if (mini < str[i])
      cout << "Ann"
           << "\n";
    else {
      mini = str[i];
      cout << "Mike"
           << "\n";
    }
  }
  return 0;
}
