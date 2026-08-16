#include <bits/stdc++.h>
#define EPS (1e-8)
#define x real()
#define y imag()
using namespace std;
typedef complex <double> point;

double dot(point a,point b){return a.x*b.x+a.y*b.y;}
double cross(point a,point b){return a.x*b.y-a.y*b.x;}
 
int ccw(point a,point b,point c){
  point d = b-a;
  point e = c-a;
  if(cross(d,e)>+EPS) return 1;//"COUNTER_CLOCKWISE"
  if(cross(d,e)<-EPS) return 1;//"CLOCKWISE"
  if(dot(d,e)<0) return 2;//"ONLINE_BACK"
  if(abs(d) < abs(e)) return -2;//"ONLINE_FRONT"
  return 0;//"ON_SEGMENT"
}

int main(){
  while(1){
  double d;
  cin>>d;
  if(d<=EPS) break;
  double px,py,vx,vy;
  cin>>px>>py>>vx>>vy;
  int flg=ccw(point(0,0),point(vx,vy),point(px,py))!=1;
  double ans=abs(point(px,py));
  if(px*vx>0||py*vy>0) ans=(1-ans)+1;
  if(d<ans||d<abs(point(px,py))) flg=0;
  if(flg)printf("%lf\n",ans);
  else cout <<"impossible"<<endl;
  }
  return 0;
}