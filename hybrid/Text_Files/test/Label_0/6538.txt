#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cctype>
#include<math.h>
#include<string>
#include<string.h>
#include<stack>
#include<queue>
#include<vector>
#include<utility>
#include<set>
#include<map>
#include<stdlib.h>
#include<iomanip>

using namespace std;

#define ll long long
#define ld long double
#define EPS 0.0000000001
#define INF 1e9
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<(n);i++)
#define loop(i,a,n) for(int i=a;i<(n);i++)
#define all(in) in.begin(),in.end()
#define shosu(x) fixed<<setprecision(x)

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;

int gcd(int a, int b){
    if(b==0) return a;
    return gcd(b,a%b);
}
int lcm(int a, int b){
    return a*b/gcd(a,b);
}


int main(void) {
    string s;
    cin >> s;
    vector<bool> c(4,false);
    int cur = 0;
    int ans = 0;
    rep(i,s.size()){
        if(s[i] == 'R'){
            cur = (cur + 1)%4;
            c[cur] = true;
        }else{
            c[cur] = false;
            cur = (4 + cur - 1)%4;
        }
        //cout << i << " " << cur << endl;
        //rep(i,4)cout << " " << c[i];
        //cout << endl;
        if(c[0] && c[1] && c[2] && c[3] && cur == 0){
            //cout << "! " << cur << endl;
            ans++;
            c[0] = c[1] = c[2] = c[3] = false;
        }
    }
    cout << ans << endl;
}

