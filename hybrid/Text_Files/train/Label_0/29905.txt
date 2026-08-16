#include "bits/stdc++.h"

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

#define dump(x)  cerr << #x << " = " << (x) << endl
#define rep(i,n) for(int i=0;i<(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb push_back


int dist( pii a,pii b){
    int y=a.first-b.first;
    int x=a.second-b.second;
    
    return (x*x + y*y);
}



int main(){
    int loop;
    cin>>loop;
    rep(i,loop){
        
        int n,x,y;
        cin>>n>>x>>y;
        
        pii start;
        cin>>start.second>>start.first;
        
        pii cat[2000];
        rep(i,n){
            cin>>cat[i].second>>cat[i].first;
        }
        
//        if( x>=y ){cout<<"You're always welcome!"<<endl;continue;}
        
        vi connect[2000];
        
        rep(i,n){
            rep(j,n){
                if(i!=j){
                    if( dist(cat[i],cat[j])<=2500 ){
                        connect[i].pb(j);
                        connect[j].pb(i);
                    }
                }
            }
        }
        
        int used[2000];
        rep(i,2000)used[i]=-9999;

        queue<int> que;
        
        rep(i,n){
            if( dist(start,cat[i])<=100 ){
                que.push(i);
                used[i]=x;
            }
        }
        int term=0;
        if( que.size() )term++;
        
        int now=0;
        int times=0;
        while(que.size()){
            times++;
            now=term*x;
            int len=que.size();
            rep(i,len){
                int qf=que.front();
                for( int j=0;j<connect[qf].size();j++){
                    int connected = connect[qf][j];
                    if( now-used[ connected ]>y ){
                        que.push( connected );
                        used[ connected ] = now+x;
                    }
                }
                que.pop();
            }
            if(times>2000)break;
            term++;
        }
        
//        while( que.size() ){
//            now=term*x;
//            bool flag=true;
//            times++;
//            int qf=que.front();
//            for( int i=0;i<connect[qf].size();i++ ){
//                int connected = connect[qf][i];
//                if( now-used[ connected ]>y ){  // >= ?
//                    if(flag)term++;
//                    flag=false;
//                    que.push( connected );
//                    used[ connected ]=now+x;    // now+x-1 ?
//                }
//            }
//            que.pop();
//            if(times>10000)break;
//        }
        
        
        if(times>2000)cout<<"You're always welcome!"<<endl;
        else cout<<now<<endl;
    }
}