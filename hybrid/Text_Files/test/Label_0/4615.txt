//@uthor: _|EE|_RB30
 
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define vi vector<int>
#define vpi vector<pair<int,int>>
#define pii pair<int,int>
#define mii map<int,int>
#define mpi map<pair<int,int>,int>
#define pb push_back
#define M 1000000007
#define pi 3.141592653589793238
#define endl "\n"
#define cap__ ios_base::sync_with_stdio(0);cin.tie(0);

int power(int x,int n){
    int res = 1;
    while(n){
        if(n%2){
            res = res*x;
        }
        x = x*x;
        n/=2;
    }
    return res;
}

signed main()
{
    cap__;

    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int a[k],t[k];
        for(int i=0;i<k;i++){
            cin>>a[i];
        }
        for(int i=0;i<k;i++){
            cin>>t[i];
        }
        priority_queue<pii,vpi,greater<pii>> q;
        vi res(n,INT_MAX);
        for(int i=0;i<k;i++){
            q.push({t[i],a[i]-1});
            res[a[i]-1] = t[i];
        }
        mii mm;
        int c = 0;
        while(!q.empty()){
            int x = q.top().first;
            int y = q.top().second;
            q.pop();
            mm[y]++;
            if(y+1<n && mm.find(y+1)==mm.end() && res[y+1]>res[y]+1){
                res[y+1] = res[y]+1;
                q.push({x+1,y+1});
            }
            if(y-1>=0 && mm.find(y-1)==mm.end() && res[y-1]>res[y]+1){
                res[y-1] = res[y]+1;
                q.push({x+1,y-1});
            }
        }
        for(int i=0;i<n;i++){
            cout<<res[i]<<" ";
        }
        cout<<endl;
    }    
}