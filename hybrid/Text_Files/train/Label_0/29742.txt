#include <bits/stdc++.h>
using namespace std;
int a[200];
int main() {
  int n;
  scanf("%d", &n);
  getchar();
  while (n--) {
    string str;
    cin >> str;
    set<char> s;
    for (int i = 0; i < str.size(); ++i) {
      s.insert(str[i]);
    }
    if (s.size() == 1)
      cout << -1 << endl;
    else {
      sort(str.begin(), str.end());
      cout << str << endl;
    }
  }
  return 0;
}
