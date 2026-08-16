#include <bits/stdc++.h>
using namespace std;
int main() {
  long long H,W,answer=INT_MAX,a,b;
  cin >> H >> W;
  if (W > 2) {
    answer = min(answer,H*((W-1)/3+1-W/3));
  } 
  if (H > 2) {
    answer = min(answer,W*((H-1)/3+1-H/3));
  }
  for (int i = 1; i < H; i++) {\
    a = min(i*W,W/2*(H-i));
    b = max(i*W,(W-1)/2*(H-i)+H-i);
    answer = min(answer,b-a);
  }
  for (int i = 1; i < W; i++) {
    a = min(i*H,H/2*(W-i));
    b = max(i*H,(H-1)/2*(W-i)+W-i);
    answer = min(answer,b-a);
  }
  cout << answer;
}