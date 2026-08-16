#include <bits/stdc++.h>
using namespace std;
bool myfunction(int i, int j) { return (i > j); }
int main() {
  int n, i = 0, j = 0;
  long int d, count = 0;
  cin >> n;
  cin >> d;
  vector<long int> numbers(n);
  for (i = 0; i < n; i++) {
    cin >> numbers.at(i);
  }
  sort(numbers.begin(), numbers.end(), myfunction);
  for (i = 0; i < (n - 1); i++) {
    for (j = i + 1; j < n; j++) {
      if (numbers.at(i) - numbers.at(j) <= d) {
        count++;
      } else {
        break;
      }
    }
  }
  cout << count * 2 << endl;
}
