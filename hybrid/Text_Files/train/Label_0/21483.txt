#include<bits/stdc++.h>
#include<math.h>
using namespace std;

int main(){
  int W, H, N;
  cin >> W >> H >> N;
  int w[4] = {0,W,0,H}; // left, right, down, up

  int x,y,a;
  for (int i=0;i<N;i++){
    cin >> x >> y >> a;
    if (a<3) w[a-1] = (a==1)? max(x, w[a-1]) : min(x, w[a-1]);
    else w[a-1] = (a==3)? max(y, w[a-1]) : min(y, w[a-1]);
  }
  
  cout << max(0,w[1]-w[0])*max(0,w[3]-w[2]) << endl;


}