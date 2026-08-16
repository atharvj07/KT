#include<cstdio>
#include<complex>
#include<vector>
#include<cmath>
#include<utility>
#include<algorithm>

using namespace std;

const double eps=1e-9;

template<class T> bool eq(T a,T b){
	return abs(a-b)<eps;
}

template<class T> int sgn(T a){
	return eq(a,0.0)?0:(a>0?1:-1);
}


typedef complex<double> Point;
typedef complex<double> Vector;
typedef pair<Point,Point> Segment;
typedef vector<Point> Polyline;

Polyline poly;
Point pd,ph;
double vd,vh;
int N;

bool onSeg(Point a,Point b,Point c){
	//Is c on a-b?
	return eq(abs(a-b),abs(a-c)+abs(b-c));
}

double doP(Vector a,Vector b){
	return (conj(a)*b).real();
}

Point proj(Point a,Point b,Point c){
	if(eq(a,b)) return c;
	Point x=b-a,p=c-a;
	Point pr=x*(doP(x,p)/norm(x));
	return pr+a;
}

pair<double,Point> solve(Segment seg,Point pt,double human,double domino){
	Point p1=seg.first,p2=seg.second;
	double d1=abs(p1-pt),d2=abs(p2-pt);
	double ln=abs(p1-p2);
	double t1=d1/vh,t2=d2/vh;
	double td=ln/vd;
	if(human+t2>domino+td) return make_pair(-1,pt);
	Point lb=p1,ub=p2;
	for(int stage=0;stage<100;stage++){
		Point mid=(lb+ub)/2.0;
		double lDomino=abs(mid-p1);
		double lHuman=abs(mid-pt);
		double tDomino=domino+lDomino/vd;
		double tHuman=human+lHuman/vh;
		if(tHuman>tDomino) lb=mid;
		else ub=mid;
	}
	double retT=domino+abs(lb-p1)/vd;
	Point retP=lb;
	return make_pair(retT,retP);
}

double getLen(Polyline poly){
	double res=0;
	for(int i=0;i+1<poly.size();i++){
		res+=abs(poly[i+1]-poly[i]);
	}
	return res;
}

pair<double,Point> solve(Polyline poly,Point pt,double human){
	if(poly.size()<=1){
		return make_pair(0,pt);
	}
	double disSum=0;
	for(int i=0;i+1<poly.size();i++){
		Segment seg;
		seg.first=poly[i];
		seg.second=poly[i+1];
		Point perp=proj(poly[i],poly[i+1],pt);
		if(onSeg(poly[i],poly[i+1],perp)){
			Segment seg1,seg2;
			seg1=Segment(poly[i],perp);
			seg2=Segment(perp,poly[i+1]);
			pair<double,Point> res;
			res=solve(seg1,pt,human,disSum/vd);
			if(res.first>=0) return res;
			disSum+=abs(perp-poly[i]);
			res=solve(seg2,pt,human,disSum/vd);
			if(res.first>=0) return res;
			disSum+=abs(poly[i+1]-perp);
		}else{
			pair<double,Point> res;
			res=solve(seg,pt,human,disSum/vd);
			if(res.first>=0){
				return res;
			}
			disSum+=abs(poly[i+1]-poly[i]);
		}
	}
	return make_pair(0,pt);
}

double solve(Polyline left,Polyline right,Point pt){
	//go left->go right
	pair<double,Point> resL=solve(left,pt,0);
	pair<double,Point> resLR=solve(right,resL.second,resL.first);
	double cur;
	if(resL.first<eps){
		cur=getLen(left)/vd;
	}else{
		cur=resL.first;
	}
	
	if(resLR.first<eps){
		cur=max(cur,getLen(right)/vd);
	}else{
		cur=max(cur,resLR.first);
	}
	
	return cur;
}

int main(){
	int N;
	scanf("%d",&N);
	for(int i=0;i<N;i++){
		int x,y;
		scanf("%d%d",&x,&y);
		poly.push_back(Point(x,y));
	}
	int x,y,v;
	scanf("%d%d%d",&x,&y,&v);
	pd=Point(x,y);
	vd=v;
	scanf("%d%d%d",&x,&y,&v);
	ph=Point(x,y);
	vh=v;
	if(eq(pd,ph)){
		printf("0\n");
		return 0;
	}
	if(eq(poly[0],pd)||eq(poly[N-1],pd)){
		if(eq(poly[N-1],pd)){
			reverse(poly.begin(),poly.end());
		}
		pair<double,Point> res=solve(poly,ph,0);
		double ans=res.first;
		if(ans<eps){
			double allDis=getLen(poly);
			ans=allDis/vd;
			printf("%.9f\n",ans);
			return 0;
		}
	}
	for(int i=0;i<N-1;i++){
		Point p1=poly[i];
		Point p2=poly[i+1];
		bool flg=onSeg(p1,p2,pd);
		if(flg){
			double ans=1e30;
			Polyline left,right;
			left.push_back(pd);
			for(int j=i;j>=0;j--) if(!eq(pd,poly[j])) left.push_back(poly[j]);
			right.push_back(pd);
			for(int j=i+1;j<N;j++) if(!eq(pd,poly[j])) right.push_back(poly[j]);
			ans=min(ans,solve(left,right,ph));
			ans=min(ans,solve(right,left,ph));
			printf("%.9f\n",ans);
			break;
		}
	}
	return 0;
}