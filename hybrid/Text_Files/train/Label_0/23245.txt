#include <bits/stdc++.h>
using namespace std;
int main(int argc, char** argv) {
  int pages;
  cin >> pages;
  int week[7];
  for (int i = 0; i < 7; i++) {
    cin >> week[i];
  }
  int count = 0;
  int day = 0;
  while (count < pages) {
    for (int i = 0; i < 7; i++) {
      count += week[i];
      if (count >= pages) {
        cout << i + 1 << endl;
        break;
      }
    }
  }
  return 0;
}
