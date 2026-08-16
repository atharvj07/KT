#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const double EPS=1e-8;
const double PI=acos(-1);

struct point{
	double x,y;
	point():x(0),y(0){}
	point(double x,double y):x(x),y(y){}
	point &operator+=(const point &a){ x+=a.x; y+=a.y; return *this; }
	point &operator-=(const point &a){ x-=a.x; y-=a.y; return *this; }
	point &operator*=(const point &a){ x*=a.x; y*=a.y; return *this; }
	point &operator/=(const point &a){ x/=a.x; y/=a.y; return *this; }
	point operator+(const point &a)const{ return point(x+a.x,y+a.y); }
	point operator-(const point &a)const{ return point(x-a.x,y-a.y); }
	point operator/(double c)const{ return point(x/c,y/c); }
};

point operator*(double c,const point &a){ return point(c*a.x,c*a.y); }

bool operator< (const point &a,const point &b){ return a.x+EPS<b.x || abs(a.x-b.x)<EPS && a.y+EPS<b.y; }
bool operator==(const point &a,const point &b){ return abs(a.x-b.x)<EPS && abs(a.y-b.y)<EPS; }

double dot(const point &a,const point &b){ return a.x*b.x+a.y*b.y; }

double cross(const point &a,const point &b){ return a.x*b.y-a.y*b.x; }

double abs(const point &a){ return sqrt(a.x*a.x+a.y*a.y); }

double abs2(const point &a){ return a.x*a.x+a.y*a.y; }

point rot(const point &a,double theta){ return point(a.x*cos(theta)-a.y*sin(theta),a.x*sin(theta)+a.y*cos(theta)); }

double arg(const point &a){
	double t=atan2(a.y,a.x);
	return t<0?t+2*PI:t;
}

struct line{
	point a,b;
	line(){}
	line(const point &a,const point &b):a(a),b(b){}
};

struct segment{
	point a,b;
	segment(){}
	segment(const point &a,const point &b):a(a),b(b){}
	operator line()const{ return line(a,b); }
};

typedef vector<point> polygon;

struct circle{
	point c;
	double r;
	circle():c(point(0,0)),r(0){}
	circle(const point &c,double r):c(c),r(r){}
};

point proj(const point &p,const line &L){ return L.a+dot(p-L.a,L.b-L.a)/abs2(L.b-L.a)*(L.b-L.a); }

enum{CCW=1,CW=-1,ON=0};
int ccw(const point &a,const point &b,const point &c){
	double rdir=cross(b-a,c-a);
	if(rdir> EPS) return CCW;
	if(rdir<-EPS) return CW;
	return ON;
}

void to_ccw(polygon &F){
	int n=F.size();
	double A=0;
	rep(i,n) A+=cross(F[i],F[(i+1)%n]);
	if(A<-EPS) reverse(F.begin(),F.end());
}

double dist(const point &a,const point &b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

bool cover(const segment &S,const point &p){
	return abs(cross(S.a-p,S.b-p))<EPS && dot(S.a-p,S.b-p)<EPS;
}

int get_intersect(const circle &C,const segment &S,vector<point> &res){
	point h=proj(C.c,S);
	double d=abs(C.c-h);
	if(d>C.r+EPS) return 0;
	if(d>C.r-EPS){
		int cnt=0;
		if(cover(S,h)) res.push_back(h), cnt++;
		return cnt;
	}
	else{
		point v=S.b-S.a;
		v=(sqrt(C.r*C.r-d*d)/abs(v))*v;
		int cnt=0;
		if(cover(S,h+v)) res.push_back(h+v), cnt++;
		if(cover(S,h-v)) res.push_back(h-v), cnt++;
		return cnt;
	}
}

bool cover(const polygon &F,const point &p){
	int n=F.size();
	bool res=false;
	rep(i,n){
		point v1=F[i]-p,v2=F[(i+1)%n]-p;
		if(v1.y>v2.y) swap(v1,v2);
		if(v1.y<EPS && EPS<v2.y && cross(v1,v2)>EPS) res=!res;
		if(abs(cross(v1,v2))<EPS && dot(v1,v2)<EPS) return true;
	}
	return res;
}

class union_find{
	vector<int> a;
public:
	union_find(int n):a(n,-1){}
	int find(int x){
		if(a[x]<0) return x;
		return a[x]=find(a[x]);
	}
	void unite(int x,int y){
		x=find(x),y=find(y);
		if(x!=y){ a[x]+=a[y]; a[y]=x; }
	}
	int size(int x){ return -a[find(x)]; }
};

int main(){
	double r;
	int n; scanf("%lf%d",&r,&n);
	polygon F(n);
	rep(i,n) scanf("%lf%lf",&F[i].x,&F[i].y);
	to_ccw(F);

	circle C(point(0,0),r);

	vector<point> P=F; // 候補点の全体
	rep(i,n){
		get_intersect(C,segment(F[i],F[(i+1)%n]),P);
	}
	P.push_back(point(-C.r,0)); // P[0] が外部に接するために円周上の偏角 π の点も追加しておく
	sort(P.begin(),P.end());
	P.erase(unique(P.begin(),P.end()),P.end());

	union_find U(P.size()); // 図形の辺に沿って移動できる点どうしをまとめる
	// 多角形の辺上
	rep(i,n){
		segment S(F[i],F[(i+1)%n]);
		vector< pair<point,int> > R;
		rep(j,P.size()) if(cover(S,P[j])) R.push_back(make_pair(P[j],j));
		sort(R.begin(),R.end());
		rep(j,(int)R.size()-1){
			point cen=(R[j].first+R[j+1].first)/2;
			if(abs(cen)>C.r+EPS){
				U.unite(R[j].second,R[j+1].second);
			}
		}
	}
	// 円上
	{
		vector< pair<double,int> > R;
		rep(i,P.size()) if(C.r-EPS<abs(P[i]) && abs(P[i])<C.r+EPS) {
			R.push_back(make_pair(arg(P[i]),i));
		}
		sort(R.begin(),R.end()); // 偏角ソート
		R.push_back(R[0]);
		R.back().first+=2*PI;
		rep(i,(int)R.size()-1){
			double phi=(R[i].first+R[i+1].first)/2;
			point cen=C.r*rot(point(1,0),phi);
			if(!cover(F,cen)){
				U.unite(R[i].second,R[i+1].second);
			}
		}
	}

	double ans=0;
	// 多角形の辺上
	rep(i,n){
		segment S(F[i],F[(i+1)%n]);
		vector< pair<point,int> > R;
		rep(j,P.size()) if(cover(S,P[j])) R.push_back(make_pair(P[j],j));
		sort(R.begin(),R.end());
		rep(j,(int)R.size()-1){
			point cen=(R[j].first+R[j+1].first)/2;
			if(abs(cen)>C.r+EPS && U.find(R[j].second)==U.find(0) && U.find(R[j+1].second)==U.find(0)) {
				ans+=dist(R[j].first,R[j+1].first);
			}
		}
	}
	// 円上
	{
		vector< pair<double,int> > R;
		rep(i,P.size()) if(C.r-EPS<abs(P[i]) && abs(P[i])<C.r+EPS) {
			R.push_back(make_pair(arg(P[i]),i));
		}
		sort(R.begin(),R.end()); // 偏角ソート
		R.push_back(R[0]);
		R.back().first+=2*PI;
		rep(i,(int)R.size()-1){
			double phi=(R[i].first+R[i+1].first)/2;
			point cen=C.r*rot(point(1,0),phi);
			if(!cover(F,cen) && U.find(R[i].second)==U.find(0) && U.find(R[i+1].second)==U.find(0)){
				ans+=C.r*(R[i+1].first-R[i].first);
			}
		}
	}

	printf("%.9f\n",ans);

	return 0;
}