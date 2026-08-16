#include <bits/stdc++.h>
using namespace std;

struct P{
	double x,y,z;
};
P operator + (P a,P b){
	a.x += b.x;
	a.y += b.y;
	a.z += b.z;
	return a;
}

double pi = acos(-1);
int main(){
	double m,t;
	cin >> m >> t;
	m = m / 180 * pi;
	
	t *= 60;
	double tot = 0;
	for(double ms = 0 ; ms < t  ; ms += 1.0){
		P mo,ka;
		mo.x = 380000 * cos(m + ms / 2500000 * 2 * pi);
		mo.y = 380000 * sin(m + ms / 2500000 * 2 * pi);
		mo.z = 0;
		ka.x = 1900 * sin(-ms / 7200 * 2 * pi);
		ka.y = 0;
		ka.z = 1900 * cos(-ms / 7200 * 2 * pi);
		ka = ka + mo;
		double a = ka.x * ka.x + ka.y * ka.y + ka.z * ka.z;
		double b = ka.x * mo.x + ka.y * mo.y + ka.z * mo.z;
		double c = 380000*380000.0 - 1800*1800;
		if( b * b - a*c >= 0 ){
			double s = (b + sqrt(b*b-a*c)) / a;
			//cout << s << endl;
			if( s < 1 ) tot++;
		}
	}
	printf("%.10lf\n",tot/60.);
	
}