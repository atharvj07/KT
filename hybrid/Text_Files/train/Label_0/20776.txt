#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>
#include <cassert>

const int wmax=4;
const int hmax=4;
const int rmax=5;

const int vx[]={0,1,0,-1};
const int vy[]={-1,0,1,0};

bool simul(std::vector<std::vector<int>> &m,int h,int w){//ある盤面で(h,w)をクリックした結果を上書きし、全消ししているかを返す
    std::queue<std::tuple<int,int,int,int>> drops;
    if(m[h][w]==4){
        m[h][w]=0;
        for (int d = 0; d < 4; ++d) {
            drops.push(std::make_tuple(h,w,d,0));
        }
    }
    else{
        ++m[h][w];
        return false;
    }
    int maxt=0;
    bool needupd=false;
    while(!drops.empty()|| needupd){
        if(needupd){
            needupd=false;
            ++maxt;
            for (int i = 0; i < hmax; ++i) {
                for (int j = 0; j < wmax; ++j) {
                    if(m[i][j]>=5){
                        for (int d = 0; d < 4; ++d) {
                            drops.push(std::make_tuple(i,j,d,maxt));
                        }
                        m[i][j]=0;
                    }
                }
            }
            continue;
        }
        auto t=drops.front();
        int& nh=std::get<0>(t);
        int& nw=std::get<1>(t);
        int& nd=std::get<2>(t);
        int& nt=std::get<3>(t);
        //assert(nd>=0&&nd<4);
        if(maxt<nt){
            ++maxt;
            needupd=true;
            continue;
        }
        drops.pop();
        if(drops.empty())needupd=true;
        nh+=vy[nd];
        nw+=vx[nd];
        if(nh<0||nh>=hmax||nw<0||nw>=wmax)continue;//外に出る
        assert(nh>=0);
        if(m[nh][nw]==0){//通り過ぎる
            drops.push(std::make_tuple(nh,nw,nd,maxt+1));
        }
        else{//ぶつかる
            ++m[nh][nw];

        }
    }
    for (int i = 0; i < hmax; ++i) {
        for (int j = 0; j < wmax; ++j) {
            if(m[i][j]!=0)return false;
        }
    }
    return true;
}

int dfs(std::vector<std::vector<int>> &m,int r){//r回クリックした状態と盤面mから消すまでの最小回数
    if(r>rmax)return rmax+1;
    int ans=rmax+1;
    for (int h = 0; h < hmax; ++h) {
        for (int w = 0; w < wmax; ++w) {
            //if(m[h][w]<r)continue;
            auto tm=m;
            if(simul(tm,h,w))ans=std::min(ans,r);
            else ans=std::min(ans,dfs(tm,r+1));
        }
    }
    return ans;
}

int main(){
    std::vector<std::vector<int>> m(hmax,std::vector<int>(wmax));
    for (int i = 0; i < hmax; ++i) {
        for (int j = 0; j < wmax; ++j) {
            std::cin>>m[i][j];
        }
    }
    for (int i = 0; i < hmax; ++i) {
        for (int j = 0; j < wmax; ++j) {
            if(m[i][j]!=0){
                goto e;
            }
        }
    }
    std::cout<<0<<std::endl;
    return 0;
    e:;
    int ans=dfs(m,1);
    std::cout<<(ans==rmax+1?-1:ans)<<std::endl;

    return 0;
}
