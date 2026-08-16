import java.io.*;
import java.util.*;
import java.math.*;
     
public class Main{
	public static void main(String[] args) throws Exception {
	IO io = new IO();
	PrintWriter out = new PrintWriter(System.out);
	Solver sr = new Solver();
	sr.solve(io,out);
	out.flush();
	out.close();
    	}

	static class Solver
	{
	    void solve(IO io, PrintWriter out)
	    {
	        int i, j;
           int t = io.nextInt();
           while(t-->0)
           {
               int n = io.nextInt();
               int[] ar = new int[n];
               for(i=0 ; i<ar.length ; i++)
                    ar[i]=io.nextInt();
               long sum=0;
               boolean flag=false;
               for(i=0 ; i<ar.length ; i++)
	            {
	                sum+=ar[i];
	                if(sum<=0)
	                    flag=true;
	            }
	            sum=0;
               for(i=ar.length-1 ; i>=0 ; i--)
	            {
	                sum+=ar[i];
	                if(sum<=0)
	                    flag=true;
	            }
               if(flag)
                    out.println("No");
                else
                    out.println("Yes");
           }
	    }
	}
	//Special thanks to Petr (on codeforces) who inspired me to implement IO class!
	static class IO
	{
    	BufferedReader reader;
        StringTokenizer tokenizer;
    	public IO() {
                reader = new BufferedReader(new InputStreamReader(System.in));
                tokenizer = null;
            }
     
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
        public String nextLine() {
            String s="";
            try {
                    s=reader.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            return s;
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
    
        public long nextLong() {
            return Long.parseLong(next());
        }
    	double nextDouble()
    	{
    		return Double.parseDouble(next());
    	}
	}
}