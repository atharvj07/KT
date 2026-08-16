#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<(int)(n); ++i)

using namespace std;
struct UnionFind{
    vector<int> parent;
    vector<long long> edge;
    vector<long long> node;

    UnionFind(int N) : parent(N, -1), edge(N, 0), node(N, 0) {}

    void print(int x){
        printf("%d: parent:%d edge:%lld node:%lld\n", x, parent[x], edge[x], node[x]);
    }

    // (root_index, root_value - x_value)
    pair<int, long long> root(int x){
        if(parent[x] < 0){
            return make_pair(x, 0);
        }else{
            pair<int, long long> p = root(parent[x]);
            p.second += edge[x] + node[parent[x]];

            // update
            parent[x] = p.first;
            edge[x] = p.second - node[ parent[x] ]; // edge + node[parent] = p.second
            return p;
        }
    }

    void unite(int x, int y, int c){
        // y - x = c
        node[x] += c;
        node[y] += c;
        edge[x] -= c;
        edge[y] -= c;

        pair<int, long long> px = root(x);
        pair<int, long long> py = root(y);
        if(px.first == py.first) return;
        parent[px.first] = py.first;
        edge[px.first] = py.second - px.second + c - node[py.first];

    }

    // return y - x
    long long compare(int x, int y){
        pair<int, long long> px = root(x);
        pair<int, long long> py = root(y);
        if(px.first != py.first) return LLONG_MIN;
        return -(py.second - px.second);
    }
};

int main(){
    int N, Q;
    while(cin >> N >> Q){
        UnionFind UF(N + 1);
        while(Q --> 0){
            string query;
            cin >> query;
            if(query == "COMPARE"){
                int x, y;
                cin >> x >> y;
                long long answer = UF.compare(x, y);
                cout << (answer > LLONG_MIN ? to_string(answer) : "WARNING") << endl;
            }else if(query == "IN"){
                int x, y, c;
                cin >> x >> y >> c;
                UF.unite(x, y, c);
            }
        }
    }
    return 0;
}