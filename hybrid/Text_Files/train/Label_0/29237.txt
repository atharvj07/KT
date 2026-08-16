#include <bits/stdc++.h>

using namespace std;

long long n, p;

int
main()
{
	cin >> n >> p;
	if( n == 1 )
	{
		cout << p << endl;
		return 0;
	}
	if( n > 40 )
	{
		cout << 1 << endl;
		return 0;
	}
	long long x = static_cast<long long>( ceil( sqrt( p ) ) );
	while( ( p % x ) != 0 || ( p % static_cast<long long>( pow( x, n ) ) ) != 0 ) --x;
	cout << x << endl;
	return 0;
}
