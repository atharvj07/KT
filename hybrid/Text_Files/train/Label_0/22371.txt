#include <cstdio>

int prim[10000000];

int main()
{

	int n, i, j;

	for( i = 2; i < 10000000 / 2; i++ ){

		for( j = 2; j < 10000000 / 2; j++ ){

			if( i * j > 10000000 || prim[i] == 1 ) break;
			
			prim[i*j] = 1;

		}

	}

	while( 1 ){

		scanf( "%d", &n );

		if( n == 0 ) break;

		for( i = n; n >= 0; i-- ){

			if( prim[i] == 0 ){

				if( prim[i-2] == 0 && prim[i-6] == 0 && prim[i-8] == 0 ){

					printf( "%d\n", i );

					break;

				}

			}

		}

	}

	return 0;

}