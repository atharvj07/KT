import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;


public class ProblemB {

public static void main(String[] args) throws IOException {
		
		ProblemB solver = new ProblemB();
		solver.init();
		solver.solve();
	}
	
	private void init() {
		
	}

	private void solve() throws IOException {
		 
		Reader in = new Reader(System.in);
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		
		int n = in.nextInt();
		int x = in.nextInt();
		int y = in.nextInt();
		int c = in.nextInt();
		
		long lo = 0;
		long hi = 2 * n;
		
		while (lo < hi) {
			long mid = (lo + hi)/2;
			long r = count(n, x , y, mid);
			if (r < c) {
				lo = mid + 1;
			} else {
				hi = mid;;
			}
		}
		out.println(lo);
		out.flush();
		out.close();
	}
	
	private long count(int n, int x, int y, long steps) {
		long r = 1  + 2 * steps * (1 + steps);
		r -= countWall(x - 1 - steps);
		r -= countWall(y - 1 - steps);
		r -= countWall(n - (x + steps));
		r -= countWall(n - (y + steps));
		r += countCorner(steps - (x - 1) - (y - 1) - 1);
		r += countCorner(steps - (y - 1) - (n - x) - 1);
		r += countCorner(steps - (n - x) - (n - y) - 1);
		r += countCorner(steps - (x - 1) - (n - y) - 1);
		
		return r;
	}

	private long countCorner(long x) {
		if (x <= 0) return 0;
		return x * ( x + 1) / 2;
	}

	private long countWall(long x) {
		if (x >= 0) return 0;
		return x * x;
	}

	private static class Reader {
	    BufferedReader reader;
	    StringTokenizer tokenizer;

	    /** call this method to initialize reader for InputStream */
	    Reader(InputStream input) {
	        reader = new BufferedReader(
	                     new InputStreamReader(input) );
	        tokenizer = new StringTokenizer("");
	    }

	    /** get next word */
	    public String next() throws IOException {
	        while ( ! tokenizer.hasMoreTokens() ) {
	            //TODO add check for eof if necessary
	            tokenizer = new StringTokenizer(
	                   reader.readLine() );
	        }
	        return tokenizer.nextToken();
	    }

	    public int nextInt() throws IOException {
	        return Integer.parseInt( next() );
	    }
	    
	    public double nextDouble() throws IOException {
	        return Double.parseDouble( next() );
	    }
	    
	    public long nextLong() throws IOException {
	    	return Long.parseLong(next());
	    }
	}

}
