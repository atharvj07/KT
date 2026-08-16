import java.util.*;
import java.io.*;

public class c{

	static long[][] inv;

	public static void main(String[] args){
		JS scan = new JS();
		int n = scan.nextInt();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for(int i = 0; i < n; i++){
			arr.add(scan.nextInt());
		}
		inv = new long[2][31];
		solve(arr, 30);
		long ans = 0;
		long xor = 0;
		for(int i = 0; i < 31; i++){
			if(inv[1][i] < inv[0][i]){
				ans += inv[1][i];
				xor |= (1 << i);
			}
			else ans += inv[0][i];
		}
		System.out.println(ans+" "+xor);
	}
	
	static void solve(ArrayList<Integer> arr, int bit){
		if(arr.size() == 0) return;
		if(bit == -1) return;
		// System.out.println(bit);
		long o = 0;
		long invNorm = 0;
		long z = 0;
		long invFlip = 0;

		ArrayList<Integer> zoinks = new ArrayList<Integer>();
		ArrayList<Integer> oinks = new ArrayList<Integer>();
		for(int i = 0; i < arr.size(); i++){
			if((arr.get(i) & (1 << bit)) == 0){
				z ++;
				invNorm += o;
				zoinks.add(arr.get(i));
			}
			else{
				o ++;
				invFlip += z;
				oinks.add(arr.get(i));
			}
		}

		inv[0][bit] += invNorm;
		inv[1][bit] += invFlip;

		solve(oinks, bit-1);
		solve(zoinks, bit-1);
	}

	static class Pair{

		int a;
		int b;
		int x;

		public Pair(int aa, int bb, int xx){
			a = aa;
			b = bb;
			x = xx;
		}
	}

	static class JS{
		public int BS = 1<<16;
		public char NC = (char)0;
		byte[] buf = new byte[BS];
		int bId = 0, size = 0;
		char c = NC;
		double num = 1;
		BufferedInputStream in;
	
		public JS() {
			in = new BufferedInputStream(System.in, BS);
		}
	
		public JS(String s) throws FileNotFoundException {
			in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
		}
	
		public char nextChar(){
			while(bId==size) {
				try {
					size = in.read(buf);
				}catch(Exception e) {
					return NC;
				}				
				if(size==-1)return NC;
				bId=0;
			}
			return (char)buf[bId++];
		}
	
		public int nextInt() {
			return (int)nextLong();
		}
	
		public long nextLong() {
			num=1;
			boolean neg = false;
			if(c==NC)c=nextChar();
			for(;(c<'0' || c>'9'); c = nextChar()) {
				if(c=='-')neg=true;
			}
			long res = 0;
			for(; c>='0' && c <='9'; c=nextChar()) {
				res = (res<<3)+(res<<1)+c-'0';
				num*=10;
			}
			return neg?-res:res;
		}
	
		public double nextDouble() {
			double cur = nextLong();
			return c!='.' ? cur:cur+nextLong()/num;
		}
	
		public String next() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c>32) {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}
	
		public String nextLine() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c!='\n') {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}
	
		public boolean hasNext() {
			if(c>32)return true;
			while(true) {
				c=nextChar();
				if(c==NC)return false;
				else if(c>32)return true;
			}
		}
	}
}