#include <bits/stdc++.h>
using namespace std;
vector<int> v;
int main() {
  string s;
  cin >> s;
  int i;
  for (i = 0; i < s.size(); i++) {
    if (s[i] == 'r') {
      printf("%d\n", i + 1);
    } else {
      v.push_back(i + 1);
    }
  }
  for (i = v.size() - 1; i >= 0; i--) {
    printf("%d\n", v[i]);
  }
}
