import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        FastScanner sc = new FastScanner();
         
        int n = sc.nextInt();
        RootedTree t = new RootedTree(n);
        
        for(int i=0;i<n;i++){
        	int k = sc.nextInt();
        	for(int j=0;j<k;j++){
        		t.addChild(i,sc.nextInt());
        	}
        }
        
        t.makeDepthTable();
        t.makeLCATable();
        
        int q = sc.nextInt();
        
        for(int i=0;i<q;i++){
        	System.out.println(t.LCA(sc.nextInt(),sc.nextInt()));
        }
        
    }

}

class RootedTree {
	int[] parent;
	NodeList[] child;
	int[] depth; //深さのテーブル。makeDepthTableを呼ぶまで作成されない。
	int[][] LCAtable; //LCA用テーブル。makeLCATableを呼ぶまで作成されない。[k][v]が2^k回親を辿ったときに到達する頂点。
	
	public RootedTree(int vnum){
		parent = new int[vnum];
		parent[0] = -1;
		
		child= new NodeList[vnum];
		
		for(int i=0;i<vnum;i++){
			child[i] = new NodeList();
		}
		
	}
	
	int vnum(){
		return parent.length;
	}
	
	//親に子を登録（同時に子に親を登録）
	void addChild(int par, int chil){
		child[par].add(chil);
		parent[chil] = par;
	}
	
	NodeList getChildren(int n){
		return child[n];
	}
	
	int getParent(int n){
		return parent[n];
	}
	
	//深さのテーブルを作る（bfs）
	void makeDepthTable(){
		depth = new int[vnum()];
		Arrays.fill(depth,-1);
		depth[0] = 0;
		
		ArrayDeque<Integer> q = new ArrayDeque<>();
		q.add(0);
		
		while(!q.isEmpty()){
			int p = q.pollFirst();
			
			for(int c:getChildren(p)){
				depth[c] = depth[p]+1;
				q.add(c);
			}
		}
	}
	
	//LCA用のテーブルを作る
	void makeLCATable(){
		int logV = log2ceil(vnum()-1);
		LCAtable = new int[logV][vnum()];
		
		for(int v=0;v<vnum();v++){
			LCAtable[0][v] = parent[v];
		}
		
        for(int k=0;k<logV-1;k++) {
            for(int v=0;v<vnum();v++) {
                if(LCAtable[k][v] < 0) {
                	LCAtable[k+1][v] = -1;
                }else {
                	LCAtable[k+1][v] = LCAtable[k][LCAtable[k][v]];
                }
            }
        }
	}
	//log_2(N)の天井
	static int log2ceil(int n){
		if(n<=1){
			return 1; //意図的
		}
		return Integer.numberOfTrailingZeros(Integer.highestOneBit(n-1))+1;
	}
	//2のn乗（ビット演算）
	static int twoPow(int n){
		return 1<<n;
	}
	
	//aとbのLCA(Lowest Common Ancestor)をLCAテーブルと深さテーブルを用いて求める
	int LCA(int u, int v){
		int logV = log2ceil(vnum());
		
        if( depth[u] > depth[v] ) {
            int t = u; u = v; v = t;
        }

        for (int k = 0; k < logV; k++) {
            if(((depth[v] - depth[u]) >> k & 1) == 1) {
                v = LCAtable[k][v];
            }
        }
        if( u == v ) return u;

        for (int k = logV-1; k >= 0; k--) {
            if( LCAtable[k][u] != LCAtable[k][v] ) {
                u = LCAtable[k][u];
                v = LCAtable[k][v];
            }
        }
        return LCAtable[0][u];
	}
	
	class NodeList extends ArrayList<Integer>{
		private static final long serialVersionUID = -2846301604366508341L;
	}
}


class FastScanner {
	private final InputStream in = System.in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		} else {
			ptr = 0;
			try {
				buflen = in.read(buffer);
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen <= 0) {
				return false;
			}
		}
		return true;
	}
	private int readByte() {
		if (hasNextByte())
			return buffer[ptr++];
		else
			return -1;
	}
	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}
	public boolean hasNext() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr]))
			ptr++;
		return hasNextByte();
	}
	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext())
			throw new NoSuchElementException();
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while (true) {
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			} else if (b == -1 || !isPrintableChar(b)) {
				return minus ? -n : n;
			} else {
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)
			throw new NumberFormatException();
		return (int) nl;
	}
	public double nextDouble() {
		return Double.parseDouble(next());
	}
}
