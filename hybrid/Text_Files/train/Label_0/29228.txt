#include <bits/stdc++.h>
using namespace std;
int main() {
  int num;
  int temp1, temp2;
  cin >> num;
  vector<int> vi1, vi2, vi3;
  for (int i = 0; (i) < (num); i++) {
    cin >> temp1 >> temp2;
    vi1.push_back(temp1);
    vi2.push_back(temp2);
    vi3.push_back(temp1);
    vi3.push_back(temp2);
  }
  sort((vi3).begin(), (vi3).end());
  ;
  int lim = vi3[num - 1];
  for (int i = 0; (i) < (num); i++) {
    if (i < num / 2)
      cout << 1;
    else if (vi1[i] <= lim)
      cout << 1;
    else
      cout << 0;
  }
  cout << endl;
  for (int i = 0; (i) < (num); i++) {
    if (i < num / 2)
      cout << 1;
    else if (vi2[i] <= lim)
      cout << 1;
    else
      cout << 0;
  }
  cout << endl;
  return 0;
}
