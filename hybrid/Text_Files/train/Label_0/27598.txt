#include <bits/stdc++.h>
using namespace std; 
    
int main(){
  int A,B,H,M;
  cin >> A >> B >> H >> M;
  double C=acos(-1)*(60*H+M)/360-acos(-1)*M/30;
  double ans=sqrt(A*A+B*B-2*A*B*cos(C));
  cout << fixed << setprecision(15) << ans << endl;
}
  