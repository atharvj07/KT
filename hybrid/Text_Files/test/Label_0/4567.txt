#include <iostream>
#include <algorithm>
#include <cstdio>
#include <climits>

static int const N = 100;

int main()
{
  for(;;) {
    int n, m;
    std::cin >> n;
    if ( n == 0 )
      break;

    std::cin >> m;
    int G[N][N] = {};
    for( int i=0; i<N; ++i )
      std::fill( G[i], G[i] + N, INT_MAX );

    for( int i=0; i<m; ++i ) {
      int a, b, l;
      std::scanf( "%d,%d,%d", &a, &b, &l );
      l = l / 100 - 1;
    
      G[a][b] = G[b][a] = l;
    }

    int d[N], p[N] = {};
    bool visited[N] = {};
    std::fill( d, d + N, INT_MAX );
    std::fill( visited, visited + N, false );

    // initialize
    int u = 0;
    d[u] = 0;
    p[u] = -1;
    
    int sum = 0;

    for( int i=0; i<n; ++i ) {
      int tmp = INT_MAX;
      for( int j=0; j<n ; ++j ) {
	if ( !visited[j] && d[j] < tmp ) {
	  u = j;
	  tmp = d[j];
	}
      }
      visited[u] = true;
      sum += d[u];
            
      for( int j=0; j<n; ++j ) {
	if ( !visited[j] && G[u][j] < d[j] ) {
	  d[j] = G[u][j];
	  p[j] = u;
       	}
      }
    }
    std::cout << sum << std::endl;
  }
}