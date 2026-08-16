#include <bits/stdc++.h>

using namespace std ;

#define inf 0x3f3f3f3f
#define ll long long

ll n , s ;

ll f( ll b , ll n )
{
	return n < b ? n : f( b , n / b ) + n % b ;
}

int main()
{
	scanf( "%lld%lld" , &n , &s ) ;
	if( s > n ) return puts( "-1" ) , 0 ;
	if( s == n ) return printf( "%lld\n" , n + 1 ) , 0 ;
	ll m = sqrt( n ) + 1 ;
	for( ll i = 2 ; i <= m ; i ++ )
	{
		if( f( i , n ) == s )
			return printf( "%lld" , i ) , 0 ;
	}
	ll ans = 1e11 ;
	n -= s ;
	for( ll i = 1 ; i * i <= n ; i ++ )
	{
		if( n % i == 0 )
		{
			ll b = n / i + 1;
			if( f ( b , n + s ) ==  s ) ans = min ( ans , b ) ;
		}
	}
	printf( "%lld\n" , ans != 1e11 ? ans : -1 ) ;
	return 0 ;
}