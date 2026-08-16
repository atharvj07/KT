#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#define loop(i,a,b) for(int i=a; i<b; i++)
#define rep(i,b) loop(i,0,b)
#define all(c) (c).begin(), (c).end()

using namespace std;

typedef vector<int> vi;

int main(){
    int n;
    while (cin >> n && n){
        vi v(n);
        int c = 0;
        rep(i, n) cin >> v[i];
        while(1){
            vi next(n);
            map<int, int> m;
            rep(i, n) m[v[i]]++;
            rep(i, n) next[i] = m[v[i]];
            if (next == v) break;
            c++;
            v = next;
        }

        cout << c << endl;
        rep(i, n - 1){
            cout << v[i] << " ";
        }
        cout << v.back() << endl;
    }
}