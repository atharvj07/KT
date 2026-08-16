import java.io.IOException;
import java.io.PrintWriter;
import java.util.NoSuchElementException;
import java.util.Random;
import java.util.Scanner;
import java.util.function.BiFunction;

public class Main{
	static Scanner scn = new Scanner(System.in);
	static FastScanner sc = new FastScanner();
	static PrintWriter ot = new PrintWriter(System.out);
	static Random rand = new Random();
	static int mod = 1000000007;
	static long modmod = (long)mod * mod;
	static long inf = (long)1e17;
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
	static int[] dx8 = {-1,-1,-1,0,0,1,1,1};
	static int[] dy8 = {-1,0,1,-1,1,-1,0,1};
	static char[] dc = {'R','D','L','U'};
	static BiFunction<Integer,Integer,Integer> fmax = (a,b)-> {return Math.max(a,b);};
	static BiFunction<Integer,Integer,Integer> fmin = (a,b)-> {return Math.min(a,b);};
	static BiFunction<Integer,Integer,Integer> fsum = (a,b)-> {return a+b;};
	static BiFunction<Long,Long,Long> fmaxl = (a,b)-> {return Math.max(a,b);};
	static BiFunction<Long,Long,Long> fminl = (a,b)-> {return Math.min(a,b);};
	static BiFunction<Long,Long,Long> fsuml = (a,b)-> {return a+b;};
	static BiFunction<Integer,Integer,Integer> fadd = fsum;
	static BiFunction<Integer,Integer,Integer> fupd = (a,b)-> {return b;};
	static BiFunction<Long,Long,Long> faddl = fsuml;
	static BiFunction<Long,Long,Long> fupdl = (a,b)-> {return b;};
	static String sp = " ";
	
	public static void main(String[] args) {
		//AOJ2568 Everlasting -One-
		//author:Suunn
		//何もわからない、助けて
		//なんか条件を綺麗に言い換えるのかな...
		//2つの転職できる条件を言い換えると
		//同じ連結成分から白と黒の頂点を1つずつ選んで、塗り替える
		//白の頂点は必ず黒に塗り替える
		//黒の頂点はどちらにしてもよい
		//もう少し考える
		//白の頂点は黒に塗り替える
		//黒の頂点はだいたい白にしても黒にしてもよいが、最低1つ白の頂点と同じ連結成分にある
		//黒の頂点を選んで白にしなければならない
		
		//白と黒が両方ある連結成分を1つ選んで、そこは白と黒が両方あるまま、それ以外は自由に塗り替えみたいなことができる
		//（一旦連結成分の白黒以外全部黒にするみたいな感じでできる）
		//これを使ってどんな操作が可能か？
		//（大きさ3以上の連結成分があるとき、その中で選ぶ「白黒」の組は自由に変更できる）
		//（大きさ2以上の連結成分が2個以上あるとき、「白黒」を選ぶ連結成分は自由に変更できる）
		
		//ここまで分かれば後は算数するだけ？
		
		//「白黒」がないようなものは互いに行き来できない
		//「白黒」があるようなもの同士では必ず行き来が可能
		
		while(true) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			if(N==0)return;
			UnionFindTree UF = new UnionFindTree(N);
			for(int i=0;i<M;i++) {
				int a = sc.nextInt()-1;
				int b = sc.nextInt()-1;
				UF.unite(a,b);
			}
			long ans = 1;
			for(int i=0;i<N;i++) {
				if(UF.isRoot(i))ans *= 2;
				ans %= mod;
			}
			if(M!=0)ans++;
			System.out.println(ans%mod);
		}
	}
	
	
	


}

class UnionFindTree {
	int[] root;
	int[] rank;
	long[] size;
	int[] edge;
	int num;
	UnionFindTree(int N){
		root = new int[N];
		rank = new int[N];
		size = new long[N];
		edge = new int[N];
		num = N;
		for(int i=0;i<N;i++){
			root[i] = i;
			size[i] = 1;
		}
	}
	
	public long size(int x) {
		return size[find(x)];
	}
	public boolean isRoot(int x) {
		return x==find(x);
	}
	public long extraEdge(int x) {
		int r = find(x);
		return edge[r] - size[r] + 1;
	}
	public int find(int x){
		if(root[x]==x){
			return x;
		}else{
			return find(root[x]);
		}
	}

	public boolean unite(int x,int y){
		x = find(x);
		y = find(y);
		if(x==y){
			edge[x]++;
			return false;
		}else{
			num--;
			if(rank[x]<rank[y]){
				root[x] = y;
				size[y] += size[x];
				edge[y] += edge[x]+1;
			}else{
				root[y] = x;
				size[x] += size[y];
				edge[x] += edge[y]+1;
				if(rank[x]==rank[y]){
					rank[x]++;
				}
			}
			return true;
		}
	}

	public boolean same(int x,int y){
		return find(x)==find(y);
	}

}



class FastScanner {
    private final java.io.InputStream in = System.in;
    private final byte[] b = new byte[1024];
    private int p = 0;
    private int bl = 0;
    private boolean hNB() {
        if (p<bl) {
            return true;
        }else{
            p = 0;
            try {
                bl = in.read(b);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (bl<=0) {
                return false;
            }
        }
        return true;
    }

	private int rB() { if (hNB()) return b[p++]; else return -1;}
    private static boolean iPC(int c) { return 33 <= c && c <= 126;}
    private void sU() { while(hNB() && !iPC(b[p])) p++;}
    public boolean hN() { sU(); return hNB();}
    public String next() {
        if (!hN()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = rB();
        while(iPC(b)) {
            sb.appendCodePoint(b);
            b = rB();
        }
        return sb.toString();
    }
    public char nextChar() {
    	return next().charAt(0);
    }
    public long nextLong() {
        if (!hN()) throw new NoSuchElementException();
        long n = 0;
        boolean m = false;
        int b = rB();
        if (b=='-') {
            m=true;
            b=rB();
        }
        if (b<'0'||'9'<b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0'<=b&&b<='9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1||!iPC(b)){
                return (m?-n:n);
            }else{
                throw new NumberFormatException();
            }
            b = rB();
        }
    }
    public int nextInt() {
        if (!hN()) throw new NoSuchElementException();
        long n = 0;
        boolean m = false;
        int b = rB();
        if (b == '-') {
            m = true;
            b = rB();
        }
        if (b<'0'||'9'<b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0'<=b&&b<='9') {
                n *= 10;
                n += b-'0';
            }else if(b==-1||!iPC(b)){
                return (int) (m?-n:n);
            }else{
                throw new NumberFormatException();
            }
            b = rB();
        }
    }
    public int[] nextInts(int n) {
    	int[] a = new int[n];
    	for(int i=0;i<n;i++) {
    		a[i] = nextInt();
    	}
    	return a;
    }
    public int[] nextInts(int n,int s) {
    	int[] a = new int[n+s];
    	for(int i=s;i<n+s;i++) {
    		a[i] = nextInt();
    	}
    	return a;
    }
    public long[] nextLongs(int n, int s) {
    	long[] a = new long[n+s];
    	for(int i=s;i<n+s;i++) {
    		a[i] = nextLong();
    	}
    	return a;
	}
    public long[] nextLongs(int n) {
    	long[] a = new long[n];
    	for(int i=0;i<n;i++) {
    		a[i] = nextLong();
    	}
    	return a;
    }
    public int[][] nextIntses(int n,int m){
    	int[][] a = new int[n][m];
    	for(int i=0;i<n;i++) {
    		for(int j=0;j<m;j++) {
    			a[i][j] = nextInt();
    		}
    	}
    	return a;
    }

    public String[] nexts(int n) {
    	String[] a = new String[n];
    	for(int i=0;i<n;i++) {
    		a[i] = next();
    	}
    	return a;
    }
    void nextIntses(int n,int[] ...m) {
    	int l = m[0].length;
    	for(int i=0;i<l;i++) {
    		for(int j=0;j<m.length;j++) {
    			m[j][i] = nextInt();
    		}
    	}
    }
    void nextLongses(int n,long[] ...m) {
    	int l = m[0].length;
    	for(int i=0;i<l;i++) {
    		for(int j=0;j<m.length;j++) {
    			m[j][i] = nextLong();
    		}
    	}
    }

}






