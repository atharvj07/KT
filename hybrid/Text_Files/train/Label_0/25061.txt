// 2009à\IF ÷ÜÁÄ¢±¤
#include <iostream>
#include <complex>
#include <vector>

using namespace std;

typedef complex<double> P;

const double EPS = 1e-8;
const double INF = 1e12;

double cross(P a, P b) { return imag(conj(a)*b); }
double angle(P a, P b) { return arg(conj(a)*b); }

P crossPoint(P lp, P lq, P mp, P mq){
	double A = cross(lq-lp, mq-mp);
	double B = cross(lq-lp, lq-mp);
	return mp + B / A * (mq-mp);
}

bool inTriangle(P a, P b, P c, P p){
	double A = cross(a-p,b-p);
	double B = cross(b-p,c-p);
	double C = cross(c-p,a-p);
	// ¡ñÍÓãÌ_ÍOÆµÄµ¤D¶áÈ¢ÆêxÍ¸ê½jÉÄxøÁ©©éD
	// ë·ÌÖWãC÷¬Èlà0ÆµÄl¦éD
	if(abs(A) < EPS || abs(B) < EPS || abs(C) < EPS) return false; 
	if(A*B < EPS || B*C < EPS || C*A < EPS) return false;
	return true;
}

int main(){
	int m, n, x, y;
	while(cin >> m >> n, m){
		vector<P> vl, vh;
		for(int i=0;i<m;i++){
			cin >> x >> y; vl.push_back(P(x,y));
		}
		for(int i=0;i<n;i++){
			cin >> x >> y; vh.push_back(P(x,y));
		}
		// ÐàªÅIIÉoR·é_ÌW
		vector<P> path;     path.push_back(vl[0]);
		// ÐàªCe_ÉÇê­ç¢ª«Â¢Ä¢é©ðo¦é
		vector<double> rot; rot.push_back(INF);
		P prev(vl[0]), cur(vl[1]);
		for(int i=2;i<m;i++){
			P next(vl[i]);
			while(true){
				P tmp = P(-1,-1);
				double minagl = 1e12;
				for(int j=0;j<n;j++){
					// prev, cur, next©çÈéOp`Éàï³êé_ðT·
					// ¼ü(cur,prev)ÆÈ·pxªÅà¬³¢jÉÐÁ©©é
					if(inTriangle(prev, cur, next, vh[j])){
						double a = abs(angle(cur-prev, vh[j]-prev));
						if(a < minagl){
							minagl = a;
							tmp = vh[j];
						}
					}
				}
				double agl;
				// real(tmp)ªÈçprev,cur,nextðÔOp`àÉ_ª³©Á½±ÆÉÈé
				if(real(tmp)<0) agl = angle(cur-prev,next-prev);
				else            agl = angle(cur-prev,tmp-prev);
				// RªÙÇ¯é»èDaglñµ½Æ«ÉCª½]·éêÍÙÇ¯éD
				// .back() ÅvectorÌÅãÌvfðQÆÅ«é
				if(rot.back()*(rot.back()+agl) < -EPS){
					path.pop_back();
					rot.pop_back();
					cur = crossPoint(prev, path.back(), cur, next);
					prev = path.back();
				} else {
					rot.back() += agl;
					if(real(tmp) < 0){
						// Ó(vl[i-1],vl[i])ãÌT[`I¹
						prev = path.back();
						cur = next;
						break;
					} else {
						// jtmpÉÐÁ©©éDcurÌÊuðißéD
						path.push_back(tmp);
						rot.push_back(0);
						cur = crossPoint(prev, tmp, cur, next);
						prev = tmp;
					}
				}
			}
		}
		// ÅI_ðÇÁ
		path.push_back(vl.back());
		double ans = 0.0;
		for(int i=1;i<path.size();i++) ans += abs(path[i]-path[i-1]);
		printf("%.5f\n", ans);
	}
}