import java.io.*;
import java.util.*;


class Main {
    static long sq(long x){return x*x;}
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        int n=sc.nextInt();
        int m=sc.nextInt();
        UnionFind u=new UnionFind(n);
        for(int i=0;i<m;++i){
            int a=sc.nextInt()-1;
            int b=sc.nextInt()-1;
            u.unify(a,b);
        }
        int d0=0;
        int d1=0;
        for(int i=0;i<n;++i){
            if(u.root(i)==u.root(0))d0++;
            if(u.root(i)==u.root(1))d1++;
        }
        long ans=Math.max(sq(n-d0)+sq(d0),sq(n-d1)+sq(d1));
        ans=(ans-n)/2;
        ans-=m;
        out.println(ans);
        out.close();
    }
    // http://codeforces.com/blog/entry/7018
    //-----------PrintWriter for faster output---------------------------------
    public static PrintWriter out;
    //-----------MyScanner class for faster input----------
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;
        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
        int[] nextIntArray(int n){
            int[]r=new int[n];
            for(int i=0;i<n;++i)r[i]=nextInt();
            return r;
        }
    }
}
class UnionFind {
    int[] parent;
    int[] rank;
    UnionFind(int n) {
	this.parent = new int[n];
	this.rank = new int[n];
	this.clear();
    }
    void clear() {
	int n = this.parent.length;
	for (int i = 0; i < n; ++i) {
	    this.parent[i] = i;
	    this.rank[i] = 0;
	}
    }
    void unify(int x, int y) {
	int rootX = this.root(x);
	int rootY = this.root(y);
	if (rootX == rootY) {
	    return;
	}
	if (this.rank[rootX] < this.rank[rootY]) {
	    this.parent[rootX] = rootY;
	} else {
	    this.parent[rootY] = rootX;
	    if (this.rank[rootX] == this.rank[rootY]) {
		this.rank[rootX]++;
	    }
	}
    }
    int root(int x) {
	if (this.parent[x] == x) {
	    return x;
	}
	return this.parent[x] = this.root(this.parent[x]);
    }
}
