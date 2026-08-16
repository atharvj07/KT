import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.*;
import java.util.*;
import java.util.LinkedList;
import java.math.*;
import java.lang.*;
import java.util.PriorityQueue;
import static java.lang.Math.*;
@SuppressWarnings("unchecked")
public class Solution implements Runnable {
    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;
        private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        public InputReader(InputStream stream) {
            this.stream = stream;
        }
        
        public int read() {
            if (numChars==-1) 
                throw new InputMismatchException();
            
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                }
                catch (IOException e) {
                    throw new InputMismatchException();
                }
                
                if(numChars <= 0)               
                    return -1;
            }
            return buf[curChar++];
        }
     
        public String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
        public int nextInt() {
            int c = read();
            
            while(isSpaceChar(c)) 
                c = read();
            
            int sgn = 1;
            
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            
            int res = 0;
            do {
                if(c<'0'||c>'9') 
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c)); 
            
            return res * sgn;
        }
        
        public long nextLong() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c));
                return res * sgn;
        }
        
        public double nextDouble() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            double res = 0;
            while (!isSpaceChar(c) && c != '.') {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, nextInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            if (c == '.') {
                c = read();
                double m = 1;
                while (!isSpaceChar(c)) {
                    if (c == 'e' || c == 'E')
                        return res * Math.pow(10, nextInt());
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    m /= 10;
                    res += (c - '0') * m;
                    c = read();
                }
            }
            return res * sgn;
        }
        
        public String readString() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } 
            while (!isSpaceChar(c));
            
            return res.toString();
        }
     
        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
     
        public String next() {
            return readString();
        }
        
        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
    public static int min(int a,int b)
    {
        if(a>b)
        {
            return b;
        }
        return a;
    }
    public static int max(int a,int b)
    {
        if(a>b)
        {
            return a;
        }
        return b;
    }
    static int mod = (int)1e9+7;
    static class pair implements Comparable<pair>
    {
        long x;
        int y;
        pair(long x,int y)
        {
            this.x = x;
            this.y = y;
        }
        public int compareTo(pair p)
        {
            if(this.x>p.x)
            {
                return 1;
            }
            else if(this.x<p.x)
            {
                return -1;
            }
            else
            {
                return this.y-p.y;
            }
        }
    }
    public static long gcd(long a,long b)
    {
        while(b!=0)
        {
            long save = a%b;
            a = b;
            b = save;
        }    
        return a;
    }
    public static void main(String args[]) throws Exception {
        new Thread(null, new Solution(),"Main",1<<26).start();
    }
    public void run() {
        InputReader sc  = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int t1 = 1;
		while(t1-->0)    
        {
           int n = sc.nextInt();
		   int m = sc.nextInt();
		   for(int i=0;i<n;i++)
		   {
			   String s = sc.readString();
			   for(int j=0;j<m;j++)
			   {
				   if(s.charAt(j)=='B')
				   {
					   int k = j+1;
					   for(;k<m;k++)
					   {
						   if(s.charAt(k)=='W')
						   {
							   break;
						   }
					   }
					   int len = k-j;
					   out.println((i+len/2+1)+" "+(j+len/2+1));
					   out.close();
					   return;
				   }
			   }
		   }
		}
		out.close();
   }
}
