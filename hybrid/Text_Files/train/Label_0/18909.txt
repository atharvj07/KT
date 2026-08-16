#include <bits/stdc++.h>
using namespace std;
int main(){
  long long n,mon=1,ans=0;
cin>>n;
while(1){
  if(n>=mon*2-1){++ans;}
else{break;}
mon*=2;
}
cout<<ans<<endl;
}
