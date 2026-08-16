#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<(int)(n); ++i)

using namespace std;
struct Card{
    char suit;
    int rank;
    bool operator < (const Card& c) const {
        if(rank != c.rank) return rank < c.rank;
        return suit < c.suit;
    }
};
typedef vector<Card> Deck;
const vector<int> None(5, -1);

Card stoc(string s) {
    Card c;
    c.suit = s[0];
    if(s[1] == 'A') c.rank = 14;
    else if(s[1] == 'K') c.rank = 13;
    else if(s[1] == 'Q') c.rank = 12;
    else if(s[1] == 'J') c.rank = 11;
    else if(s[1] == 'T') c.rank = 10;
    else c.rank = s[1] - '0';
    return c;
}

vector<int> highest(const Deck& d) {
    vector<int> a;
    a.reserve(5);
    for(auto& c : d) a.push_back(c.rank);
    sort(a.begin(), a.end(), greater<int>());
    return a;
}

vector<int> one_pair(const Deck& d, const vector<int>& a, int m[15]) {
    vector<int> res;
    res.reserve(5);
    for(auto c : a) if(m[c] != 2) res.push_back(c);
    if(res.size() != 3) return None;
    sort(res.begin(), res.end(), greater<int>());
    for(auto c : a) if(m[c] == 2) res.insert(res.begin(), c);
    assert(res.size() == 5);
    return res;
}

vector<int> two_pair(const Deck& d, const vector<int>& a, int m[15]) {
    vector<int> res;
    res.reserve(5);
    for(auto c : a) if(m[c] == 2) res.push_back(c);
    if(res.size() != 4) return None;
    sort(res.begin(), res.end(), greater<int>());
    for(auto c : a) if(m[c] == 1) res.push_back(c);
    assert(res.size() == 5);
    return res;
}

vector<int> three(const Deck& d, const vector<int>& a, int m[15]) {
    vector<int> res;
    res.reserve(5);
    for(auto c : a) if(m[c] != 3) res.push_back(c);
    if(res.size() != 2) return None;
    sort(res.begin(), res.end(), greater<int>());
    for(auto c : a) if(m[c] == 3) res.insert(res.begin(), c);
    return res;
}

vector<int> straight(const Deck& d, const vector<int>& a, int m[15]) {
    if(a[0] == 14 && a[1] == 5 && a[2] == 4 && a[3] == 3 && a[4] == 2) return {5, 4, 3, 2, 1}; // ????
    REP(i, 4) if(a[i] != a[i+1] + 1) return None;
    return a;
}

vector<int> flush(const Deck& d, const vector<int>& a, int m[15]) {
    int cnt[26] = {};
    for(auto& c : d) cnt[c.suit - 'A'] ++;
    if(cnt[d[0].suit - 'A'] == 5) return a;
    return None;
}

vector<int> full_house(const Deck& d, const vector<int>& a, int m[15]) {
    vector<int> res;
    res.reserve(5);
    for(auto c : a) if(m[c] == 3) res.push_back(c);
    if(res.size() != 3) return None;
    for(auto c : a) if(m[c] == 2) res.push_back(c);
    if(res.size() != 5) return None;
    return res;
}

vector<int> four(const Deck& d, const vector<int>& a, int m[15]) {
    vector<int> res;
    res.reserve(5);
    for(auto c : a) if(m[c] == 4) res.push_back(c);
    if(res.size() != 4) return None;
    for(auto c : a) if(m[c] == 1) res.push_back(c);
    assert(res.size() == 5);
    return res;
}

vector<int> straight_flush(const Deck& d, const vector<int>& a, int m[15]) {
    if(flush(d, a, m) == None) return None;
    return straight(d, a, m);
}

vector<int> royal(const Deck& d, const vector<int>& a, int m[15]) {
    if(straight_flush(d, a, m) == None) return None;
    if(a[0] == 14 && a[1] == 13) return a;
    return None;
}

bool win(const Deck& a, const Deck& b) {
    auto aa = highest(a);
    auto ab = highest(b);
    int ma[15] = {};
    for(auto c : aa) ma[c] += 1;
    int mb[15] = {};
    for(auto c : ab) mb[c] += 1;
#define check(func) do{ auto av = func(a, aa, ma); auto bv = func(b, ab, mb); if(av != bv) return av > bv; }while(false)
    check(royal);
    check(straight_flush);
    check(four);
    check(full_house);
    check(flush);
    check(straight);
    check(three);
    check(two_pair);
    check(one_pair);
    //check(highest);
#undef check
    if(aa != ab) return aa > ab;
    return false;
}

void print(Card c) {
    cout << "(" << c.suit << "," << c.rank << ")";
}


void print(Deck a) {
    assert(a.size() == 5);
    REP(i, 5) {
        print(a[i]);
        cout << " ";
    }
    cout << endl;
}


int main(){
    while(true) {
        string m1, m2;
        cin >> m1 >> m2;
        if(m1 == "#") break;
        vector<Card> my;
        vector<Card> your;
        my.push_back(stoc(m1));
        my.push_back(stoc(m2));
        REP(i, 2) {
            string s;
            cin >> s;
            your.push_back(stoc(s));
        }
        REP(i, 3) {
            string s;
            cin >> s;
            my.push_back(stoc(s));
            your.push_back(stoc(s));
        }
        set<Card> cset;
        for(auto c : my) cset.insert(c);
        for(auto c : your) cset.insert(c);

        vector<Card> cand;
        for(char a : string("SHDC")) {
            for(int r = 2; r <= 14; r++) {
                Card c = {a, r};
                if(!cset.count(c)) cand.push_back(c);
            }
        }
        int winc = 0, losec = 0;
        for(int i = 0; i < cand.size(); i++) {
            auto c1 = cand[i];
            for(int j = i + 1; j < cand.size(); j++) {
                auto c2 = cand[j];
                bool winb = false;
                auto myd = my;
                auto yourd = your;
                myd.push_back(c1); myd.push_back(c2);
                yourd.push_back(c1); yourd.push_back(c2);
                for(int s1 = (1 << 5) - 1; s1 < (1 << 7);){
                    // do something here
                    Deck md;
                    REP(k, 7) if(s1 >> k & 1) md.push_back(myd[k]);
                    bool exist = false;
                    for(int s2 = (1 << 5) - 1; s2 < (1 << 7);){
                        // do something here
                        Deck yd;
                        REP(k, 7) if(s2 >> k & 1) yd.push_back(yourd[k]);
                        if(!win(md, yd)){
                            exist = true;
                            break;
                        }
                        int x = s2 & -s2, y = s2 + x;
                        s2 = ((s2 & ~y) / x >> 1) | y;
                    }
                    if(!exist){
                        // print(c1); cout << " "; print(c2); cout << endl;
                        // print(md);
                        winb = true;
                        break;
                    }
                    int x = s1 & -s1, y = s1 + x;
                    s1 = ((s1 & ~y) / x >> 1) | y;
                }
                if(winb) winc ++;
                else losec++;
            }
        }
        //cout << winc << " " << losec << endl;
        printf("%.16f\n", 1.0 * winc / (winc + losec));
    }
    return 0;
}