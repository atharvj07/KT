#include<bits/stdc++.h>
using namespace std;

void problem_solver() {
    int n, u, v;
    cin >> n >> u >> v;
    vector<int> a(n);
    bool t1 = false, t2 = false, t3 = false;
    for(int i=0; i<n; i++)   cin >> a[i];
    for(int i=0; i<n-1; i++) {
        if(abs(a[i] - a[i+1]) > 1) {
            cout << 0;
            return;
        }
        if(a[i] - a[i+1] == 0)   t1 = true;
        if(abs(a[i] - a[i+1]) == 1)   t2 = true;
    }
    int cost = INT_MAX;
    if(t1) {
        cost = 2 * v;
        cost = min(cost, u + v);
    }
    if(t2) {
        cost = min(cost, min(u, v));
    }
    cout << cost;
}

int main() {
    int tt;
    cin >> tt;
    for(int t=1; t<=tt; t++) {
        problem_solver();
        cout << "\n";
    }
}
