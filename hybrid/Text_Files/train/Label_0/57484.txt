import java.util.*;
import java.io.*;

	
public class Main {
	public static void main(String[] args) throws Exception {
		FastScanner sc = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		
		int h = sc.nextInt();
		int w = sc.nextInt();
		int lim = sc.nextInt();
		
		String[] chocos = new String[h];
		int[][] acum = new int[h+1][w+1];
		fill(acum[0],0);
	   	for(int i=1; i<=h; i++){
	   	    acum[i][0]=0;
	   	}
		
	   	for(int i=0; i<h; i++){
	   	    chocos[i] = sc.next();
			for(int j=0; j<w; j++){
			    acum[i+1][j+1] = acum[i][j+1]+acum[i+1][j]-acum[i][j];
			    if(chocos[i].charAt(j)=='1') acum[i+1][j+1]++;
			}
	   	}
	   	
	   	int brokenH =0, sum=0, minX=INF;
	   	bitloop:
		for(int bit=0; bit < (1<<(h-1)); bit++){
		    ArrayList<Integer> broken_pos = new ArrayList<>();
		    broken_pos.add(-1);
			for(int i=0; i<(h-1); i++){
				if(isFlaged(bit,i)) broken_pos.add(i);
			}
			broken_pos.add(h-1);
			brokenH = broken_pos.size()-2;
			sum = brokenH;
			
			int last_broken=-1, t=0;
			while(t < w){
			    for(int j=0; j<=brokenH; j++){
			        //out.println(areaSum(acum,broken_pos.get(j),broken_pos.get(j+1),last_broken,t));
			        if(areaSum(acum,broken_pos.get(j),broken_pos.get(j+1),last_broken,t) > lim){
			            if(last_broken==(t-1)) continue bitloop;
			            last_broken=t-1;
			            sum++;
			            break;
			        }
			    }
			    t++;
			}
			minX = min(sum,minX);
		}
		out.println(minX);
		
		
		out.flush();
	}
	
    private static int areaSum(int[][] acum_plus1, int bY_notInclude, int aY_include, int bX_notInclude, int aX_include){
        int ans = acum_plus1[aY_include+1][aX_include+1];
        ans -= acum_plus1[aY_include+1][bX_notInclude+1];
        ans -= acum_plus1[bY_notInclude+1][aX_include+1];
        ans += acum_plus1[bY_notInclude+1][bX_notInclude+1];
        return ans;
    }

	private static int INF = (int)1e8;
	private static long INFL = (long)1e17;
	private static int e97 = (int)1e9 + 7;
	
	
	private static int abs(int a){
	    return (a>=0) ? a: -a;
	}
	private static long abs(long a){
	    return (a>=0) ? a: -a;
	}
	
	private static int min(int a, int b){
	    return (a>b) ? b : a;
	}
	private static long min(long a, long b){
	    return (a>b) ? b : a;
	}
	
	private static int max(int a, int b){
		return (a>b) ? a : b;
	}
	private static long max(long a, long b){
		return (a>b) ? a : b;
	}
	
	private static int minN(int... ins){
		int min = ins[0];
		for(int i=1; i<ins.length; i++){
			if(ins[i] < min) min = ins[i];
		}
		return min;
	}
	private static int maxN(int... ins){
		int max = ins[0];
		for(int i=1; i<ins.length; i++){
			if(ins[i] > max) max = ins[i];
		}
		return max;
	}
	private static long minN(long... ins){
		long min = ins[0];
		for(int i=1; i<ins.length; i++){
			if(ins[i] < min) min = ins[i];
		}
		return min;
	}
	private static long maxN(long... ins){
		long max = ins[0];
		for(int i=1; i<ins.length; i++){
			if(ins[i] > max) max = ins[i];
		}
		return max;
	}
	
	private static int minExAd(int[] dt, int ad){
	int min=Integer.MAX_VALUE;
		for(int i=0; i<dt.length; i++){
			if((i != ad) && (dt[i] < min)) min = dt[i];
		}
		return min;
	}
	private static long minExAd(long[] dt, int ad){
	long min=Long.MAX_VALUE;
		for(int i=0; i<dt.length; i++){
			if((i != ad) && (dt[i] < min)) min = dt[i];
		}
		return min;
	}
	private static int minExVal(int[] dt, int ex_val){
	int min=Integer.MAX_VALUE;
		for(int i=0; i<dt.length; i++){
			if((dt[i] != ex_val) && (dt[i] < min)) min = dt[i];
		}
		return min;
	}
	private static long minExVal(long[] dt, long ex_val){
	long min=Long.MAX_VALUE;
		for(int i=0; i<dt.length; i++){
			if((dt[i] != ex_val) && (dt[i] < min)) min = dt[i];
		}
		return min;
	}
	
	private static boolean same3(long a, long b, long c){
	if(a!=b) return false;
	if(b!=c) return false;
	if(c!=a) return false;
	return true;
	}
	private static boolean dif3(long a, long b, long c){
	if(a==b) return false;
	if(b==c) return false;
	if(c==a) return false;
	return true;
	}
	
	private static int factorial(int n) {
		int ans=1;
		for(int i=n; i>0; i--){
			ans*=i;
		}
		return ans;
	}
	
	private static long gcd(long m, long n) {
		if(m < n) return gcd(n, m);
		if(n == 0) return m;
		return gcd(n, m % n);
	}
	
	private static int pow2(int in){
		return in*in;
	}
	private static long pow2(long in){
		return in*in;
	}
	
	private static int getDigit2(long num){
		long cf = 1;
		int d=0;
		while(num >= cf){
			d++;
			cf = 1<<d;
		}
		return d; //numはd桁の数で、2^dより小さい
	}
	
	private static int getDigit10L(long num){
		long cf = 1;
		int d=0;
		while(num >= cf){
			d++;
			cf*=10;
		}
		return d; //numはd桁の数で、10^dより小さい
	}
	
	private static boolean isINF(int in){
	if((in*20)>INF) return true;
	else return false;
	}
	private static boolean isINFL(long in){
	if((in*10000)>INFL) return true;
	else return false;
	}
	
	private static long pow10E97(long ob, int soeji){
		if(soeji==2) return (ob*ob)%e97;
		
		int d = getDigit2(soeji);
		long[] ob_pow_2pow = new long[d];
		
		ob_pow_2pow[0] = ob;
		for(int i=1; i<d; i++){
			ob_pow_2pow[i] = (ob_pow_2pow[i-1]*ob_pow_2pow[i-1])%e97;
		}
		
		long ans=1;
		for(int i=d-1; i>=0; i--){
			if(soeji >= (1<<i)){
				soeji -= (1<<i);
				ans = (ans*ob_pow_2pow[i])%e97;
			}
 		}
		
		return ans;
	}
	
	
	private static int flag(int pos){
	    return (1<<pos);
	}
	private static boolean isFlaged(int bit, int pos){
    	if((bit&(1<<pos)) > 0) return true;
    	else return false;
	}
	private static int deflag(int bit, int pos){
	    return bit&~(1<<pos);
	}
	private static void showflag(int bit){
    	for(int i=0; i<getDigit2(bit); i++){
        	if(isFlaged(bit,i)) System.out.print("O");
        	else System.out.print(".");
    	}
	}
	
	
	private static void fill(boolean[] ob, boolean res){
		for(int i=0; i<ob.length; i++){
			ob[i] = res;
		}
		return;
	}
	private static void fill(int[] ob, int res){
		for(int i=0; i<ob.length; i++){
			ob[i] = res;
		}
		return;
	}
	private static void fill(long[] ob, long res){
		for(int i=0; i<ob.length; i++){
			ob[i] = res;
		}
		return;
	}
	private static void fill(char[] ob, char res){
		for(int i=0; i<ob.length; i++){
			ob[i] = res;
		}
		return;
	}
	private static void fill(int[][] ob, int res){
		for(int i=0; i<ob.length; i++){
			for(int j=0; j<ob[0].length; j++){
				ob[i][j] = res;
			}
		}
		return;
	}
	private static void fill(long[][] ob, long res){
		for(int i=0; i<ob.length; i++){
			for(int j=0; j<ob[0].length; j++){
				ob[i][j] = res;
			}
		}
		return;
	}
	private static void fill(char[][] ob, char res){
		for(int i=0; i<ob.length; i++){
			for(int j=0; j<ob[0].length; j++){
				ob[i][j] = res;
			}
		}
		return;
	}
	private static void fill(int[][][] ob, int res){
		for(int i=0; i<ob.length; i++){
			for(int j=0; j<ob[0].length; j++){
				for(int k=0; k<ob[0][0].length; k++){
			ob[i][j][k] = res;
				}
			}
		}
		return;
	}
	private static void fill(long[][][][] ob, long res){
		for(int i=0; i<ob.length; i++){
			for(int j=0; j<ob[0].length; j++){
				for(int k=0; k<ob[0][0].length; k++){
				for(int l=0; l<ob[0][0][0].length; l++){
				ob[i][j][k][l]=res;
				}
				}
			}
		}
		return;
	}
	
	static void show_b2d_array(boolean[][] dt, int lit_x, int lit_y){
		for(int i=0; i<dt[0].length; i++){
			for(int j=0; j<dt.length; j++){
				if((i==lit_y) && (j==lit_x)) System.out.print("X");
				else if(dt[j][i]) System.out.print("O");
				else System.out.print(".");
			}
			System.out.println();
		}
	}
	static void show_L2(long[][] dt, String cmnt){
		PrintWriter out = new PrintWriter(System.out);
		for(int i=0; i<dt[0].length; i++){
			for(int j=0; j<dt.length; j++){
				out.print(dt[j][i]+",");
			}
			out.println("<-"+cmnt+":"+i);
		}
		out.flush();
	}
	static void disp_que(ArrayDeque<Integer> dt){		//上手くいかなかった時用
		int a=0;
		while(dt.size()>0){
			a=dt.removeLast();
			System.out.print(a);
		}
		System.out.println("\n");
	}
	
	
	private static void nextPerm(ArrayList<Integer> former){
		int pivot=-1;
		int ln = former.size();
		for(int i = ln; i>1; i--){
			if(former.get(i-2) < former.get(i-1)){
				pivot = i-2;
				break;
			}
		}
		if(pivot==-1){
		former = null;
		return;
		}
		int pivot_fig = former.get(pivot);
		
		int min_pos=pivot+1;
		int min=former.get(min_pos);
		for(int i=ln-1; i > pivot+1; i--){
			if((former.get(i) < min)&&(former.get(i) > pivot_fig)){
				min_pos=i;
				min=former.get(min_pos);
			}
		}
		Collections.swap(former, pivot, min_pos);
		Collections.sort(former.subList(pivot+1, ln));
		return;
	}
	
	public static int binarySearch(int[] dt, int target){
		int left=0, right=dt.length-1;
		int mid=-1;
		while(left<=right){
			mid = (right+left)/2;
			if(dt[mid] == target) return mid;
			if(dt[mid] < target) left=mid+1;
			else right=mid-1;
		}
		return -1;
	}
	public static int binarySearchMax(long[] dt, long target){
		int left=-1, right=dt.length;
		int mid=-1;
		
		while((right-left)>1){
			mid = left + (right-left)/2;
			if(dt[mid] < target) left=mid;
			else right=mid;
		}
		return left;//target未満の最大のaddress
	}
	
	
	private static int dfs2(boolean[][] state, int x, int y, int depth){		//薄氷渡り
		int[] tmpltX = {1,-1,0,0};
		int[] tmpltY = {0,0,1,-1};
		int newX = -1, newY = -1;
		
		state[x][y] = false;
		depth++;
		
		int maxDunder_this_brunch = depth, tmpD=0;
		for(int i=0; i < 4; i++){
			newX = x+tmpltX[i];
			newY = y+tmpltY[i];
			if((newX >= 0) && (newY >= 0) && (newX < state.length) && (newY < state[0].length) && state[newX][newY]) tmpD = dfs2(state, newX, newY, depth);
			if(tmpD > maxDunder_this_brunch) maxDunder_this_brunch=tmpD;
		}
		state[x][y] = true;
		return maxDunder_this_brunch;
	}



static class Edge{
    int v2;
    long weight;
    public Edge(int vn, long w){
        this.v2 = vn;
        this.weight = w;
    }
}
static class Edge2{
    int v2;
    long cost1,cost2;
    public Edge2(int vn, long w1, long w2){
        this.v2 = vn;
        this.cost1 = w1;
        this.cost2 = w2;
    }
}

static class Comparator_Edge implements Comparator<Edge>{
    public int compare(Edge a, Edge b){
        if(a.weight>b.weight){
            return 1;
        }else if(a.weight<b.weight){
            return -1;
        }
        return 0;
    }
}
static class FastScanner {
	private final InputStream in = System.in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		}else{
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
	
	private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
	private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
	public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
	public String next() {
		if (!hasNext()) throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) throw new NoSuchElementException();
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
		while(true){
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			}else if(b == -1 || !isPrintableChar(b)){
				return minus ? -n : n;
			}else{
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
		return (int) nl;
	}
	public double nextDouble() { return Double.parseDouble(next());}
}
}