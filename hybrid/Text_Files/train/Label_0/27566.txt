#include <bits/stdc++.h>
using namespace std;
int main(){
  long long a,b,c,ans=0; cin>>a>>b>>c;
  while(a%2==0 && b%2==0 && c%2==0){
    ans++;
    long long aa,bb,cc;
    aa=b/2+c/2;
    bb=c/2+a/2;
    cc=a/2+b/2;
    a=aa, b=bb, c=cc;
    if(a==b && b==c){
      ans=-1;
      break;
    }
  }
  cout<<ans<<endl;
}
