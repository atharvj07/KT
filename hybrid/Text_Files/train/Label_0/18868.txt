#include<bits/stdc++.h>
using namespace std;
#define ldb  double
bool Bar;
const ldb mi=1e-9;
int n,mk;
ldb q,w,a1,a2;
int sign(ldb a) {
	if(abs(a)<mi)return 0;
	return a>0?1:-1;
}
struct Point {
	ldb x,y;
	ldb len() {
		return x*x+y*y;
	}
	int operator ==(const Point& a)const {
		return abs(x-a.x)<=mi&&abs(y-a.y)<=mi;
	}
	Point operator +(const Point& a)const {
		return(Point)<%x+a.x,y+a.y%>;
	}
	Point operator -(const Point& a)const {
		return(Point)<%x-a.x,y-a.y%>;
	}
	Point operator /(const ldb& a)const {
		return(Point)<%x/a,y/a%>;
	}
	Point operator *(const ldb& a)const {
		return(Point)<%x*a,y*a%>;
	}
} a,b,c,d,l,r,mid;
bool Ka;
Point Base(Point a) {
	ldb l=sqrt(a.len());
	if(a.x<-mi)a.x=-a.x,a.y=-a.y;
	else if(abs(a.x)<=mi)a.y=abs(a.y);
	if(abs(l)<=mi)l=1;
	return a/l;
}
ldb dot(Point a,Point b) {
	return a.x*b.x+a.y*b.y;
}
ldb det(Point a,Point b) {
	return a.x*b.y-a.y*b.x;
}
int Check(ldb a,ldb b) {
	return sign(a-b)<1;
}
int Case;
int main() {
//	printf("%lf\n",(&Ka-&Bar)/1024.0/1024.0);
//	freopen("tmp.in","r",stdin);
//	freopen("tmp.out","w",stdout);
	scanf("%d",&n);
	for(int i=1; i<=n; ++i) {
		scanf("%lf%lf",&a.x,&a.y);
		scanf("%lf%lf",&b.x,&b.y);
		scanf("%lf%lf",&c.x,&c.y);
		scanf("%lf%lf",&d.x,&d.y);
		l=Base(b-a),r=Base(d-c);
//		l=b-a,r=d-c;
//		printf("%d ",++Case);
		mid=a+l*(det(r,(a-c))/det(l,r));
		if(a.x>b.x)swap(a.x,b.x);
		if(a.y>b.y)swap(a.y,b.y);
		if(c.x>d.x)swap(c.x,d.x);
		if(c.y>d.y)swap(c.y,d.y);
//		if(l==r) {
//			mk=Check(a.x,c.x)&&Check(c.x,b.x)&&Check(a.y,c.y)&&Check(c.y,b.y);
//			mk|=Check(a.x,d.x)&&Check(d.x,b.x)&&Check(a.y,d.y)&&Check(d.y,b.y);
//			mk|=Check(c.x,a.x)&&Check(a.x,d.x)&&Check(c.y,a.y)&&Check(a.y,d.y);
//			mk|=Check(c.x,b.x)&&Check(b.x,d.x)&&Check(c.y,b.y)&&Check(b.y,d.y);
//		} else {
		printf("%.10lf %.10lf\n",mid.x,mid.y);
//			mk=Check(a.x,mid.x)&&Check(mid.x,b.x)&&Check(c.x,mid.x)&&Check(mid.x,d.x)&&
//			   Check(a.y,mid.y)&&Check(mid.y,b.y)&&Check(c.y,mid.y)&&Check(mid.y,d.y);
//			mk&=(mid.x==mid.x)&&(mid.y==mid.t)
//
//		}
//		if(!mk)puts("0");
//		else puts("1");
	}
	return 0;
}
