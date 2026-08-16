#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
  int W, H, n;
  cin >> W >> H >> n;
  int w=0, h=0;
  rep(i,n) {
    int x, y, A;
    cin >> x >> y >> A;
    if(A==1) w=max(w,x);
    else if(A==2) W=min(W,x);
    else if(A==3) h=max(h,y);
    else if(A==4) H=min(H,y);
  }
  int ans = (W-w)*(H-h);
  if(W-w<0||H-h<0) ans = 0;
  
  cout << ans << endl;
}
