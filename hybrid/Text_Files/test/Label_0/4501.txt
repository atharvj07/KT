#include <bits/stdc++.h>
#define fi first
#define se second

namespace IO {
  const int IN_LEN = 1 << 18 | 1;
  static char buf[IN_LEN] , *s , *t;
  inline int Getchar( void ) { return s == t && ( t = ( s = buf ) + fread( buf , 1 , IN_LEN , stdin ) ) , s == t ? -1 : *s++; }
  template <class T> inline void read( T & x ) {
    static int c , f; c = Getchar() , x = f = 0;
    while( c < '0' || c > '9' ) { if( c == '-' ) f = 1; c = Getchar(); }
    while( c <= '9' && c >= '0' ) x = x * 10 + c - 48 , c = Getchar(); 
    x = f ? -x : x;
  }
} using IO::read;

using namespace std;

typedef long long lol;
typedef pair<int,int> pii;
const int N = 2e5 + 5;

lol ans[N] , f[N][2];

struct Data {
  int x , y , id , _y;
  bool operator < ( const Data & rhs ) const {
    return x < rhs.x;
  }
  lol friend dist( Data a , Data b ) {
    return abs( a.x - b.x ) + abs( a._y - b._y );
  }
} dat[N];

int n , discre[N] , discre_tot;

inline int discreid( int x ) { return lower_bound( discre + 1 , discre + 1 + discre_tot , x ) - discre; }

int main( void ) {
  read( n );
  for( int i = 1 ; i <= n ; ++i ) {
    read( dat[i].x );
    read( dat[i].y );
    discre[i] = dat[i].y;
    dat[i]._y = dat[i].y;
    dat[i].id = i;
  }
  memset( ans , -1 , sizeof ans );
  sort( dat + 1 , dat + 1 + n );
  sort( discre + 1 , discre + 1 + n );
  discre_tot = unique( discre + 1 , discre + 1 + n ) - discre - 1;
  for( int i = 1 ; i <= n ; ++i )
    dat[i].y = discreid( dat[i].y );
  for( int i = 1 , L , R , l , r , _mono , _updl , _updr , sz , _cnt ; i <= n ; ++i )
    if( !~ans[dat[i].id] ) {
      l = r = i , L = dat[i].y , R = dat[i].y;
      _mono = 0;
      if( i < n && dat[i + 1].y == dat[i].y + 1 ) _mono = 1;
      if( i < n && dat[i + 1].y == dat[i].y - 1 ) _mono = -1;
      if( !_mono ) {
        if( i > 1 && dat[i - 1].y == dat[i].y - 1 ) _mono = 1;
        if( i > 1 && dat[i - 1].y == dat[i].y + 1 ) _mono = -1;
      }
      if( !_mono ) {
        ans[dat[i].id] = 0;
        continue;
      }
      vector<pii> layer;
      vector<int> cnt;
      while( 114514 ) {
        _updl = _updr = _cnt = 0;
        while( l > 1 && dat[l - 1].y == L - _mono ) --l , L -= _mono , _updl = 1 , ++_cnt;
        while( r < n && dat[r + 1].y == R + _mono ) ++r , R += _mono , _updr = 1 , ++_cnt;
        if( _updl || _updr ) {
          cnt.push_back( _cnt );
          if( !layer.size() ) layer.push_back( pii( l , r ) );
          else {
            int _l = l , _r = r;
            if( !_updl ) _l = r - _cnt + 1;
            if( !_updr ) _r = l + _cnt - 1;
            layer.push_back( pii( _l , _r ) );
          }
          swap( L , R );
          _mono = -_mono;
        } else break;
      }
      sz = layer.size();
      memset( f , 0x3f , sizeof( int ) * 2 * sz );
      f[sz - 1][0] = f[sz - 1][1] = 0;
      for( int _ = sz - 2 , l , r , _l , _r , _t ; ~_ ; --_ ) {
        l = layer[_].fi , r = layer[_].se;
        _l = layer[_+1].fi , _r = layer[_+1].se;
        _t = cnt[_+1];
        f[_][0] = min( dist( dat[l] , dat[_r] ) + f[_+1][0] , dist( dat[l] , dat[_l] ) + f[_+1][1] ) + dist( dat[_l] , dat[_r] ) - _t;
        f[_][1] = min( dist( dat[r] , dat[_r] ) + f[_+1][0] , dist( dat[r] , dat[_l] ) + f[_+1][1] ) + dist( dat[_l] , dat[_r] ) - _t;
      }
      l = layer[0].fi , r = layer[0].se;
      for( int _ = l ; _ <= r ; ++_ )
        ans[dat[_].id] = min( dist( dat[_] , dat[r] ) + f[0][0] , dist( dat[_] , dat[l] ) + f[0][1] ) + dist( dat[l] , dat[r] ) - ( r - l );
    }
  for( int i = 1 ; i <= n ; ++i )
    printf("%lld\n",ans[i]);
  return 0;
}
