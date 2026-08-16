#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
#include <iterator>
using namespace std;

class BinaryIndexedTree
{
private:
    int n;
    vector<int> data;
public:
    BinaryIndexedTree(int n){ // コンストラクタ
        this->n = n;
        data.assign(n+1, 0);
    }
    void add(int k, int x){ // k番目の要素にxを加算する
        ++ k;
        while(k <= n){
            data[k] += x;
            k += k & -k;
        }
    }
    int sum(int k){ // 区間[0,k]の総和を返す
        ++ k;
        int ret = 0;
        while(k > 0){
            ret += data[k];
            k -= k & -k;
        }
        return ret;
    }
    int sum(int a, int b){ // 区間[a,b]の総和を返す
        return sum(b) - sum(a-1);
    }
};

int inversionNumber(const vector<int>& v)
{
    int n = v.size();
    vector<pair<int, int> > p(n);
    for(int i=0; i<n; ++i)
        p[i] = make_pair(v[i], i);
    sort(p.rbegin(), p.rend());

    BinaryIndexedTree bit(n);
    int ans = 0;
    for(int i=0; i<n; ++i){
        ans += bit.sum(p[i].second);
        bit.add(p[i].second, 1);
    }
    return ans;
}


double solve(vector<pair<double, double> > v)
{
    int n = v.size();
    int m = n * (n - 1) / 2;
    sort(v.rbegin(), v.rend());

    double left = -1.0e10;
    double right = 1.0e10;
    for(int t=0; t<200; ++t){
        double x = (left + right) / 2.0;
        vector<pair<double, int> > y(n);
        for(int i=0; i<n; ++i){
            y[i].first = v[i].first * x + v[i].second;
            y[i].second = i;
        }
        sort(y.begin(), y.end());

        vector<int> a(n);
        for(int i=0; i<n; ++i)
            a[i] = y[i].second;
        int b = inversionNumber(a);

        if(b < (m + 1) / 2)
            left = x;
        else
            right = x;
    }

    return left;
}

int main()
{
    int n;
    cin >> n;
    vector<double> a(n), b(n), c(n);
    for(int i=0; i<n; ++i)
        cin >> a[i] >> b[i] >> c[i];

    vector<pair<double, double> > v1(n), v2(n);
    for(int i=0; i<n; ++i){
        v1[i] = make_pair(-a[i] / b[i], c[i] / b[i]);
        v2[i] = make_pair(-b[i] / a[i], c[i] / a[i]);
    }
    printf("%.10f %.10f\n", solve(v1), solve(v2));

    return 0;
}
