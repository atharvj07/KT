#include <memory>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <numeric>
#include <complex>
#include <cassert>
#include <iterator>
#include <functional>
#if __cplusplus == 201103L
#include <tuple>
#endif

using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); ++i)
struct Tag{
    string name;
    string text;
    bool visible;
    vector<Tag*> child;
    Tag(string name) : name(name), visible(true) {}
    Tag(string name, string text) : name(name), text(text), visible(true) {}
    ~Tag(){
        for(auto ch : child) delete ch;
    }
};

typedef pair<Tag*, int> Result;
Result parse_dml(const string& s, int p = 0){
    assert(s[p++] == '<');
    string tag_name;
    while(s[p] != '>'){ tag_name += s[p++]; }
    assert(s[p++] == '>');

    Tag* tag = new Tag(tag_name);

    if(tag_name == "br") return Result(tag, p);

    while(s[p + 1] != '/'){
        if(s[p] == '<'){
            Result r = parse_dml(s, p);
            p = r.second;
            tag->child.push_back(r.first);
        }else{
            string text;
            while(s[p] != '<'){ text += s[p++]; }
            tag->child.push_back( new Tag("", text) );
        }
    }

    assert(s[p++] == '<');
    assert(s[p++] == '/');
    string tag_end;
    while(s[p] != '>') tag_end += s[p++];
    assert(tag_name == tag_end);
    assert(s[p++] == '>');
    return Result(tag, p);
}

void make_doc(Tag* p, Tag* doc[500][500], char view[500][500], int W, int H, int& x, int& y){
    if(! p->visible) return;
    if(p->name == "script") return;
    if(p->name == "br"){
        x = 0;
        y ++;
        return ;
    }

    for(auto np : p->child){
        if(np->text.empty()){
            make_doc(np, doc, view, W, H, x, y);
        }else{
            for(auto c : np->text) {
                if(y < H) doc[y][x] = p;
                if(y < H) view[y][x] = c;
                if(x + 1 < W){
                    x++;
                }else{
                    x = 0;
                    y++;
                }
            }
        }
    }
}

vector<string> collect_script(Tag* p, map<string, string>& file_dict){
    vector<string> res;
    if(p->name == "script"){
        assert(p->child[0]->text.size() > 0);
        string file = p->child[0]->text + ".ds";
        res.push_back(file_dict[file]);
        return res;
    }

    for(auto np : p->child){
        vector<string> vs = collect_script(np, file_dict);
        res.insert(res.end(), vs.begin(), vs.end());
    }
    return res;
}
void apply(Tag* p, bool rval, vector<string>& selectors, int k){
    if(p->name == selectors[k]) k++;
    if(k == (int)selectors.size() - 1) { // selectors[k] == "visible"
        p->visible = rval;
    }else{
        for(auto np : p->child){
            apply(np, rval, selectors, k);
        }
    }
}
void apply(Tag* root, string s){
    vector<string> token;
    string cur;
    for(auto c : s){
        if(cur == "=" || cur == "!=" || c == '!' || (cur != "!" && c == '=')) {
            token.push_back(cur);
            cur = "";
        }
        cur += c;
    }
    token.push_back(cur);
    reverse(token.begin(), token.end());

    bool rval = (token[0] == "true" ? true : false);
    for(int i = 2; i < (int)token.size(); i += 2){
        if(token[i - 1] == "!=") rval ^= rval;

        // split(token[i], ".")
        string t = token[i];
        for(auto& c : t) if(c == '.') c = ' ';
        stringstream ss(t);
        vector<string> selectors;
        while(ss >> t) selectors.push_back(t);

        apply(root, rval, selectors, 0);
    }
}
void run(Tag* root, string func, map<string, string>& file_dict){
    vector<string> scripts = collect_script(root, file_dict);
    for(string script : scripts){
        for(auto& c : script) if(c == '{' || c == '}') c = ' ';
        stringstream ss(script);
        string name, program;
        while(ss >> name >> program) if(name == func){
            for(auto& c : program) if(c == ';') c = ' ';
            stringstream ss(program);
            string sentence;
            while(ss >> sentence){ apply(root, sentence); }
        }
    }
}

int main(){
    int N;
    cin >> N;
    map<string, string> file_dict;
    for(int i = 0; i < N; i++) {
        string name, data;
        cin >> name;
        cin.ignore();
        getline(cin, data);
        file_dict[name] = data;
    }

    int M;
    cin >> M;
    while(M--){
        int W, H, S;
        string file;
        cin >> W >> H >> S >> file;
        Tag* root = parse_dml(file_dict.at(file + ".dml")).first;

        Tag* doc[500][500] = {};
        char view[500][500] = {};
        int docx = 0, docy = 0;
        make_doc(root, doc, view, W, H, docx, docy);

        while(S--){
            int x, y;
            cin >> x >> y;
            bool update = false;
            if(doc[y][x] && doc[y][x]->name == "link"){
                update = true;
                assert(doc[y][x]->child.size() == 1);
                file = doc[y][x]->child[0]->text;
                delete root;
                root = parse_dml(file_dict.at(file + ".dml")).first;
            }else if(doc[y][x] && doc[y][x]->name == "button"){
                update = true;
                assert(doc[y][x]->child.size() == 1);
                string func = doc[y][x]->child[0]->text;
                run(root, func, file_dict);
            }

            if(update){
                memset(doc, 0, sizeof(doc));
                memset(view, 0, sizeof(view));
                int docx = 0, docy = 0;
                make_doc(root, doc, view, W, H, docx, docy);
            }
        }
        for(int y = 0; y < H; y++){
            for(int x = 0; x < W; x++){
                if(view[y][x]) putchar(view[y][x]);
                else putchar('.');
            }
            putchar('\n');
        }
    }
    return 0;
}