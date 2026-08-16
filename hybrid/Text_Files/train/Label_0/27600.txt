#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,h,m;
    cin>>a>>b>>h>>m;
    double pi = acos(-1);
    double theta=(h/12.0+(m/60.0)/12.0-m/60.0)*2*pi;
    double ans = sqrt(a*a+b*b-2*a*b*cosl(theta));
    printf("%.10lf\n", ans);
    return 0;
}
