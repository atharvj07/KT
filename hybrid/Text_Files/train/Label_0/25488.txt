#include <bits/stdc++.h>
using namespace std;
int main() {
  string s, t, s1;
  cin >> s;
  cin >> t;
  int l = s.size();
  s1 = s;
  for (int i = l - 1; i >= 0; i--) {
    if (s[i] == 'z') {
      s[i] = 'a';
    } else {
      s[i] = s[i] + 1;
      break;
    }
  }
  if (s > s1 && s < t) {
    cout << s << endl;
  } else {
    printf("No such string\n");
  }
  return 0;
}
