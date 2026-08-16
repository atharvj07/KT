import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;


public class D {	
	BufferedReader reader;
    StringTokenizer tokenizer;
    PrintWriter out;
    
    long MODULAR = 1000000009;
    
	public void solve() throws IOException {				
		int N = nextInt();
		int H = nextInt();
		long[][][][] dp = new long[2][H][H][H];
		dp[1][0][0][0] = 4;
		for(int i = 1; i < N; i++){
			long[][][][] old = dp.clone();
			dp = new long[2][H+1][H+1][H+1];
			for(int h1 = 0; h1 < H; h1++){
				for(int h2 = 0; h2 < H; h2++){
					for(int h3 = 0; h3 < H; h3++){
						for(int alive = 0; alive <= 1; alive++){
							long add = old[alive][h1][h2][h3] % MODULAR;		
							
							int newh1 = (h1 == 0 || h1 == H-1)? 0: h1+1;
							int newh2 = (h2 == 0 || h2 == H-1)? 0: h2+1;
							int newh3 = (h3 == 0 || h3 == H-1)? 0: h3+1;
							int alive1 = (h1 > 0 || i < H)? 1: 0;		
							int alive2 = (h2 > 0 || i < H)? 1: 0;
							int alive3 = (h3 > 0 || i < H)? 1: 0;
							
							dp[alive][newh1][newh2][newh3] += add; 
							dp[alive1][alive][newh2][newh3] += add;
							dp[alive2][newh1][alive][newh3] += add;
							dp[alive3][newh1][newh2][alive] += add;
						}						
					}
				}
			}
		}
		
		long ans = 0;
		for(int h1 = 0; h1 < H; h1++){
			for(int h2 = 0; h2 < H; h2++){
				for(int h3 = 0; h3 < H; h3++){
					ans = (ans + dp[1][h1][h2][h3]) % MODULAR;
					if( h1 > 0 || h2 > 0 || h3 > 0){
						ans = ( ans + dp[0][h1][h2][h3]) % MODULAR;
					}
				}
			}
		}
		out.println( ans );
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		new D().run();
	}
	
	public void run() {
        try {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
            out = new PrintWriter(System.out);
            solve();
            reader.close();
            out.close();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    String nextToken() throws IOException {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }
        return tokenizer.nextToken();
    }

}
