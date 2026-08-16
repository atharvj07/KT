#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <tuple>
#include <queue>
#include <list>
using namespace std;
// #define fprintf(...) void(0)

bool judge(int N, int T,
           const vector< tuple<int, int, int> > &info, int O) {
    priority_queue< int, vector<int>, greater<int> > op;
    list< pair<int, int> > cs;
    for(int i=0; i<O; i++) op.emplace(0);
    for(int i=0; i<N; i++) cs.emplace_back(0, i);

    // fprintf(stderr, "# num of operators = %d\n", O);
    for(int t=0; t<=T and cs.size(); t++) {
        // customer 選ぶ
        for(auto itr = cs.begin(); itr!=cs.end(); ) {
            int p, k; tie(p, k) = *itr;
            int M, L, K; tie(M, L, K) = info[k];

            bool inc = false;
            if(p <= t and t + M <= T) {
                int o = op.top(); op.pop();
                if(o > t) {
                    // 対応できる operator がいない
                    op.emplace(o);
                    inc = true;
                }
                else {
                    // 対応
                    // fprintf(stderr, "t = %d, customer = %d, op time = %d\n", t, k + 1, o);
                    itr = cs.erase(itr);
                    op.emplace(t + M);
                }
            }
            else if(t + M > T) {
                return false;
            }
            else {
                inc = true;
            }
            
            if(inc) {
                // update time
                if(t - L == p) {
                    // fprintf(stderr, "t = %d, update: customer = %d, time = %d\n", t, k+1, t+K);
                    *itr = make_pair(t+K, k);
                    if(t + K > T) return false;
                }
                itr++;
            }
        }
    }

    return cs.empty();
}

int solve_testcase() {
    int N, T; cin >> N >> T;
    if(N == 0 and T == 0) return 1;

    vector< tuple<int, int, int> > info;
    for(int i=0; i<N; i++) {
        int M, L, K; cin >> M >> L >> K;
        info.emplace_back(M, L, K);
    }

    for(int m=1; m<=N; m++) {
        if(judge(N, T, info, m)) {
            cout << m << endl;
            return 0;
        }
    }
    return 0;
}

int main() {
    while(!solve_testcase());
    return 0;
}

