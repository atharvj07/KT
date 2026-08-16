#include <bits/stdc++.h>
using namespace std;

int main() {
  int l,r,n;
  cin >> l >> r >> n;
  int d[1111];
  memset(d,0,sizeof(d));
  for(int i=0; i<n; i++) {
    int x,y;
    cin >> x >> y;
    for(int j=x; j<y; j++) d[j]=1;
  }
  for(int i=l; i<r; i++) {
    if(d[i]) {
      cout << 1 << endl;
      return 0;
    }
  }
  cout << 0 << endl;
  return 0;
}
