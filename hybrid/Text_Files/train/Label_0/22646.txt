#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <complex>
using namespace std;
const long double EPS = 1e-8;
const long double INF = 1e12;
#define EQ(n,m) (abs((n)-(m)) < EPS)
typedef complex<long double> P;
typedef vector<P> VP;
#define X real()
#define Y imag()

vector<long double> solve_quadeq(long double a, long double b, long double c){
    vector<long double> ret;
    if(abs(a) < EPS){
        if(abs(b) > EPS) ret.push_back(-c/b);
        return ret;
    }
    long double d = b*b -4*a*c;
    if(abs(d) < EPS) d = 0;
    if(d < 0) return ret;
    if(d < 0) d = 0;
    ret.push_back((-b +sqrt(d))/(2*a));
    ret.push_back((-b -sqrt(d))/(2*a));
    return ret;
}

const long double g = 9.8;

int main(){
    int n;
    long double v;
    cin >> n >> v;
    VP p(n);
    for(int i=0; i<n; i++){
        long double x,y;
        cin >> x >> y;
        p[i] = P(x, y);
    }

    long double ans = abs(p[1] -p[0]);
    int pos = 1;
    while(pos < n-1){
        P launch = p[pos];
        P prevdir = p[pos] -p[pos-1];
        P nextdir = p[pos+1] -p[pos];
        //ジャンプしない
        if(arg(prevdir) < arg(nextdir) +EPS){
            ans += abs(nextdir);
            pos++;
            continue;
        }
        //ジャンプする
        //放物線の関数
        long double theta = arg(prevdir);
        long double vx = v *cos(theta);
        long double vy = v *sin(theta);
        for(; pos<n-1; pos++){
            //直線の式(y = rx+s)
            long double r,s;
            r = (p[pos+1].Y -p[pos].Y) /(p[pos+1].X -p[pos].X);
            s = -p[pos].X *r +p[pos].Y;
            //直線と放物線が交わる時間tの方程式(at^2 +bt +c = 0)
            long double a,b,c;
            a = g/2;
            b = r*vx -vy;
            c = r*launch.X -launch.Y +s;
            //交点をとる
            vector<long double> solt = solve_quadeq(a, b, c);
            bool solved = false;
            for(long double t: solt){
                if(t < EPS) continue;
                long double x = vx*t +launch.X;
                if(p[pos].X +EPS < x && x +EPS < p[pos+1].X){
                    P cp(x, -g*t*t/2 +vy*t +launch.Y);
                    ans += abs(cp -p[pos+1]);
                    pos++;
                    solved = true;
                    break;
                }
            }
            if(solved) break;
        }
    }
    cout << fixed << setprecision(10);
    cout << ans << endl;
    return 0;
}
