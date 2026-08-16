
import java.util.*;
import java.lang.*;
import java.lang.reflect.Array;
import java.io.*;
import java.math.*;
import java.text.DecimalFormat;
public class Temp{     
    static class InputReader { 
        private final InputStream stream;
	private final byte[] buf = new byte[8192];
	private int curChar, snumChars;
 	public InputReader(InputStream st) {
            this.stream = st;
	} 
	public int read() {
            if (snumChars == -1)
	 	throw new InputMismatchException();
            if (curChar >= snumChars) {
		curChar = 0;
                try {
                    snumChars = stream.read(buf);
		} 
                catch (IOException e) {
                    throw new InputMismatchException();
           	}
		if (snumChars <= 0)
                    return -1;
            }
            return buf[curChar++];
	}
        public int ni() {
            int c = read();
            while (isSpaceChar(c)) {
               	c = read();
            }
            int sgn = 1;
            if (c == '-') {
		sgn = -1;
		c = read();
            }
            int res = 0;
            do {
		res *= 10;
		res += c - '0';
		c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
	} 
	public long nl() {
            int c = read();
            while (isSpaceChar(c)) {
            c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
	} 
	public int[] nia(int n) {
            int a[] = new int[n];
            for (int i = 0; i < n; i++) {
		a[i] = ni();
            }
            return a;
	} 
	public String rs() {
            int c = read();
            while (isSpaceChar(c)) {
		c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
		res.appendCodePoint(c);
                    c = read();
            } while (!isSpaceChar(c));
            return res.toString();
	}
	public String nextLine() {
            int c = read();
            while (isSpaceChar(c))
		c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isEndOfLine(c));
            return res.toString();
        } 
	public boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
	}
 
	private boolean isEndOfLine(int c) {
            return c == '\n' || c == '\r' || c == -1;
	} 
    }
    static PrintWriter w = new PrintWriter(System.out);
    public static class Key {

        private final int x;
        private final int y;

        public Key(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Key)) return false;
            Key key = (Key) o;
            return x == key.x && y == key.y;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            return result;
        }
    }
    static long mod=1000000007L;
    static ArrayList<Integer> arr[];
    static int n;
    static boolean prime[]=new boolean[(int)(1e7+1)];
    static ArrayList<Integer> pri=new ArrayList<>();
    static int maxD[]=new int[(int)3e6+1];
    static void findMaxD(){
        for(int i:pri){
            if(i<=2)continue;
            if(prime[i]){
                for(int j=3;(j*i)<=(int)3e6;j+=2){
                    maxD[j*i]=Math.max(Math.max(i, j),maxD[j*i]);
                }
            }    
        }
        for(int i=2;i<=(int)3e6;i+=2){
            maxD[i]=i/2;
        }
    }

    static void sieve() {
	Arrays.fill(prime, true);
        pri.add(-1);
	prime[0] = prime[1] = false;
	for(int i = 2 ; i <=(int)1e7 ; ++i) {
            if(prime[i]) {
                pri.add(i);
                int j=2*i;
                while(j<=(int)1e7){
                    prime[j]=false;
                    j+=i;
                }
            }
	}
			
    }
    public static void main (String[] args)throws IOException{
        InputReader sc=new InputReader(System.in);
        sieve();
        findMaxD();
        
        int n=sc.ni();
        //TreeMap<Integer,Integer> map=new TreeMap<>();
        int co[]=new int[(int)3e6+1];
        for(int i=0;i<2*n;i++){
            int a=sc.ni();
            co[a]++;
//            if(map.containsKey(a))map.replace(a,map.get(a)+1);
//            else map.put(a,1);
        }
        ArrayList<Integer> ans=new ArrayList<>();
        for(int i=(int)3e6;i>2;i--){
            if(co[i]>0&&!prime[i]){
                int l=co[i];
                for(int k=0;k<l&&co[maxD[i]]>0;k++){
                    ans.add(i);
                    co[i]--;
                    co[maxD[i]]--;
                }
            }
        }
        for(int i=2;i<=(int)3e6;i++){
            if(co[i]>0&&prime[i]){
                int l=co[i];
                for(int k=0;k<l&&co[pri.get(i)]>0;k++){
                    co[i]--;
                    co[pri.get(i)]--;
                    ans.add(i);
                }
            }
        }
        
        
       
        for(int i:ans)w.print(i+" ");
        w.println();
    	w.close();
    }
}