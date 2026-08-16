#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<functional>
#define PAIR pair<int,int>
using namespace std;
class point{
public:
    vector<long long> dp;
    long long fast;
    point(){
        dp.resize(5,((long long)1<<63)-1);
        fast = 10000000;
    }
};
int H,W;
long long A,B,C,N;
vector<PAIR> mv;
class num{
public:
    long long time;
    PAIR pos;
    int dir;
};

bool operator<(const num&A,const num&B){
    return A.time<B.time;
}
bool operator>(const num&A,const num&B){
    return A.time>B.time;
}
bool operator==(const num&A,const num&B){
    return A.time==B.time;
}

PAIR operator + (const PAIR&A,const PAIR&B){
    PAIR res;
    res.first = A.first+B.first;
    res.second = A.second+B.second;
    return res;
}

point& getpa(vector<vector<point> >&map,PAIR d){
    int x =d.first;
    int y = d.second;
    return map[x][y];
}

void getfast(vector<vector<point> >&,vector<PAIR>&);
bool isin(int,int);
int main(){
    mv.resize(5);
    mv[0]=PAIR(1,0);
    mv[1]=PAIR(0,-1);
    mv[2]=PAIR(-1,0);
    mv[3]=PAIR(0,1);
    mv[4]=PAIR(0,0);
    cin>>H>>W>>A>>B>>C>>N;
    vector<vector<point> > map(W+1,vector<point>(H+1));
    vector<PAIR> player(N);
    for(int i=0;i<N;++i){
        cin>>player[i].second>>player[i].first;
    }
    getfast(map,player);
    priority_queue<num,vector<num>,greater<num> > que;
    getpa(map,player[0]).dp[4]=0;
    num start;
    start.time = 0;
    start.pos = player[0];
    start.dir = 4;
    /*
    for(int y=0;y<map.front().size();++y){
        for(int x=0;x<map.size();++x){
            cout<<map[x][y].dp[4]<<" ";
        }
        cout<<endl;
    }
     */
    que.push(start);
    while(!que.empty()){
        num d = que.top();
        que.pop();
        if(d.time!=getpa(map,d.pos).dp[d.dir]){
            continue;
        }
        if(d.dir<4){
            PAIR np = d.pos + mv[d.dir];
            if(isin(np.first,np.second)){
                long long ntime = d.time + A;
                if(ntime<getpa(map,np).dp[d.dir]){
                    getpa(map,np).dp[d.dir] = ntime;
                    num dnum;
                    dnum.time = ntime;
                    dnum.pos = np;
                    dnum.dir = d.dir;
                    que.push(dnum);
                }
            }
            long long ntime = d.time + getpa(map,d.pos).fast;
            if(ntime<getpa(map,d.pos).dp[4]){
                getpa(map,d.pos).dp[4] = ntime;
                num dnum;
                dnum.time = ntime;
                dnum.pos = d.pos;
                dnum.dir = 4;
                que.push(dnum);
            }
        }else{
            for(int i=0;i<4;++i){
                long long ntime = d.time + B;
                if(ntime<getpa(map,d.pos).dp[i]){
                    getpa(map,d.pos).dp[i]=ntime;
                    num dnum;
                    dnum.time = ntime;
                    dnum.pos = d.pos;
                    dnum.dir = i;
                    que.push(dnum);
                }
                ntime = d.time + C;
                PAIR np = d.pos + mv[i];
                if(!isin(np.first,np.second)){
                    continue;
                }
                if(ntime<getpa(map,np).dp[4]){
                    getpa(map,np).dp[4]=ntime;
                    num dnum;
                    dnum.time = ntime;
                    dnum.pos = np;
                    dnum.dir = 4;
                    que.push(dnum);
                }
            }
        }
    }
    cout<<getpa(map,player.back()).dp[4]<<endl;
    
    /*
    for(int y=0;y<map.front().size();++y){
        for(int x=0;x<map.size();++x){
            cout<<map[x][y].dp[4]<<" ";
        }
        cout<<endl;
    }
     */
    return 0;
}

void getfast(vector<vector<point> >& map,vector<PAIR>&player){
    queue<PAIR> que;
    for(int i=0;i<player.size();++i){
        int x = player[i].first;
        int y = player[i].second;
        que.push(player[i]);
        getpa(map,player[i]).fast=0;
    }
    while(!que.empty()){
        PAIR d = que.front();
        que.pop();
        for(int i=0;i<4;++i){
            PAIR np = d+mv[i];
            if(!isin(np.first,np.second)){
                continue;
            }
            if(getpa(map,np).fast>getpa(map,d).fast+1){
                getpa(map,np).fast = getpa(map,d).fast+1;
                que.push(np);
            }
        }
    }
    for(int x=0;x<map.size();++x){
        for(int y=0;y<map.front().size();++y){
            getpa(map,PAIR(x,y)).fast*=C;
        }
    }
}

bool isin(int x,int y){
    return x>=0&&x<=W&&y>=0&&y<=H;
}
