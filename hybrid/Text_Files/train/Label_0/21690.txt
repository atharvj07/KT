#include <bits/stdc++.h>
using namespace std;
template <typename T>
void SOUT(T what) {
  cout << what << endl;
}
int main() {
  int n, k;
  scanf("%d %d", &n, &k);
  if (k >= n) {
    cout << "-1\n";
    return 0;
  }
  int i = n;
  vector<int> out;
  for (; i >= 1; i--) {
    if (k > 0) {
      out.push_back(i);
      k--;
    } else
      break;
  }
  for (; i >= 2; i -= 2) {
    out.push_back(i - 1);
    out.push_back(i);
  }
  if (i == 1) out.push_back(1);
  reverse((out).begin(), (out).end());
  for (int i = 0; i < (out.size()); ++i) cout << out[i] << " ";
  cout << endl;
}
