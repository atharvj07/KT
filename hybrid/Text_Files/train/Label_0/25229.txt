#include <bits/stdc++.h>
using namespace std;
int main() {
  string s;
  cin >> s;
  int n = s.size();
  int arr[300] = {0}, brr[4] = {0};
  for (int i = 0; i < n; i++) {
    if (s[i] == '!')
      brr[i % 4]++;
    else
      arr[s[i]] = i % 4;
  }
  cout << brr[arr['R']] << " " << brr[arr['B']] << " " << brr[arr['Y']] << " "
       << brr[arr['G']] << endl;
}
