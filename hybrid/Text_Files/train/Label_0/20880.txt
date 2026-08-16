//Hello. I'm Peter.
//#pragma comment(linker, "/STACK:102400000,102400000")
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<cctype>
#include<ctime>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
using namespace std;
typedef long long ll;
typedef unsigned int uin;
#define peter cout<<"i am peter"<<endl
#define input freopen("data.txt","r",stdin)
#define randin srand((unsigned int)time(NULL))
#define INT (0x3f3f3f3f)*2
#define LL (0x3f3f3f3f3f3f3f3f)*2
#define MAXN
#define N 510
#define M
inline int read(){
	int x=0,f=1;char ch=getchar();
	while(ch>'9'||ch<'0'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
const double eps=1e-9;
inline int dcmp(double x){
    if(fabs(x)<eps) return 0;
    else if(x<0) return -1;
    else return 1;
}
int n,m;
struct Point{
    double x,y;
    Point(){};
    Point(double xx,double yy){
        x=xx,y=yy;
    }
};
inline bool comp(const Point a,const Point b){
    if(dcmp(a.x-b.x)) return a.x<b.x;
    else return a.y<b.y;
}
typedef Point Vector;
Vector operator+(const Vector a,const Vector b){
    return Vector(a.x+b.x,a.y+b.y);
}
Vector operator-(const Vector a,const Vector b){
    return Vector(a.x-b.x,a.y-b.y);
}
double operator*(const Vector a,const Vector b){
    return a.x*b.x+a.y*b.y;
}
double operator%(const Vector a,const Vector b){
    return a.x*b.y-a.y*b.x;
}
Vector operator*(const Vector a,const double b){
    return Vector(a.x*b,a.y*b);
}
Vector operator*(const double b,const Vector a){
    return Vector(a.x*b,a.y*b);
}
bool operator ==(const Vector a,const Vector b){
    return !dcmp(a.x-b.x)&&!dcmp(a.y-b.y);
}
Vector operator/(const Vector a,const double b){
    return Vector(a.x/b,a.y/b);
}
double Square_Triangle(Point p1,Point p2,Point p3){
    //????§???¢??¢?§????????????????
    return 0.5*fabs((p2-p1)%(p3-p1));
}
#define lenp res.size()
void Convex_Hull(Point *p,int n,vector<Point>&res){
    res.clear();
    sort(p,p+n,comp);
    for(int i=0;i<n;i++){
        while(lenp>1&&dcmp((res[lenp-1]-res[lenp-2])%(p[i]-res[lenp-1]))<=0) res.pop_back();
        res.push_back(p[i]);
    }
    int k=(int)lenp;
    for(int i=n-2;i>=0;i--){
        while(lenp>k&&dcmp((res[lenp-1]-res[lenp-2])%(p[i]-res[lenp-1]))<=0) res.pop_back();
        res.push_back(p[i]);
    }
    if(lenp>1) res.pop_back();
}
void readPointInt(Point &p){
    int x,y;
    x=read(),y=read();
    p=Point(x,y);
}
Point p1[N],p2[N];
#define lenv1 v1.size()
#define lenv2 v2.size()
#define lenv v.size()
double Square_ConvexHull(vector<Point>&v){//?????????????????¢?§?
    //lenv>=3
    double res=0.0;
    for(int i=1;i<lenv-1;i++){
        res+=Square_Triangle(v[0],v[i],v[i+1]);
    }
    return res;
}
double Square_PointWithConvexHull(Point p,vector<Point>&v){
    //?±???????????????????????????¢????????¢?§?
    v.push_back(v[0]);
    double res=0.0;
    for(int i=0;i<lenv-1;i++){
        res+=Square_Triangle(p,v[i],v[i+1]);
    }
    v.pop_back();
    return res;
}
bool PointOnSegment(Point p,Point p1,Point p2){
    Vector v1=p1-p,v2=p2-p;
    if(dcmp(v1%v2)) return false;
    else if(dcmp(v1*v2)>0) return false;
    else return true;
}
bool PointInConvexHull1_In_ConvexHull2(vector<Point>&v1,vector<Point>&v2){
    if(lenv1==1&&lenv2==1) return v1[0]==v2[0];
    if(lenv1==1&&lenv2==2) return PointOnSegment(v1[0],v2[0],v2[1]);
    if(lenv2>=3){
        double Sv2=Square_ConvexHull(v2);
        for(int i=0;i<lenv1;i++){
            double St=Square_PointWithConvexHull(v1[i],v2);
            if(!dcmp(St-Sv2)) return true;
        }
    }
    return false;
}
bool Segment1_Inter_Segment2(Point p1,Point p2,Point q1,Point q2){
    if(!dcmp((p1-p2)%(q1-q2))){
        return PointOnSegment(p1,q1,q2)||PointOnSegment(p2,q1,q2)||PointOnSegment(q1,p1,p2)||PointOnSegment(q2,p1,p2);
    }
    else{
        int t1=dcmp((p2-p1)%(q1-p1));
        int t2=dcmp((p2-p1)%(q2-p1));
        int t3=dcmp((q2-q1)%(p1-q1));
        int t4=dcmp((q2-q1)%(p2-q1));
        return t1*t2<=0&&t3*t4<=0;
    }
}
bool ConvexHull1_Inter_ConvexHull2(vector<Point>&v1,vector<Point>&v2){
    //?????????????????¨??????????????????
    if(PointInConvexHull1_In_ConvexHull2(v1,v2)) return true;
    if(PointInConvexHull1_In_ConvexHull2(v2,v1)) return true;
    //???????????????????????????
    if(lenv1>=2&&lenv2>=2){
        v1.push_back(v1[0]);
        v2.push_back(v2[0]);
        for(int i=0;i<lenv1-1;i++){
            for(int j=0;j<lenv2-1;j++){
                if(Segment1_Inter_Segment2(v1[i],v1[i+1],v2[j],v2[j+1])){
                    v1.pop_back();
                    v2.pop_back();
                    return true;
                }
            }
        }
        v1.pop_back();
        v2.pop_back();
    }
    return false;
}
int main(){
    while(1){
        n=read(),m=read();
        if(!n&&!m) break;
        for(int i=0;i<n;i++){
            readPointInt(p1[i]);
        }
        vector<Point>res1;
        Convex_Hull(p1,n,res1);
        for(int i=0;i<m;i++){
            readPointInt(p2[i]);
        }
        vector<Point>res2;
        Convex_Hull(p2,m,res2);
        if(ConvexHull1_Inter_ConvexHull2(res1,res2)){
            printf("NO\n");
        }
        else printf("YES\n");
    }
    return 0;
}