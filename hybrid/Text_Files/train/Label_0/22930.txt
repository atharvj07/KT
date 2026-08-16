//Bairstow

#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <complex>
#include <cmath>
using namespace std;
 
#define EPS_S 1e-9
#define EPS 1e-4
 
typedef complex<double> P;
typedef pair<int,int> pii;
 
void bairstow(double &p, double &q, vector<double> &a){
    int n = a.size() - 1;
     
    vector<double> b(n + 1), c(n + 1);
    double dp, dq, e;
     
    p = q = 0.12345;
    int cnt = 0;
    do{
        b[0] = a[0];
        b[1] = a[1] - p * b[0];
         
        for(int k = 2; k <= n; ++k){
            b[k] = a[k] - p * b[k-1] - q * b[k-2];
        }
        c[0] = b[0];
        c[1] = b[1] - p * c[0];
        for(int k = 2; k <= n; ++k){
            c[k] = b[k] - p * c[k-1] - q * c[k-2];
        }
        e = c[n-2] * c[n-2] - c[n-3] * (c[n-1] - b[n-1]);
		if(abs(e) < EPS_S){ break; }
        dp = (b[n-1] * c[n-2] - b[n] * c[n-3]) / e;
        dq = (b[n] * c[n-2] - b[n-1] * (c[n-1] - b[n-1])) / e;
        p += dp;
        q += dq;
    }while(++cnt < 10000 && min(abs(dp), abs(dp)) > EPS_S);
     
    a.swap(b);
}
 
vector<P> solve_powered(vector<double> a){
    vector<P> ret;

	while(abs(a.back()) < EPS_S){
		ret.push_back(0.0);
		a.pop_back();
	}

    while(a.size() > 1){
        if(a.size() == 2){
            ret.push_back(-a[1] / a[0]);
        }
        else{
            double p, q;
            if(a.size() == 3){
                p = a[1] / a[0];
                q = a[2] / a[0];
            }
            else{
                bairstow(p, q, a);
            }
 
            P rt = sqrt(P(p * p - 4.0 * q));
            ret.push_back((-p + rt) * 0.5);
            ret.push_back((-p - rt) * 0.5);
        }
         
        a.resize(a.size() - 2);
    }
     
    return ret;
}
 
int main(){
    int d;
    scanf("%d", &d);
    vector<double> a(d + 1);
    for(int i = d; i >= 0; --i){
        scanf("%lf", &a[i]);
    }
 
    vector<P> ret = solve_powered(a);
    vector<pii> ans;
    for(int i = 0; i < ret.size(); ++i){
        double re = real(ret[i]), im = imag(ret[i]);
        double rei = floor(re + 0.5), imi = floor(im + 0.5);
        if(abs(re - rei) < EPS && abs(im - imi) < EPS){
            ans.push_back(pii(rei, imi));
        }
    }

    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    printf("%d\n", ans.size());
    for(int i = 0; i < ans.size(); ++i){
        if(i != 0){ putchar(' '); }
         
        int re = ans[i].first, im = ans[i].second;
        if(re == 0){
            if(im == 0){ printf("0"); }
            else if(im == 1){
                printf("i");
            }
            else if(im == -1){
                printf("-i");
            }
            else{ printf("%di", im); }
        }
        else{
            printf("%d", re);
            if(im == 1){
                printf("+i");
            }
            else if(im == -1){
                printf("-i");
            }
            else if(im != 0){
                printf("%+di", im);
            }
        }
    }
    puts("");
}