#include<iostream>
using namespace std;
int main(){
  int n,m,t,mt,tt;
  while(cin>>n){
    if(n==0) break;
    mt = 0;
    tt = 0;
    for(int i=0;i<n;i++){
      cin >> m >> t;
      if(m>t) mt += (m+t);
      else if(t>m) tt += (m+t);
      else{
	mt += m;
	tt += t;
      }
    }
    cout << mt << ' ' << tt << endl;
  }
  return 0;
}