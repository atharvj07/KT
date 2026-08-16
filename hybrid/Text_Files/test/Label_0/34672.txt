/*
     * Code Author: Akshay Miterani
     * DA-IICT
     */
    import java.io.*;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.*;
     
     
    public class MainC {
     
    	static double eps=(double)1e-6;
    	static long mod=(int)1e9+7;
    	public static void main(String args[]){
    		InputReader in = new InputReader(System.in);
    		OutputStream outputStream = System.out;
    		PrintWriter out = new PrintWriter(outputStream);
    		//----------My Code----------
    		int n=in.nextInt();
    		int m=in.nextInt();
    		int k=in.nextInt();
    		LinkedList<Integer> a=new LinkedList<Integer>();
    		for(int i=0;i<k;i++){
    			a.add(in.nextInt());
    		}
    		long ans=0;
    		for(int cus=0;cus<n;cus++){
    			for(int pro=0;pro<m;pro++){
    				int x=in.nextInt();
    				int ind=a.indexOf(x);
    				a.remove(ind);
    				ans+=ind+1;
    				a.addFirst(x);
    			}
    		}
    		out.println(ans);
    		out.close();
    		//---------------The End------------------
    		
    	}

    	
    	static long modulo(long a,long b,long c) {
    	    long x=1;
    	    	    long y=a;
    	    	    while(b > 0){
    	    	        if(b%2 == 1){
    	    	            x=(x*y)%c;
    	    	        }
    	    	        y = (y*y)%c; // squaring the base
    	    	        b /= 2;
    	    	    }
    	    	    return  x%c;
    	    	}
    	static long gcd(long x, long y)
        {
            long r=0, a, b;
            a = (x > y) ? x : y; // a is greater number
            b = (x < y) ? x : y; // b is smaller number
            r = b;
            while(a % b != 0)
            {
                r = a % b;
                a = b;
                b = r;
            }
            return r;
        }
    	static class Pair implements Comparable<Pair>{
    		long x;
    		long y;
    		int i;
    		Pair(long xx,long yy){
    			x=xx;
    			y=yy;
    		}
    		@Override
    		public int compareTo(Pair o) {
    			if(this.y>=o.y)
    				return 1;
    			else
    				return 0;
					
    		}
    	}
    	
    	static class InputReader {
    	    public BufferedReader reader;
    	    public StringTokenizer tokenizer;
     
    	    public InputReader(InputStream inputstream) {
    	      reader = new BufferedReader(new InputStreamReader(inputstream));
    	      tokenizer = null;
    	    }
    	    
    	    public String nextLine(){
    	    	String fullLine=null;
    	    	while (tokenizer == null || !tokenizer.hasMoreTokens()) {
    	            try {
    	              fullLine=reader.readLine();
    	            } catch (IOException e) {
    	              throw new RuntimeException(e);
    	            }
    	            return fullLine;
    	          }
    	          return fullLine;
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
    		public long nextLong() {
    		      return Long.parseLong(next());
    		    }
    	    public int nextInt() {
    	      return Integer.parseInt(next());
    	    }
    	  }
    } 