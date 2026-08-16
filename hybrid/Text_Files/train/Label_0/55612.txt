import java.util.*;

class Point
{
	final double X;
	final double Y;

	public Point( double x, double y )
	{
		X = x;
		Y = y;
		return;
	}

	public Point minus( final Point p )
	{
		return new Point( X - p.X, Y - p.Y );
	}

	public double dot( final Point p )
	{
		return X * p.X + Y * p.Y;
	}

	public double cross( final Point p )
	{
		return X * p.Y - Y * p.X;
	}

	public double arg()
	{
		return Math.atan2( Y, X );
	}
}

class Edge
{
	final int to;
	final int rev;
	final int id;
	final Point angle;

	public Edge( int t, int r, int i, Point a )
	{
		to = t;
		rev = r;
		id = i;
		angle = a;
		return;
	}
}

// public class DualGraphBuilder
class DualGraphBuilder
{
	final int N;
	int M;

	final ArrayList< Point > ps_;
	final ArrayList< ArrayList< Edge > > G;
	final ArrayList< ArrayList< Integer > > edge_indices_, edge_positions_;
	final ArrayList< ArrayList< Boolean > > used_;

	int outer_ = -1;
	final ArrayList< ArrayList< Point > > areas_;

	ArrayList< ArrayList< Integer > > intersects_;


	public DualGraphBuilder( final ArrayList< ArrayList< Double > > coordinates )
	{
		N = coordinates.size();
		M = 0;
		ps_ = new ArrayList< Point >( N );

		G = new ArrayList< ArrayList< Edge > >( N );
		for ( int i = 0; i < N; ++i )
		{
			G.add( new ArrayList< Edge >() );
		}

		edge_indices_ = new ArrayList< ArrayList< Integer > >( N );
		for ( int i = 0; i < N; ++i )
		{
			edge_indices_.add( new ArrayList< Integer >() );
		}

		edge_positions_ = new ArrayList< ArrayList< Integer > >( Collections.nCopies( N, null ) );
		used_ = new ArrayList< ArrayList< Boolean > >( Collections.nCopies( N, null ) );
		areas_ = new ArrayList< ArrayList< Point > >();

		for ( ArrayList< Double > p : coordinates )
		{
			ps_.add( new Point( p.get( 0 ), p.get( 1 ) ) );
		}

		return;
	}

	public void connect( final int a, final int b )
	{
		G.get( a ).add( new Edge( b, G.get( b ).size(), M, ps_.get( b ).minus( ps_.get( a ) ) ) );
		G.get( b ).add( new Edge( a, G.get( a ).size() - 1, M, ps_.get( a ).minus( ps_.get( b ) ) ) );
		++M;

		return;
	}

	public void solve()
	{
		sortEdges();

		for ( int v = 0; v < N; ++v )
		{
			for ( int i = 0; i < G.get( v ).size(); ++i )
			{
				if ( used_.get( v ).get( i ) )
				{
					continue;
				}

				dfs( v, i );
			}
		}

		return;
	}

	private void sortEdges()
	{
		for ( int v = 0; v < N; ++v )
		{
			edge_indices_.get( v ).ensureCapacity( G.get( v ).size() );
			for ( int i = 0; i < G.get( v ).size(); ++i )
			{
				edge_indices_.get( v ).add( i );
			}

			final int vv = v;
			Collections.sort( edge_indices_.get( v ), ( Integer i, Integer j )->
					Double.compare( G.get( vv ).get( i ).angle.arg(), G.get( vv ).get( j ).angle.arg() ) );

			edge_positions_.set( v, new ArrayList< Integer >( Collections.nCopies( G.get( v ).size(), 0 ) ) );
			for ( int i = 0; i < G.get( v ).size(); ++i )
			{
				edge_positions_.get( v ).set( edge_indices_.get( v ).get( i ), i );
			}

			used_.set( v, new ArrayList< Boolean >( Collections.nCopies( G.get( v ).size(), false ) ) );
		}

		intersects_ = new ArrayList< ArrayList< Integer > >( M );
		for ( int i = 0; i < M; ++i )
		{
			intersects_.add( new ArrayList< Integer >() );
		}

		return;
	}

	private void dfs( final int sv, final int se )
	{
		ArrayList< Point > area = new ArrayList< Point >();

		for ( int v = sv, e = se; area.isEmpty() || v != sv; )
		{
			used_.get( v ).set( e, true );
			area.add( ps_.get( v ) );
			intersects_.get( G.get( v ).get( e ).id ).add( areas_.size() );

			final int r = G.get( v ).get( e ).rev;
			v = G.get( v ).get( e ).to;
			e = edge_indices_.get( v ).get( ( edge_positions_.get( v ).get( r ) + G.get( v ).size() - 1 ) % G.get( v ).size() );
		}

		{
			double theta = 0;
			for ( int i = 0; i < area.size(); ++i )
			{
				final Point p1 = area.get( ( i + 1 ) % area.size() ).minus( area.get( i ) );
				final Point p2 = area.get( ( i + 2 ) % area.size() ).minus( area.get( ( i + 1 ) % area.size() ) );
				theta += Math.atan2( p1.cross( p2 ), p1.dot( p2 ) );
			}
			if ( theta < 0 )
			{
				outer_ = areas_.size();
			}
		}

		areas_.add( area );

		return;
	}

	public int areaNumber()
	{
		return areas_.size();
	}

	public ArrayList< ArrayList< Point > > areas()
	{
		return areas_;
	}

	public ArrayList< ArrayList< Integer > > edges()
	{
		ArrayList< ArrayList< Integer > > res = new ArrayList< ArrayList< Integer > >( intersects_.size() );
		for ( ArrayList< Integer > row : intersects_ )
		{
			ArrayList< Integer > r = new ArrayList< Integer >( 2 );
			r.add( row.get( 0 ) );
			r.add( row.get( 1 ) );
			res.add( r );
		}
		return res;
	}

	public int outer()
	{
		return outer_;
	}

}

class Main
{
	public static void main( String[] args )
	{
		Scanner scanner = new Scanner( System.in );

		while ( true )
		{
			final int N = scanner.nextInt();
			final int M = scanner.nextInt();
			
			if ( N == 0 && M == 0 )
			{
				break;
			}

			ArrayList< ArrayList< Double > > coordinates = new ArrayList< ArrayList< Double > >( N );
			for ( int i = 0; i < N; ++i )
			{
				final int X = scanner.nextInt();
				final int Y = scanner.nextInt();
				ArrayList< Double > row = new ArrayList< Double >( 2 );
				row.add( (double)X );
				row.add( (double)Y );
				coordinates.add( row );
			}

			DualGraphBuilder dualgraph = new DualGraphBuilder( coordinates );
			for ( int i = 0; i < M; ++i )
			{
				final int u = scanner.nextInt() - 1;
				final int v = scanner.nextInt() - 1;
				dualgraph.connect( u, v );
			}
			dualgraph.solve();

			final int dN = dualgraph.areaNumber();
			ArrayList< ArrayList< Integer > > dG = new ArrayList< ArrayList< Integer > >( dN );
			for ( int i = 0; i < dN; ++i )
			{
				dG.add( new ArrayList< Integer >() );
			}

			for ( ArrayList< Integer > e : dualgraph.edges() )
			{
				final int u = e.get( 0 );
				final int v = e.get( 1 );
				dG.get( u ).add( v );
				dG.get( v ).add( u );
			}

			final int INF = dN * 2;
			final int s = dualgraph.outer();

			ArrayList< Integer > distances = new ArrayList< Integer >( dN );
			for ( int i = 0; i < dN; i++ )
			{
				distances.add( INF );
			}
			distances.set( s, 0 );

			Queue< Integer > que = new ArrayDeque< Integer >();
			que.add( s );

			while ( !que.isEmpty() )
			{
				final int u = que.poll();

				for ( int v : dG.get( u ) )
				{
					if ( distances.get( v ).equals( INF ) )
					{
						distances.set( v, distances.get( u ) + 1 );
						que.add( v );
					}
				}
			}

			final int res = Collections.max( distances );
			System.out.printf( "%d\n", res );
		}

		return;
	}
}