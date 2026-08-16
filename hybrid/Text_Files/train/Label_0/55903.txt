import java.io.*;
import java.util.*;

class Main {
    static class UnionFind {
	int [] data;
	UnionFind(int n) {
	    data = new int[n];
	    for(int i = 0; i < n; i++) data[i] = -1;
	}
	int root(int x) {
	    if(data[x] < 0) return x;
	    data[x] = root(data[x]);
	    return data[x];
	}
	boolean find(int x, int y) { 
	    return root(x) == root(y);
	}
	void union(int x,  int y) {
	    x = root(x); 
	    y = root(y);
	    if (x != y) {
		if (data[x] < data[y]) {
		    int t = x;
		    x = y;
		    y = t;
		}
		data[x] += data[y]; 
		data[y] = x;
	    }
	}
    }
    static int n;
    public static void main(String [] args) throws Exception {
	Scanner sc = new Scanner(System.in);
	n = sc.nextInt();
	int m = sc.nextInt();
	int [][] es = new int[m][4];
	for(int i = 0; i < m; i++) {
	    es[i][1] = sc.nextInt() - 1; // from
	    es[i][2] = sc.nextInt() - 1; // to
	    es[i][0] = sc.nextInt(); // cost
	    es[i][3] = 0;
	}
	Arrays.sort(es, new Comparator<int[]>() {
		public int compare(int [] x1, int [] x2) {
		    for(int i = 0; i < 3; i++) {
			int d = x1[i] - x2[i];
			if(d != 0) return d;
		    }
		    return 0;
		}
		public boolean equals(Object o) { return true; }
	    });
	int mn = mst(es, -1);
	// System.out.println("mst = " + mn);
	int c = 0, k = 0;
	for(int i = 0; i < es.length; i++) {
	    if(es[i][3] == 1) {
		int mm = mst(es, i);
		if(mm != mn) {
		    c += es[i][0];
		    k++;
		}
	    }
	}
	System.out.println("" + k + " " + c);
    }
    static int mst(int [][] es, int skip) {
	UnionFind uf = new UnionFind(n);
	int c = 0;
	for(int i = 0; i < es.length; i++) {
	    if(i == skip) continue;
	    if(!uf.find(es[i][1], es[i][2])) {
		c += es[i][0];
		es[i][3] = 1;
	    }
	    uf.union(es[i][1], es[i][2]);
	}
	return c;
    }
}

