#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  string arr[n];
  int i = 0;
  for (i = 0; i < n; i++) cin >> arr[i];
  int count = 0, cnt = 0;
  for (i = 0; i < n; i++) {
    if (arr[i][0] == s[0] && arr[i][1] == s[1] && arr[i][2] == s[2])
      count++;
    else
      cnt++;
  }
  if (cnt == count)
    cout << "home";
  else
    cout << "contest";
  return 0;
}
