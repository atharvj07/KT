#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  string s_begin = "I hate ", s_end = "it";
  string y = "that I hate ", x = "that I love ";
  cout << s_begin;
  for (int i = 2; i <= n; i++) {
    if (i % 2 == 0)
      cout << x;
    else
      cout << y;
  }
  cout << s_end << endl;
}
