#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, ta, b, tb;
  cin >> a >> ta >> b >> tb;
  string st;
  cin >> st;
  int min = (stoi(st.substr(0, 2)) * 60 + stoi(st.substr(3, 5)));
  vector<int> arr;
  for (int i = 300; i < (24 * 60); i += b) arr.push_back(i);
  int s = upper_bound(arr.begin(), arr.end(), min - tb) - arr.begin();
  int e = lower_bound(arr.begin(), arr.end(), min + ta - 1) - arr.begin();
  if (!binary_search(arr.begin(), arr.end(), min + ta - 1)) e--;
  cout << (e - s + 1);
}
