#include<iostream>
#include<cmath>
#include<cstdio>
#include<complex>
using namespace std;

typedef complex<double> Point;

#define EPS (1e-10)
#define EQ(a,b) (abs((a)-(b)) < EPS)
#define EQV(a,b) ( EQ( (a).real() , (b).real() ) && EQ( (a).imag(), (b).imag() ) )

double abs(Point a,Point b) {
  return sqrt( (a.real()-b.real())*(a.real()-b.real()) + (a.imag()-b.imag())*(a.imag()-b.imag()) );
}

double cross(Point a,Point b) {
  return (a.real()*b.imag()- a.imag()*b.real());
}

// àÏ : aEb
double dot(Point a,Point b) {
  return (a.real()*b.real() + a.imag()*b.imag());
}

//¼üÌ½s»è
int is_parallel(Point a1,Point a2,Point b1,Point b2){
  return EQ( cross(a1-a2,b1-b2) , 0.0 );
}

// _a,bð[_Æ·éüªÆ_cÆÌ£
double distance_ls_p(Point a, Point b, Point c) {
  if ( dot(b-a, c-a) < EPS ) return abs(c-a);
  if ( dot(a-b, c-b) < EPS ) return abs(c-b);
  return abs(cross(b-a, c-a)) / abs(b-a);
}

int main() {

  double D;
  while(true) {
    cin>>D;
    if(D==0) break;

    double vx,vy,px,py,st;
    cin>>px>>py>>vx>>vy;

    Point as = Point(px,py);
    Point g = Point(0,0);
    Point at = Point(px+vx,py+vy);
    if( !is_parallel( as, g, at, as ) ) goto NO;

    st = distance_ls_p( as, at, g );
    if( EPS <  abs( as, g ) - st ) {
      if( abs( as, g ) > D ) goto NO;
      printf("%.10lf\n", abs(as,g));
    } else if( abs( abs( as, g ) - st ) < EPS ){
      if( 2 - abs( as, g ) > D ) goto NO;
      printf("%.10lf\n", 2-abs(as,g) );
    }
    continue;

  NO:
    printf("impossible\n");
  }
}