#include<bits/stdc++.h>
using namespace std;

int n,m;
double x[1000],y[1000],z[1000];
double tx,ty,tz,ar;

double dot(double ax,double ay,double az,
           double bx,double by,double bz){
  return ax*bx+ay*by+az*bz;
}

int calc(double sx,double sy,double sz){
  double S=sqrt(sx*sx+sy*sy+sz*sz);
  double T=sqrt(tx*tx+ty*ty+tz*tz);
  double Cos = dot(tx,ty,tz,sx,sy,sz)/T/S;
  double ti=acos(Cos);

  if(ti < ar + 0.00000001 ){
    return 1;
  }else{
    return 0;
  }
}
bool flg[1000];
int main(){
  while(cin>>n&&n){
    for(int i=0;i<n;i++){
      flg[i]=false;
      cin>>x[i]>>y[i]>>z[i];
    }
    cin>>m;
    for(int i=0;i<m;i++){
      cin>>tx>>ty>>tz>>ar;
      for(int j=0;j<n;j++){
        if(calc(x[j],y[j],z[j]))flg[j]=true;
      }
    }
    int ans=0;
    for(int i=0;i<n;i++)ans+=flg[i];
    cout<<ans<<endl;
  }
  return 0;
}