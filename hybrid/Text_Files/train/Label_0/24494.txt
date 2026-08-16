#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
double p[6];
double q[6];
double ans = 1.0;
void test(double prob){
	double cur = 0;
	for(int i = 0; i < 6; i++){
		cur += max(prob*p[i],(1.0-prob)*q[i]);
	}
	ans = min(ans,cur);
}
int main(){
	for(int i = 0; i < 6; i++) cin >> p[i];	
	for(int i = 0; i < 6; i++) cin >> q[i];
	for(int i = 0; i < 6; i++) p[i] /= 100.0;
	for(int i = 0; i < 6; i++) q[i] /= 100.0;
	test(0);
	test(1);
	for(int i = 0; i < 6; i++){
		if(p[i] + q[i] < 0.00000001) continue;
		test((p[i])/(p[i]+q[i]));
		test((q[i])/(p[i]+q[i]));
	}
	printf("%.10lf\n", ans);

}
