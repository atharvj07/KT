#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  string x;
  cin>>n>>x;
  int m=0;
  for(int i=0;i<n;i++)
    m+=(int)(x.at(i)-'0');
  int rp=0;
  int rm=0;
  for(int i=0;i<n;i++){
    rp=(rp*2+(int)(x.at(i)-'0'))%(m+1);
    if(m>1)
      rm=(rm*2+(int)(x.at(i)-'0'))%(m-1);
  }
  vector<int> c(n,0);
  int pp=1;
  int pm=1;
  for(int i=n-1;i>=0;i--){
    if(m==1&&x.at(i)=='1')
      continue;
    int ci=1;
    int b=(x.at(i)=='0'?(rp+pp)%(m+1):(rm-pm+m-1)%(m-1));
    while(b>0){
      ci++;
      int a=b;
      int pc=0;
      while(a>0){
        pc+=a%2;
        a/=2;
      }
      b%=pc;
    }
    c.at(i)=ci;
    pp=pp*2%(m+1);
    if(m>1)
      pm=pm*2%(m-1);
  }
  for(int i=0;i<n;i++)
    cout<<c.at(i)<<endl;
}