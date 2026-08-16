import java.io.IOException;
import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;

class Solve{
	final Scanner in = new Scanner(System.in);
	
	static final double INF = 1e9;
	int n;
	boolean solve(){
		n = in.nextInt();
		if(n == 0) return false;
		int[] r = new int[n];
		int[] w = new int[n];
		Book[] b = new Book[n];
		int all = 0;
		for(int i=0; i<n; i++){
			r[i] = in.nextInt();
			w[i] = in.nextInt();
			all += r[i]+w[i];
			b[i] = new Book(r[i], w[i]);
		}
		Arrays.sort(b);
		int wsum = 0;
		for(int i=1; i<n; i++){
			wsum += b[i].r;
		}
		int sp = b[0].r - wsum;
		if(sp <= 0){
			System.out.println(all);
			return true;
		}
		int[] nw = new int[n-1];
		wsum = 0;
		for(int i=1; i<n; i++){
			nw[i-1] = b[i].w;
			wsum += b[i].w;
		}
		if(wsum <= sp){
			System.out.println(all+(sp-wsum));
			return true;
		}
		Arrays.sort(nw);
		n--;
		res = 0;
		int[] ww = new int[n];
		for(int i=0; i<n; i++) ww[i] = nw[n-1-i];
		dfs(0, 0, sp, ww, new BitSet(n));
		System.out.println(all+(sp-res));
		return true;
	}
	
	int res = 0;
	boolean dfs(int sum, int st, int sp, int[] w, BitSet used){
		if(sum == sp){
			res = sum;
			return true;
		}
		if(sum > sp) return false;
		if(sum > res) res = sum;
		for(int i=used.nextClearBit(st); i<n && sum+w[i]*(n-i)>res; i=used.nextClearBit(i+1)){
			used.set(i);
			if(dfs(sum+w[i], i+1, sp, w, used)) return true;
			used.clear(i);
		}
		return false;
	}
	
}

class Book implements Comparable<Book>{
	int r, w;
	Book(int r, int w){
		this.r = r;
		this.w = w;
	}
	@Override
	public int compareTo(Book o) {
		return o.r-r;
	}
}


public class Main{
	public static void main(String[] args) throws IOException{
		Solve solve = new Solve();
		while(solve.solve());
	}
}