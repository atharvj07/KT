#include <cstdio>
#include <vector>
#include <cmath>
#include <complex>
#include <iostream>
using namespace std;

#define EPS 1e-6

typedef long double ldouble;
typedef complex<ldouble> P;

ldouble cross(const P &a, const P &b){
	return real(a) * imag(b) - imag(a) * real(b);
}

int n;
P z[10001];
ldouble Vabs;

const ldouble g = 9.8;

P jump(int &i){
	P dir = z[i] - z[i-1];
	P v = Vabs / abs(dir) * dir;
	const P &base = z[i];
	ldouble a = g / (real(v) * real(v) * 2.0);
	ldouble b = imag(v) / real(v);

	for(int j = i; j < n - 1; ++j){
		P z1 = z[j] - base;
		P z2 = z[j+1] - base;
		ldouble c = imag(z2 - z1) / real(z2 - z1);
		ldouble d = imag(z1) - c * real(z1);
		ldouble e = sqrt((b-c) * (b-c) - 4.0 * a * d);

		for(ldouble sgn = -1.0; sgn < 2.0; sgn += 2.0){
			ldouble x = (b - c + sgn * e) / (2.0 * a);
			if(x > real(z1) && x < real(z2)){
				ldouble y = -a * x * x + b * x;
				i = j;
				return P(x, y) + base;
			}
		}
	}

	i = n;
	return z[n-1];
}

int main(){
	ldouble x, y;
	cin >> n >> Vabs;
	for(int i = 0; i < n; ++i){
		cin >> x >> y;
		z[i] = P(x, y);
	}

	ldouble ans = 0.0;
	P prev = z[0];
	for(int i = 1; i < n; ++i){
		P dif = z[i] - prev;
		ans += abs(dif);
		if(i == n - 1) break;

		if(cross(dif, z[i+1] - z[i]) < -EPS){
			prev = jump(i);
		}
		else{
			prev = z[i];
		}
	}
	
	printf("%.20f\n", (double)ans);
}