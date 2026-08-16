#include <bits/stdc++.h>
using namespace std;
string s[100005];
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    cin >> s[i];
  }
  int len = s[1].length();
  for (int i = 0; i < len; ++i) {
    set<char> st;
    for (int j = 1; j <= n; ++j) {
      if (s[j][i] >= 'a' && s[j][i] <= 'z') {
        st.insert(s[j][i]);
      }
    }
    if (st.size() == 0) {
      printf("a");
    } else if (st.size() == 1) {
      printf("%c", *st.begin());
    } else {
      printf("?");
    }
  }
  printf("\n");
}
