#include <iostream>
#include <cmath>
using namespace std;

int main(){
  int n,s,a,b;
  while(cin>>a>>b>>n){
    s=0;
    a%=b;
    for(int i=1;i<=n;i++){
      a*=10;
      s+=a/b;
      a%=b;
    }
    cout<<s<<endl;
  }
  return 0;
}