#include<cmath>
#include<cstdio>
#include<vector>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const long double EPS=1e-8;
const long double PI=acos(-1);

struct point{
	long double x,y;
	point():x(0),y(0){}
	point(long double x,long double y):x(x),y(y){}
	point operator-(const point &a)const{ return point(x-a.x,y-a.y); }
};

long double cross(const point &a,const point &b){ return a.x*b.y-a.y*b.x; }

long double arg(const point &a){
	long double t=atan2(a.y,a.x);
	return t<0?t+2*PI:t;
}

struct line{
	point a,b;
	line(){}
	line(const point &a,const point &b):a(a),b(b){}
};

enum{CCW=1,CW=-1,ON=0};
int ccw(const point &a,const point &b,const point &c){
	long double rdir=cross(b-a,c-a);
	if(rdir>0) return CCW;
	if(rdir<0) return CW;
	return ON;
}

long double dist(const point &a,const point &b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

const long double g=9.8;

int main(){
	int n;
	long double v; scanf("%d%Lf",&n,&v);
	point p[10000];
	rep(i,n) scanf("%Lf%Lf",&p[i].x,&p[i].y);

	long double a[9999],b[9999]; // y = a*x + b
	rep(i,n-1){
		a[i]=(p[i+1].y-p[i].y)/(p[i+1].x-p[i].x);
		b[i]=p[i].y-a[i]*p[i].x;
	}

	long double ans=dist(p[0],p[1]);
	for(int i=1;i<n-1;){
		if(ccw(p[i-1],p[i],p[i+1])!=CW){ // テ」ツつクテ」ツδ」テ」ツδウテ」ツδ療」ツ?療」ツ?ェテ」ツ??
			ans+=dist(p[i],p[i+1]);
			i++;
		}
		else{ // テ」ツつクテ」ツδ」テ」ツδウテ」ツδ療」ツ?凖」ツつ?
			long double vx=v*cos(arg(p[i]-p[i-1]));
			long double vy=v*sin(arg(p[i]-p[i-1]));
			long double x0=p[i].x,y0=p[i].y;
			for(;i+1<n;i++){
				// テヲツ鳴愿ゥツ敖「テ」ツ?ィテ」ツ?カテ」ツ?、テ」ツ?凝」ツつ凝ヲツ卍づ・ツ按サ t テ」ツつ津ヲツアツづ」ツつ?」ツつ?
				// A*t^2 + B*t + C = 0
				long double A=-g/2;
				long double B=vy-a[i]*vx;
				long double C=y0-a[i]*x0-b[i];
				if(B*B-4*A*C<0) continue;

				long double t0=(-B+sqrt(B*B-4*A*C))/(2*A);
				long double t1=(-B-sqrt(B*B-4*A*C))/(2*A);

				long double xx; // テヲツ鳴愿ゥツ敖「テ」ツ?ィテ」ツ?カテ」ツ?、テ」ツ?凝」ツつ凝、ツスツ催ァツスツョ
				xx=x0+vx*t0;
				if(p[i].x<xx && xx<p[i+1].x){ point q(xx,-g/2*t0*t0+vy*t0+y0); ans+=dist(q,p[i+1]); break; }
				xx=x0+vx*t1;
				if(p[i].x<xx && xx<p[i+1].x){ point q(xx,-g/2*t1*t1+vy*t1+y0); ans+=dist(q,p[i+1]); break; }
			}
			i++;
		}
	}

	printf("%.15Lf\n",ans);

	return 0;
}