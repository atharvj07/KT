#include <iostream>
#define A  600
#define B  800
#define C 1000
#define D 1200
#define E 1400
#define F 1600
#define Z    0

using namespace std;

int rmn_max( int x, int y ){
  return x > y ? x : y;
}

int main(){
  int n;
  while( 1 ){
    cin >> n;
    if( !n ){ return 0; }
    int cost = 0;
    for( int i = 0; i < n; i++ ){
      int x, y, h, w;
      cin >> x >> y >> h >> w;
      int ml = x + y + h;
      
      int lcost = A;
      if( ml > 160 ){
        lcost = Z;
      }else if( ml > 140 ){
        lcost = F;
      }else if( ml > 120 ){
        lcost = E;
      }else if( ml > 100 ){
        lcost = D;
      }else if( ml > 80 ){
        lcost = C;
      }else if( ml > 60 ){
        lcost = B;
      }else{
        lcost = A;
      }
      if( lcost == Z ||  w > 25 ){
        lcost = Z;
      }else if( w > 20 ){
        lcost = rmn_max( F, lcost );
      }else if( w > 15 ){
        lcost = rmn_max( E, lcost );
      }else if( w > 10 ){
        lcost = rmn_max( D, lcost );
      }else if( w > 5 ){
        lcost = rmn_max( C, lcost );
      }else if( w > 2 ){
        lcost = rmn_max( B, lcost );
      }else{
        lcost = rmn_max( A, lcost );
      }
      cost += lcost;
    }
    cout << cost << endl;
  }
}