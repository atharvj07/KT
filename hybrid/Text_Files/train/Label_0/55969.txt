import java.util.*;
import java.io.*;

public class Main {
	static final int M = 1000000007;
		static FastReader in = new FastReader();
		static PrintWriter out = new PrintWriter(System.out);
//		static Scanner in = new Scanner(System.in);
//        File file = new File("input.txt");
//        Scanner in = new Scanner(file);
//        PrintWriter out = new PrintWriter(new FileWriter("output.txt"));
    public static void main(String[] args) {
    	
//    	int t = in.nextInt();
//    	while(t-- > 0){
    	 String str = in.next();
    	 out.println(3);
    	 out.println("R "+(str.length()-1));
    	 out.println("L "+str.length());
    	 out.println("L 2");
    	  
//    	}
    	out.close(); 
    }    	
    
   
    static int gcd(int a, int b) {
    	if(b==0) return a;
    	return gcd(b, a%b);
    }
    
	static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}