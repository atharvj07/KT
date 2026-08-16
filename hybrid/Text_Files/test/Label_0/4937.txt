#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll,ll> mp;
ll inf =  1e9;
typedef pair<ll,mp> mmp;

int main(){
    int y1,y2,m1,m2,d1,d2;
    cin>>y1>>m1>>d1>>y2>>m2>>d2;
    mmp a = mmp(y1,mp(m1,d1) );
    mmp b = mmp(y2,mp(m2,d2) );
    mmp m = min(a,b);
    mmp M = max(a,b);
    int dis = abs( y1-y2 );
    if( M.second.first > m.second.first || (M.second.first==m.second.first && M.second.second > m.second.second) ){
	cout<<dis + 1 <<endl;
    }else{
	cout<<dis<<endl;
    }

    return 0;
}

