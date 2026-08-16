#include <bits/stdc++.h>
using namespace std;

int buff[][7] = {
  {0, 1, 2, 4, 6, 7, 9},
  {1, 3, 4, 6, 8, 9, 11},
  {2, 4, 5, 7, 9, 10, 12},
  {4, 6, 7, 9, 11, 12, 14},
  {6, 8, 9, 11, 13, 14, 16},
  {7, 9, 10, 12, 14, 15, 17},
  {9, 11, 12, 14, 16, 17, 18}
};
int main()
{
  string S;
  int arr[7];
  
  while(cin >> S, S != "#") {
    bool f = true;
    for(int i = (1 << 19) - 1; i >= 0; i--) {
      int sum = 0;
      for(int j = 0; j < 7; j++) {
        arr[j] = 0;
        for(int k = 0; k < 7; k++) arr[j] += ((i >> buff[j][k]) & 1) << k;
        sum += (S[arr[j]] - '0') << j;
      }
      if(S[sum] != S[arr[3]]) {
        f = false;
        break;
      }
    }
    cout << (f ? "yes" : "no") << endl;
  }
}