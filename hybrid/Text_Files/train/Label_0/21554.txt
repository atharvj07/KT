#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string second;
  cin >> second;
  int n = second.length();
  vector<int> AB;
  vector<int> BA;
  for (int i = 0; i < n - 1; i++) {
    if (second[i] == 'A' && second[i + 1] == 'B') AB.push_back(i);
    if (second[i] == 'B' && second[i + 1] == 'A') BA.push_back(i);
  }
  sort(AB.begin(), AB.end());
  sort(BA.begin(), BA.end());
  bool possible = false;
  if (AB.size() == 0 or BA.size() == 0) {
    cout << "NO\n";
    return 0;
  }
  if (abs(AB[0] - BA[BA.size() - 1]) > 1) possible = true;
  if (abs(BA[0] - AB[AB.size() - 1]) > 1) possible = true;
  if (possible)
    cout << "YES\n";
  else
    cout << "NO\n";
  return 0;
}
