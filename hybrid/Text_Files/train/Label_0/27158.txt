#include <iostream>
#include <vector>

using namespace std;

template<typename T>
class SegTree {
public:
    explicit SegTree(int n, T def) : N(calcN_(n)), def(def), mVal(2*calcN_(n)-1, def) {}
    void update(int idx, T value){
        int i = N + idx - 1;
        update_(mVal[i], value);
        while(i > 0){
            i = (i-1)/2;
            mVal[i] = operate(mVal[2*i+1], mVal[2*i+2]);
        }
    }
    T get(int l, int r){
        l = max(0, l);
        r = min(N, r);
        int offset = N;
        T resL = def;
        T resR = def;
        while(offset > 0){
            if(l >= r) break;
            if(l&1){ resL = operate(resL, mVal[offset+l-1]); l++; }
            if(r&1){ resR = operate(mVal[offset+r-2], resR); }
            l /= 2;
            r /= 2;
            offset /= 2;
        }
        return operate(resL, resR);
    }
    int maxRight(int l, T v){
        l = max(0, l) + N;
        T resL = def;
        while(l){
            if(l&1){
                T next = operate(resL, mVal[l-1]);
                if(next >= v){
                    while(l < N){
                        l *= 2;
                        next = operate(resL, mVal[l-1]);
                        if(next < v){
                            resL = next;
                            ++l;
                        }
                    }
                    return l - N;
                }
                resL = next;
                if(!(l&(l+1))) break;
                l++;
            }
            l /= 2;
        }
        return N;
    }
private:
    int calcN_(int n){
        int res = 1;
        while(res < n) res *= 2;
        return res;
    }
    void update_(T& data, T val) { data = val; }
    T operate(T a, T b) { return max(a, b); }
    const int N;
    const T def;
    vector<T> mVal;
};

int main(){
    int N, Q; cin >> N >> Q;
    SegTree<int> seg(N, 0);
    for(int i=0;i<N;i++){
        int a; cin >> a;
        seg.update(i, a);
    }
    for(int i=0;i<Q;i++){
        int t, x, v; cin >> t >> x >> v;
        if(t==1){
            seg.update(x-1, v);
        } else if(t==2){
            cout << seg.get(x-1, v) << endl;
        } else {
            cout << min(seg.maxRight(x-1, v), N) + 1 << endl;
        }
    }
}