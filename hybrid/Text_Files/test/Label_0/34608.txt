//package clipse;


import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;
import java.io.*;
import java.math.*;




public class AA
{
	
	static StringBuilder sb;
	static dsu dsu;
	static long fact[];
	static long mod=(long)(1e9+7);
	static long sum=(mod+mod+2);
	static long A[];
	static long B[];
	static long ans[];
	static int n;
	static int m;
	
	
	
	
	
	static void solve()
    {
		
		int n=i();
		int x0=i();
		pair A[]=new pair[n];
		for(int i=0;i<n;i++)
		{
			int x=i();
			int y=i();
			if(y<x)
			A[i]=new pair(y,x);
			else
				A[i]=new pair(x,y);
			
		}
		int min=Integer.MAX_VALUE;
		for(int p=0;p<=1000;p++)
		{
			boolean flag=true;
			for(int i=0;i<n;i++)
			{
				if(A[i].x<=p&&A[i].y>=p)
				{
					
				}
				else
					flag=false;
				
			}
			if(flag)
			{
				min=Math.min(min,Math.abs(p-x0));
			}
			
			
		}
	if(min==Integer.MAX_VALUE)
		min=-1;
		
		
	System.out.println(min);
	
	
	
		
		
    }
		
		
		
    
	
	
	
	
	 public static void main(String[] args)
	 {
	         sb=new StringBuilder();
	         
	      /*   fact=new long[(int)1e6+1];
	         fact[0]=fact[1]=1;
	         for(int i=2;i<fact.length;i++)
	         {
	        	fact[i]=((long)(i%mod)*1L*(long)(fact[i-1]%mod))%mod; 
	         }
	        */
	         
	        int test=1;
	        while(test-->0) 
	        {
	        	
	    		
	        	 solve();
	        }
	        
	         System.out.println(sb);
	         
	 }
	 
//*******************************************NCR%P*******************************************************	 
	 static long ncr(int n, int r)
	 {
		 if(r>n)
			 return (long)0;
		 
		 long res=fact[n]%mod;
		 //System.out.println(res);
		 res=((long)(res%mod)*(long)(p(fact[r],mod-2)%mod))%mod;
		 res=((long)(res%mod)*(long)(p(fact[n-r],mod-2)%mod))%mod;
		 //System.out.println(res);
		 return res;
		
		 
	 }
		static long p(long x, long y)//POWER FXN //
		{
			if(y==0)
				return 1;
			
			long res=1;
			while(y>0)
			{
				if(y%2==1)
				{
					res=(res*x)%mod;
					y--;
				}
				
				x=(x*x)%mod;
				y=y/2;
				
				
			}
			return res;
		}
		

//*******************************************END*******************************************************
	 
	 
	 
	 
	 
	 //*********************************Disjoint set union*************************//
	 static class dsu
	 {
		 int parent[];
		 dsu(int n)
		 {
			 parent=new int[n];
			 for(int i=0;i<n;i++)
				 parent[i]=-1;
		 }
		 int find(int a)
		 {
			 if(parent[a]<0)
				 return a;
			 else
			 {
				 int x=find(parent[a]);
				 parent[a]=x;
				 return x;
			 }
		 }
		 void merge(int a,int b)
		 {
			 a=find(a);
			 b=find(b);
			 if(a==b)
				 return;
			 parent[b]=a;
		 }
	 }
	 
	 
	 
//*******************************************PRIME FACTORIZE *****************************************************************************************************//
	 static TreeMap<Integer,Integer> prime(long n)
	 {
		 TreeMap<Integer,Integer>h=new TreeMap<>();
		 long num=n;
		 for(int i=2;i<=Math.sqrt(num);i++)
		 {
			 if(n%i==0)
			 {
				 int nt=0;
				 while(n%i==0) {
					 n=n/i;
					 nt++;
				 }
				 h.put(i, nt);
			 }
		 }
		 if(n!=1)
			 h.put((int)n, 1);
		 return h;
		 
	 }
	 
	
	
//*************CLASS PAIR ***********************************************************************************************************************************************
	    static class pair implements Comparable<pair>
	    {
	        int x;
	        int y;

	        pair(int x, int y) {
	            this.x = x;
	            this.y = y;
	        }
	        public int compareTo(pair o)
	        {
	        	return y-o.y;
	        	
	        }
			
	       
	    }
//*************CLASS PAIR *****************************************************************************************************************************************************
	
	
	

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int Int() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String String() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public String next() {
            return String();
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0)
                    writer.print(' ');
                writer.print(objects[i]);
            }
        }

        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

        public void flush() {
            writer.flush();
        }
    }

    static InputReader in = new InputReader(System.in);
    static OutputWriter out = new OutputWriter(System.out);
   

    public static int[] sort(int[] a) {
        int n = a.length;
        ArrayList<Integer> l = new ArrayList<>();
        for (int i : a)
            l.add(i);
        Collections.sort(l);
        for (int i = 0; i < l.size(); i++)
            a[i] = l.get(i);
        return a;
    }

    public static long pow(long x, long y) {
        long res = 1;
        while (y > 0) {
            if (y % 2 != 0) {
                res = (res * x);// % modulus;
                y--;

            }
            x = (x * x);// % modulus;
            y = y / 2;
        }
        return res;
    }
//GCD___+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    public static long gcd(long x, long y) {
        if (x == 0)
            return y;
        else
            return gcd(y % x, x);
    }
    //****************LOWEST COMMON MULTIPLE   *************************************************************************************************************************************

    public static long lcm(long x, long y) {
        return (x * (y / gcd(x, y)));
    }
//INPUT PATTERN******************************************************************************************************************************************************************
    public static int i() {
        return in.Int();
    }

    public static long l() {
        String s = in.String();
        return Long.parseLong(s);
    }

    public static String s() {
        return in.String();
    }

    public static int[] readArray(int n) {
        int A[] = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = i();
        }
        return A;
    }

    public static long[] readArray(long n) {
        long A[] = new long[(int) n];
        for (int i = 0; i < n; i++) {
            A[i] = l();
        }
        return A;
    }

}






	