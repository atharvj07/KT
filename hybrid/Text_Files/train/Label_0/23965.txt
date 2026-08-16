#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  char s[16];
  string two = "2";
  string three = "3";
  string four = "322";
  string five = "5";
  string six = "53";
  string seven = "7";
  string eight = "7222";
  string nine = "7332";
  cin >> n;
  cin >> s;
  string ans;
  int r;
  for (int i = 0; i < strlen(s); i++) {
    r = s[i] - 48;
    switch (r) {
      case 2:
        ans = ans + two;
        break;
      case 3:
        ans = ans + three;
        break;
      case 4:
        ans = ans + four;
        break;
      case 5:
        ans = ans + five;
        break;
      case 6:
        ans = ans + six;
        break;
      case 7:
        ans = ans + seven;
        break;
      case 8:
        ans = ans + eight;
        break;
      case 9:
        ans = ans + nine;
        break;
      default:
        break;
    }
  }
  sort(ans.begin(), ans.end());
  reverse(ans.begin(), ans.end());
  cout << ans;
}
