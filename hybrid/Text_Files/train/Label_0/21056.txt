#include<bits/stdc++.h>
#define REP(i,first,last) for(int i=first;i<=last;++i)
#define DOW(i,first,last) for(int i=first;i>=last;--i)
using namespace std;
long long Random(long long a)
{
	return (1ll*rand()*rand()+rand())%a;
}
long long Random(long long f,long long e)
{
	return f+Random(e-f+1);
}
double Sqr(double a)
{
	return a*a;
}
const double PI=3.14159265358979323846264338327950288419716939;
struct Point
{
	double x,y;
	Point(double fx=0,double fy=0)
	{
		x=fx;
		y=fy;
	}
	void Read()
	{
		scanf("%lf%lf",&x,&y);
	}
	void Write()
	{
		printf("%.9lf %.9lf",x,y);
	}
	double operator ^(Point const b)const
	{
		return x*b.x+y*b.y;
	}
	double operator |(Point const b)const
	{
		return x*b.y-b.x*y;
	}
	double operator ==(Point const b)const
	{
		return sqrt((x-b.x)*(x-b.x)+(y-b.y)*(y-b.y));
	}
	Point operator *(double const b)const
	{
		return Point(x*b,y*b);
	}
	Point operator +(Point const b)const
	{
		return Point(x+b.x,y+b.y);
	}
	Point operator -(Point const b)const
	{
		return Point(x-b.x,y-b.y);
	}
	bool operator !=(Point const b)const
	{
		if(1e-5<=fabs(x-b.x))
		{
			return 1;
		}
		if(1e-5<=fabs(y-b.y))
		{
			return 1;
		}
		return 0;
	}
};
Point Symmetrical(Point a,Point m=Point(0,0))
{
	return Point(m.x*2-a.x,m.y*2-a.y);
}
/**
 *      /
 *   a /
 *    m
 *   / b
 *  /
 *
 *    a
 *
 * ---m-----
 *
 *    b
 * return b;
 */
struct Vector
{
	Point a,b;
	Vector(Point f=Point(0,0),Point e=Point(0,0))
	{
		a=f;
		b=e;
	}
	double operator ^(Vector const c)const
	{
		return (a.x-b.x)*(c.a.x-c.b.x)+(c.a.y-c.b.y)*(a.y-b.y);
	}
	double operator |(Vector const c)const
	{
		return (a.x-b.x)*(c.a.y-c.b.y)-(c.a.x-c.b.x)*(a.y-b.y);
	}
};
struct Circle
{
	Point core;
	double radius;
	Circle(Point c=Point(0,0),double r=0)
	{
		core=c;
		radius=r;
	}
};
Point ProjectivePoint(Point a,Vector b)
{
	double c=Vector(b.a,a)^Vector(b.a,b.b);
	c/=(b.a==b.b)*(b.a==b.b);
	return (b.b-b.a)*c+b.a;
}
/**
 *     *
 *     |
 *     |
 * *---m-----*
 *
 *         *
 *         |
 *         |
 * *----*  m
 * return m;
 */
double PointToVector(Point a,Vector b)
{
	Point c=ProjectivePoint(a,b);
	if(
		(
			(b.a.x<=c.x)==(c.x<=b.b.x)
		)
		&&
		(
			(b.a.y<=c.y)==(c.y<=b.b.y)
		)
	)
	{
		return a==c;
	}
	return min(a==b.a,a==b.b);
}
/**
 *   *
 *   |
 * *------*
 *
 *           *
 *          /
 *  *------*
 * return min_dis;
 */
bool InRectangle(Point a,Point b,Point c)
{
	return
	min(b.x,c.x)<=a.x&&a.x<=max(b.x,c.x)
	&&
	min(b.y,c.y)<=a.y&&a.y<=max(b.y,c.y);
}
/**
 *   a
 *  b---*
 *  |   |
 *  *---c
 *  return 0;
 *
 *  b---*
 *  |a  |
 *  *---c
 *  return 1;
 */
bool RectangleIntersection(Point a0,Point a1,Point b0,Point b1)
{
	int zx=fabs(a0.x+a1.x-b0.x-b1.x);
	int zy=fabs(a0.y+a1.y-b0.y-b1.y);
	int x=fabs(a0.x-a1.x)+fabs(b0.x-b1.x);
	int y=fabs(a0.y-a1.y)+fabs(b0.y-b1.y);
	if(zx<=x&&zy<=y)
	{
		return 1;
	}
	return 0;
}
/**
 *  *---*
 *  |   |
 *  *---*
 *
 *    *--*
 *    |  |
 *    |  |
 *    *--*
 * return 0;
 *
 *  *---*
 *  | *-+*
 *  *-+-*|
 *    |  |
 *    *--*
 * return 1;
 */
bool Intersect(Vector a,Vector b)
{
	double a_aa=a|Vector(a.a,b.a);
	double a_ab=a|Vector(a.a,b.b);
	double b_aa=b|Vector(b.a,a.a);
	double b_ab=b|Vector(b.a,a.b);
	if((a_aa==0||a_ab==0||((a_aa<0)^(a_ab<0)))&&(b_aa==0||b_ab==0||((b_aa<0)^(b_ab<0))))
	{
		return RectangleIntersection(a.a,a.b,b.a,b.b);
	}
	return 0;
}
/**
 *      *
 *     /
 *    /*
 *   /  \
 *  /    \
 * *      *
 * return 0;
 *
 *      *
 *  *  /
 *   \/
 *   /\
 *  /  \
 * *    *
 * return 1;
 */
Point QueryIntersect(Vector a,Vector b)
{
	Vector u(a.a,b.a);
	Vector v(b.a,b.b);
	Vector w(a.a,a.b);
	double c=(w|u)/(v|w);
	return Point(b.a.x+(b.b.x-b.a.x)*c,b.a.y+(b.b.y-b.a.y)*c);
}
/**
 *        *
 * *     /
 *  \   /
 *   \ /
 *    m
 *   / \
 *  *   \
 *       *
 * return m;
 */
double VectorToVector(Vector a,Vector b)
{
	if(Intersect(a,b))
	{
		return 0.0;
	}
	return min
	(
		min(PointToVector(a.a,b),PointToVector(a.b,b)),
		min(PointToVector(b.a,a),PointToVector(b.b,a))
	);
}
/**
 *   *----*
 *     |
 * *--------*
 *
 * *-----*
 *        \
 *         *-----*
 * return min_dis;
 */
double TriangleArea(Point a,Point b,Point c)
{
	double al=b==c;
	double bl=a==c;
	double cl=a==b;
	double p=(al+bl+cl)/2;
	return sqrt(p*(p-al)*(p-bl)*(p-cl));
}
/**
 *       a
 *      /|
 *     / |
 *    /  |
 *   c---b
 * return area;
 */
Circle Circumscribed(Point a,Point b,Point c)
{
	double a1=2*(b.x-a.x);
	double b1=2*(b.y-a.y);
	double c1=Sqr(b.x)+Sqr(b.y)-Sqr(a.x)-Sqr(a.y);
	double a2=2*(c.x-b.x);
	double b2=2*(c.y-b.y);
	double c2=Sqr(c.x)+Sqr(c.y)-Sqr(b.x)-Sqr(b.y);
	Point core=Point
	(
		((c1*b2)-(c2*b1))/((a1*b2)-(a2*b1)),
		((a1*c2)-(a2*c1))/((a1*b2)-(a2*b1))
	);
	return Circle(core,core==a);
}
/**
 *       a
 *  p   /|
 *     / |
 *    /  |
 *   c---b
 * (dis(p,a)=dis(p,b)=dis(p,c))
 * return p;
 */
Circle Inscribed(Point a,Point b,Point c)
{
	double al=b==c;
	double bl=a==c;
	double cl=a==b;
	return Circle(Point((al*a.x+bl*b.x+cl*c.x)/(al+bl+cl),(al*a.y+bl*b.y+cl*c.y)/(al+bl+cl)),TriangleArea(a,b,c)/(al+bl+cl)*2);
}
/**
 *       a
 *      /|
 *     / |
 *    / p|
 *   c---b
 * (dis(p,ac)=dis(p,ab)=dis(p,bc))
 * return p;
 */
int PolygonPoint(Point a,Point point[],int n)
{
	point[n+1]=point[1];
	bool now=0;
	REP(i,1,n)
	{
		if(Intersect(Vector(a,Point(1e6,a.y)),Vector(point[i],point[i+1])))
		{
			if(
				(PointToVector(a,Vector(point[i],point[i+1]))<=1e-5))
			{
				return 1;
			}
			if((a.y<point[i].y)^(a.y<point[i+1].y))
			{
				now^=1;
			}
		}
	}
	if(now==0)
	{
		return 0;
	}
	return 2;
}
/**
 *       *---*
 *      /     \
 *     *   a   *
 *      \     /
 *       *---*
 * return 2;
 *
 *       *---*
 *      /     \
 *     *       * a
 *      \     /
 *       *---*
 * return 0;
 *
 *       *---*
 *      /     \
 *     *       *
 *      \     /
 *       *-a-*
 * return 1;
 */
double Area(Point point[],int n)
{
	double result=0;
	REP(i,2,n)
	{
		result+=point[i-1]|point[i];
	}
	result+=point[n]|point[1];
	return fabs(result)/2.0;
}
/**
 *       *---*
 *      /   /
 *     *   *---*
 *      \     /
 *       *---*
 * return area;
 */
double Perimeter(Point point[],int n)
{
	double result=0;
	REP(i,2,n)
	{
		result+=(point[i-1]==point[i]);
	}
	return result+(point[1]==point[n]);
}
/**
 *       *---*
 *      /   /
 *     *   *---*
 *      \     /
 *       *---*
 * return perimeter;
 */
bool CheckConvexHull(Point point[],int n)
{
	double first=0,c;
	point[++n]=point[1];
	REP(i,1,n-1)
	{
		if(!first)
		{
			first=Vector(point[i],point[i+1])|Vector(point[i+1],point[i+2]);
		}
		else
		{
			c=(Vector(point[i],point[i+1])|Vector(point[i+1],point[i+2]));
			if(c!=0&&((first<0)^(c<0)))
			{
				return 0;
			}
		}
	}
	return 1;
}
/**
 *       *---*
 *      /   /
 *     *   *---*
 *      \     /
 *       *---*
 * return 0;
 *
 *       *---*
 *      /     \
 *     *       *
 *      \     /
 *       *---*
 * return 1;
 */
Point f_point;
bool Cmp(Point a,Point b)
{
	double c=Vector(f_point,a)|Vector(f_point,b);
	if(0<c)
	{
		return 1;
	}
	if(c==0&&(f_point==a)<(f_point==b))
	{
		return 1;
	}
	return 0;
}
int GetConvexHull(Point point[],Point st[],int n)
{
	REP(i,2,n)
	{
		if(point[i].y<point[1].y||point[i].y==point[1].y&&point[i].x<point[1].x)
		{
			swap(point[i],point[1]);
		}
	}
	f_point=point[1];
	sort(point+2,point+1+n,Cmp);
	int top=1;
	st[1]=point[1];
	REP(i,2,n)
	{
		while(1<top&&(Vector(st[top-1],st[top])|Vector(st[top],point[i]))<=0)
		{
			--top;
		}
		st[++top]=point[i];
	}
	return top;
}
/**
 *       *   *
 *
 *     *   *   *
 *
 *       *   *
 *         |
 *         V
 *       *---*
 *      /     \
 *     *   *   *
 *      \     /
 *       *---*
 */
double GetDiam(Point point[],int n)
{
	double result=0;
	if(n==2)
	{
		return point[1]==point[2];
	}
	point[++n]=point[1];
	int top=2;
	REP(i,1,n)
	{
		while(
			(Vector(point[i],point[top])|Vector(point[top],point[i+1]))
			>
			(Vector(point[i],point[top+1])|Vector(point[top+1],point[i+1]))
			)
		{
			top++;
			if(top==n+1)
			{
				top=1;
			}
		}
		result=max(result,max(point[i]==point[top],point[i+1]==point[top]));
	}
	return result;
}
/**
 *       *---*
 *      / \   \
 *     *   \   *
 *      \   \ /
 *       *---*
 * return max_dis;
 */
Point a,b,c;
int main()
{
	a.Read();
	b.Read();
	c.Read();
	Circle cir=Inscribed(a,b,c);
	cir.core.Write();
	printf(" %.9lf\n",cir.radius);
	return 0;
}
