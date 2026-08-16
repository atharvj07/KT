

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.awt.Point;

 
public class TryB
{
    
    static class InputReader {
 
		private final InputStream stream;
		private final byte[] buf = new byte[8192];
		private int curChar, snumChars;
 
		public InputReader(InputStream st) {
			this.stream = st;
		}
 
		public int read() {
			if (snumChars == -1)
	 			throw new InputMismatchException();
			if (curChar >= snumChars) {
				curChar = 0;
				try {
					snumChars = stream.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (snumChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}
 
		public int ni() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}
 
		public long nl() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return res * sgn;
		}
 
		public int[] nia(int n) {
			int a[] = new int[n];
			for (int i = 0; i < n; i++) {
				a[i] = ni();
			}
			return a;
		}
 
		public String rs() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}
 
		public String nextLine() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndOfLine(c));
			return res.toString();
		}
 
		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
 
		private boolean isEndOfLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
 
	}
	

	
	
	
   
		static PrintWriter w = new PrintWriter(System.out);
 static char [][]sol;
    public static void main(String[] args)
    {
        
        InputReader sc = new InputReader(System.in);
        //PrintWriter w = new PrintWriter(System.out);
    
       /* 
        prime  = new boolean[n + 1];
		sieve();
		prime[1] = false;
		*/
		/*
		as = new ArrayList<>();
		for(int i=2;i<=1000000;i++)
		{
		    if(prime[i])
		    as.add(i);
		}
		*/
		
       /* 
		
	long a = sc.nl();
	 
            BigInteger ans = new BigInteger("1");
            for (long i = 1; i < Math.sqrt(a); i++) {
                if (a % i == 0) {
                    if (a / i == i) {
                        ans = ans.multiply(BigInteger.valueOf(phi(i)));
                        
                    } else {
                        ans = ans.multiply(BigInteger.valueOf(phi(i)));
                        ans = ans.multiply(BigInteger.valueOf(phi(a / i)));
 
                        
                    }
 
 
                }
            }
            w.println(ans.mod(bigInteger));
            */
          
         // MergeSort ob = new MergeSort();
       // ob.sort(arr, 0, arr.length-1);
       
    // Student []st = new Student[x];    
   // st[i] = new Student(i,d[i]);
     //Arrays.sort(st,(p,q)->p.diff-q.diff);
  
     

  int x = sc.ni();
  int temp = 0;
  int maxy = 0;
  int maxx = 0;
  for(int i=0;i<x;i++)
  {
      int p = sc.ni();
      int q = sc.ni();
      temp = Math.max(temp, p+q);
  }
 w.println(temp);

   
   
     w.close();
        
  
    
    }
    static boolean checkT(int a,int b, int c)
    {
        int f = 0;
        if(a+b <= c || b+c <=a||a+c <= b)
            return false;
        else
            return true;
    }
    static double costheta(int a,int b,int c)
    {
        double pos = ((double)b*(double)b + (double)c*(double)c-(double)a*(double)a) / (2*(double)b*(double)c);
         return pos;
    }
     public static int ip(String s){
		return Integer.parseInt(s);
	}
	 public static String ips(int s){
		return Integer.toString(s);
	}
         static long area(int ax,int ay,int bx,int by,int cx,int cy)
         {
             long ar = ((long)ax*((long)by-(long)cy)) + ((long)bx*((long)cy-(long)ay)) + ((long)cx*((long)ay-(long)by));
             return Math.abs(ar);
         }
         public static int lowerBound(Student[] array, int length, int value) {
        int low = 0;
        int high = length-1;
        while (low < high) {
            final int mid = (low + high) / 2;
            if (value <= array[mid].val) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
  }
  public static int upperBound(int[] array, int length, int value) {
        int low = 0;
        int high = length-1;
        while (low < high) {
            final int mid = (low + high) / 2;
            if (value >= array[mid]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
   static class Student
    {
        
        int val;
        int index;
        Student(int val,int index)
        {
            this.val = val;
            this.index = index;
            
            
        }
        
    }
}