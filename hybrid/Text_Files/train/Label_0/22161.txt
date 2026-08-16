#include <cstdio>
#include <vector>
#include <complex>
#include <cmath>
using namespace std;

typedef double D;
typedef complex<D> P;
typedef const P &rP;

const D EPS = 1e-10;

D dot(rP a, rP b){
	return real(a) * real(b) + imag(a) * imag(b);
}

void intrcc(rP p1, D r1, rP p2, D r2, vector<P> &res){
	D d = abs(p2 - p1);
	D phi = arg(p2 - p1);
	D costheta = (d * d + r1 * r1 - r2 * r2) / (2.0 * d * r1);
	if( abs(costheta) > 1.0 ){	return;	}
	D theta = acos(costheta);
	res.push_back(p1 + polar(r1, phi + theta));
	res.push_back(p1 + polar(r1, phi - theta));
}

void intrlc(rP p1, rP p2, rP pc, D r, vector<P> &res){
	P v12 = p2 - p1;
	P v1c = pc - p1;

	D a = norm(v12);
	D b = -dot(v12, v1c);
	D c = norm(v1c) - r * r;

	D d = b * b - a * c;
	if(abs(a) < EPS || d < EPS){
		return;
	}
	d = sqrt(d);
	D t1 = (-b + d) / a;
	D t2 = (-b - d) / a;
	res.push_back(p1 + v12 * t1);
	res.push_back(p1 + v12 * t2);
}

D rtod(D h, D r){
	if(r <= h){ return r; }
	D th = asin((r - h) / r);
	return r * cos(th);
}

vector<P> ps;
vector<D> hs;
vector<D> ds;
D wl;

bool check(D r){
	D lx = rtod(wl, r);
	D rx = 100.0 - lx;
	
	P fld[4];
	fld[0] = P(lx, lx);
	fld[1] = P(lx, rx);
	fld[2] = P(rx, rx);
	fld[3] = P(rx, lx);
	
	vector<P> cand(fld, fld + 4);

	ds.resize(hs.size());
	for(size_t i = 0; i < hs.size(); ++i){
		ds[i] = rtod(hs[i], r);
	}
	
	for(size_t i = 0; i < hs.size(); ++i){
		for(int j = 0; j < 4; ++j){
			intrlc(fld[j], fld[(j + 1) & 3], ps[i], ds[i], cand);
		}
		for(size_t j = 0; j < i; ++j){
			intrcc(ps[i], ds[i], ps[j], ds[j], cand);
		}
	}
	
	for(size_t i = 0; i < cand.size(); ++i){
		D x = real(cand[i]), y = imag(cand[i]);
		if(x > lx - EPS && x < rx + EPS && y > lx - EPS && y < rx + EPS){
			bool ok = true;
			for(size_t j = 0; j < ds.size(); ++j){
				if(abs(cand[i] - ps[j]) < ds[j] - EPS){
					ok = false;
					break;
				}
			}
			if(ok){
				return true;
			}
		}
	}
	return false;
}

int main(){
	int n;
	D x, y;
	while(scanf("%d%lf", &n, &wl), n){
		ps.resize(n);
		hs.resize(n);
		for(int i = 0; i < n; ++i){
			scanf("%lf%lf%lf", &x, &y, &hs[i]);
			ps[i] = P(x, y);
		}
		
		D left = 0.0, right = 200.0;
		for(int ttt = 200; ttt--; ){
			D mid = (left + right) * 0.5;
			if(check(mid)){
				left = mid;
			}
			else{
				right = mid;
			}
		}
		printf("%.9f\n", left);
	}
}