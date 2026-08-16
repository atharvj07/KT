#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

static const double PI = acos(-1.0);

template<class T> T GCD( T x, T y ) { return x ? GCD(y%x,x) : y; }

struct Rational
{
	Rational( long long num = 0, long long den = 1 ) : n(num), d(den)
	{
		if ( n && d ) {
			long long gcd = GCD(n,d);
			n /= gcd, d /= gcd;
		} else if ( n ) {
			n = 1;
		} else if ( d ) {
			d = 1;
		}
	}

	Rational operator+( const Rational& rhs ) const
	{
        long long gcd = GCD( d, rhs.d );
		return Rational( n*(rhs.d/gcd)+d/gcd*rhs.n, gcd*(d/gcd)*(rhs.d/gcd) );
	}
	Rational operator-( const Rational& rhs ) const
	{
		return Rational( n*rhs.d-d*rhs.n, d*rhs.d );
	}
	Rational operator*( const Rational& rhs ) const
	{
        Rational r1( n, rhs.d ), r2( rhs.n, d );
		return Rational( r1.n*r2.n, r1.d*r2.d );
	}
	Rational operator/( const Rational& rhs ) const
	{
		return *this * Rational( rhs.d, rhs.n );
	}
	
    bool operator<( const Rational& rhs ) const
    {
        return n*rhs.d < rhs.n*d;
    }
	
    bool operator!=( const Rational& rhs ) const
    {
		return (rhs < *this) || (*this < rhs);
    }

    bool operator==( const Rational& rhs ) const
    {
		return !(rhs != *this);
    }

    bool operator<=( const Rational& rhs ) const
    {
		return !(rhs < *this);
    }

	Rational abs() const { return Rational(::abs(n),::abs(d)); }

	double to_f() const { return 1.0*n/d; } 

	long long n;
	long long d;
};

template<class T>
struct Vec2
{
    Vec2( T _x, T _y ) : x(_x), y(_y) {}

    double length() const { return sqrt(x*x + y*y); }

    Vec2 operator+( const Vec2& rhs ) const { return Vec2(x+rhs.x, y+rhs.y); }
    Vec2 operator-( const Vec2& rhs ) const { return Vec2(x-rhs.x, y-rhs.y); }
    Vec2 operator*( T s ) const { return Vec2(x*s, y*s); }
    T dot( const Vec2& rhs ) const { return x*rhs.x + y*rhs.y; }
    T cross( const Vec2& rhs ) const { return x*rhs.y - y*rhs.x; }

	bool operator<( const Vec2& rhs ) const
	{
		if ( x != rhs.x ) return x < rhs.x;
		return y < rhs.y;
	}
    bool operator!=( const Vec2& rhs ) const
    {
		return (rhs < *this) || (*this < rhs);
    }

    bool operator==( const Vec2& rhs ) const
    {
		return !(rhs != *this);
    }

    T x;
    T y;
};

typedef Vec2<double> VecD;
typedef Vec2<Rational> VecR;

template<class T>
T cross(const Vec2<T> &O, const Vec2<T> &A, const Vec2<T> &B)
{
    return (A-O).cross(B-O);
}

template<class T>
void ConvexHull( const vector<Vec2<T> >& point, vector<size_t>& hull )
{
    vector<pair<Vec2<T>,size_t> > P;
    for ( int i = 0; i < (int)point.size(); i++ ) {
		P.push_back( make_pair( point[i], i ) );
    }
    sort( P.begin(), P.end() );

    vector<size_t> H(2*point.size());

    int k = 0;
    for ( int i = 0; i < (int)point.size(); i++ ) {
        while ( k >= 2 && cross(P[H[k-2]].first, P[H[k-1]].first, P[i].first) <= 0 ) {
            k--;
        }
        H[k++] = i;
    }
 
    int t = k+1;
    for ( int i = point.size()-2; i >= 0; i-- ) {
        while ( k >= t && cross(P[H[k-2]].first, P[H[k-1]].first, P[i].first) <= 0 ) {
            k--;
        }
        H[k++] = i;
    }
 
    hull.resize(k);
    for ( int i = 0; i < k; i++ ) {
        hull[i] = P[H[i]].second;
    }
}

template<class T>
bool IsIntSegments( const pair<Vec2<T>,Vec2<T> >& A, const pair<Vec2<T>,Vec2<T> >& B )
{
	const Vec2<T>& A1 = A.first; const Vec2<T>& A2 = A.second;
	const Vec2<T>& B1 = B.first; const Vec2<T>& B2 = B.second;
	return ( cross(A1,A2,B1)*cross(A1,A2,B2) <= 0 && cross(B1,B2,A1)*cross(B1,B2,A2) <= 0 );
}

bool IsInsideOfConvexPolygon( const VecD& point, const vector<VecD>& poly )
{
  const size_t n = poly.size() - 1;
  VecD g = (poly[0] + poly[n/3] + poly[2*n/3]) * (1.0/3.0); 
  for ( size_t i = 0; i < poly.size()-1; i++ ) {
	  if ( IsIntSegments( make_pair(point,g), make_pair(poly[i],poly[i+1]) ) ) {
		  return false;
	  }
  }
  return true;
}

double SunshineLength( const VecD& A, const VecD& B, const vector<vector<VecD> >& shadow )
{
	vector<double> param(1,0);
	for ( size_t i = 0; i < shadow.size(); i++ ) {
		for ( size_t j = 0; j < shadow[i].size()-1; j++ ) {
			if ( !IsIntSegments( make_pair(A,B), make_pair(shadow[i][j], shadow[i][j+1]) ) ) {
				continue;
			}
			VecD d = shadow[i][j+1] - shadow[i][j];
			double d1 = fabs( cross( shadow[i][j], shadow[i][j+1], A ) );
			double d2 = fabs( cross( shadow[i][j], shadow[i][j+1], B ) );
			if ( d1 == 0 && d2 == 0 ) continue;
			double t = d1 / (d1 + d2);
			param.push_back( t );
		}
	}
	param.push_back(1);
	sort( param.begin(), param.end() );

	double ratio = 1.0;
	for ( size_t i = 0; i < param.size()-1; i++ ) {
		double p = 0.5*(param[i]+param[i+1]);
		VecD m = A + (B-A)*p;
		for ( size_t j = 0; j < shadow.size(); j++ ) {
			if ( IsInsideOfConvexPolygon( m, shadow[j] ) ) {
				ratio -= param[i+1] - param[i];
				break;
			}
		}
	}
	return ratio * sqrt((B-A).dot(B-A));
}

struct Node
{
	Node() : cur(0,0), sum(0.0) {}
	bool operator<( const Node& rhs ) const { return sum < rhs.sum; }
	VecR cur;
	vector<VecR> next;
	vector<double> weight;
	double sum;
};

int main()
{
	int N, M;
	while ( 1 )  {
	cin >> N >> M;
	if ( N==0 && M==0 ) break;
	vector<double> height(N);
	vector<vector<VecD> > vertices(N);
	for ( int i = 0; i < N; i++ ) {
		int NV;
		cin >> NV >> height[i];
		for ( int j = 0; j < NV; j++ ) {
			double x, y;
			cin >> x >> y;
			vertices[i].push_back( VecD(x,y) );
		}
	}

	vector<pair<VecR,VecR> > road;
	for ( int i = 0; i < M; i++ ) {
		int x0,y0,x1,y1;
		cin >> x0 >> y0 >> x1 >> y1;
		road.push_back( make_pair( VecR(x0,y0), VecR(x1,y1) ) );
	}

	double theta, phi;
	cin >> theta >> phi;
	phi = phi / 180 * PI;
	theta = theta / 180 * PI;
	int xs,ys,xt,yt;
	cin >> xs >> ys >> xt >> yt;
	VecR terms[2] = { VecR(xs,ys), VecR(xt,yt) };

	vector<vector<VecD> > shadow(N);
	for ( int i = 0; i < N; i++ ) {
		vector<VecD> proj;
		for ( size_t j = 0; j < vertices[i].size(); j++ ) {
			proj.push_back( vertices[i][j] );
			proj.push_back( vertices[i][j] - VecD(cos(theta),sin(theta))*(height[i]/tan(phi)) );
		}

		vector<size_t> hull;
		ConvexHull( proj, hull );
		for ( size_t j = 0; j < hull.size(); j++ ) {
			shadow[i].push_back( proj[hull[j]] );
		}
	}

	map<VecR,Node> g;
	for ( size_t i = 0; i < road.size(); i++ ) {
		vector<Rational> param;
		for ( size_t j = 0; j < road.size(); j++ ) {
			if ( i == j ) continue;
			if ( !IsIntSegments(road[i], road[j]) ) continue;
			Rational d1 =  cross(road[j].first, road[j].second, road[i].first ).abs();
			Rational d2 =  cross(road[j].first, road[j].second, road[i].second ).abs();
			if ( d1 == 0 && d2 == 0 ) continue;
			Rational t = d1 / (d1 + d2);
			param.push_back( t );
		}

		VecR d = road[i].second - road[i].first;
		for ( int j = 0; j < 2; j++ ) {
			VecR ds = terms[j] - road[i].first;
			if ( d.cross(ds) == 0 ) {
				Rational t = d.dot(ds) / d.dot(d);
				if ( Rational(0) <= t && t <= 1 ) {
					param.push_back(t);
				}
			}
		}

		sort( param.begin(), param.end() );
		for ( size_t j = 1; j < param.size(); j++ ) {
			if ( param[j-1] < param[j] ) {
				VecR v1 = road[i].first + d*param[j-1];
				VecR v2 = road[i].first + d*param[j];
				double w = SunshineLength(
					VecD(v1.x.to_f(),v1.y.to_f()), VecD(v2.x.to_f(),v2.y.to_f()), shadow );
				g[v1].cur = v1;
				g[v1].next.push_back(v2);
				g[v1].weight.push_back(w);
				g[v1].sum = (v1==terms[0] ? 0.0 : HUGE_VAL);

				g[v2].cur = v2;
				g[v2].next.push_back(v1);
				g[v2].weight.push_back(w);
				g[v2].sum = (v2==terms[0] ? 0.0 : HUGE_VAL);
			}
		}
	}

	multiset<Node> s;
	s.insert( g[terms[0]] );

	set<VecR> fixed;
	while ( !s.empty() ) {
		Node c = *s.begin();
		s.erase( s.begin() );

		if ( !fixed.insert( c.cur ).second ) continue;

		if ( c.cur == terms[1] ) {
			printf( "%.10f\n", c.sum );
			break;
		}

		for ( size_t i = 0; i < c.next.size(); i++ ) {
			Node n = g[c.next[i]];
			if ( n.sum > c.sum + c.weight[i] && fixed.count(n.cur) == 0 ) {
				n.sum = c.sum + c.weight[i];
				s.insert( n );
			}
		}
	}
	}

	return 0;
}
