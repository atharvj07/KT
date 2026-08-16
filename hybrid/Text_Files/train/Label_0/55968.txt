import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;
import java.util.StringTokenizer;


public class E {	
	BufferedReader reader;
    StringTokenizer tokenizer;
    PrintWriter out;
    
    public void shuffleArray(int[] arr) {
        Random rnd = new Random();
        for (int i = arr.length - 1; i >= 0; i--) {
            int pos = rnd.nextInt(i + 1);
            int temp = arr[i];
            arr[i] = arr[pos];
            arr[pos] = temp;
        }
    }
    
	public void solve() throws IOException {				
		int N = nextInt();
		int[][] s = new int[N][];
		for(int i = 0; i < N; i++)
			s[i] = new int[]{i, nextInt()};
		
		Arrays.sort(s, new Comparator<int[]>(){
			public int compare(int[] arg0, int[] arg1) {
				return arg0[1] < arg1[1]? -1: 1;
			}			
		});
						
		int[] a = new int[N];
		int[] b = new int[N];
		
		for(int i = 0; i < N/3; i++){
			a[i] = i; 
			b[i] = s[i][1] - a[i];
		}
		for(int i = N/3; i < 2*N/3; i++){
			b[i] = i; 
			a[i] = s[i][1] - b[i];
		}
		for(int i = 2*N/3; i < N; i++){
			b[i] = (N-1) - i; 
			a[i] = s[i][1] - b[i];
		}
		
//		for(int i = 0; i < N; i++){
//			out.println( s[i][1] + ": " + a[i] + ", " + b[i]);
//		}
				
		out.println("YES");			
		int[] finala = new int[N];
		int[] finalb = new int[N];
		for(int i = 0; i < N; i++){
			finala[ s[i][0] ] = a[ i ];
			finalb[ s[i][0] ] = b[ i ];
		}
		
		for(int i = 0; i < N; i++)
			out.print(finala[i] + " ");
		out.println();
		for(int i = 0; i < N; i++)
			out.print(finalb[i] + " ");
		out.println();					
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		new E().run();
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
