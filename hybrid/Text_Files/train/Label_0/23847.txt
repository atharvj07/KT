#include <bits/stdc++.h>
using namespace std;
string s;
vector<int> v;
int main() {
  int n;
  cin >> n >> s;
  for (int i = 2; i <= n; i++) {
    if (n % i == 0) {
      v.push_back(i);
    }
  }
  int len = s.size();
  for (int x = 0; x < (int)v.size(); x++) {
    int i = v[x];
    string s1 = s.substr(0, i);
    string s2 = s.substr(i, len - i);
    reverse(s1.begin(), s1.end());
    s = s1 + s2;
  }
  cout << s << endl;
}
