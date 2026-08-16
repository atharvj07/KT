import java.io.*;
import java.util.*;
import java.text.*;
import java.lang.*;
import java.math.BigInteger;
import java.util.regex.*;

public class Myclass {
	static ArrayList a[]=new ArrayList[3000001];
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        
        InputReader in = new InputReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int n=in.nextInt();
        int m=in.nextInt();
        Vector<pair>edge=new Vector<>();
        Vector<pair>req=new Vector<>();
        for(int i=0;i<m;i++) {
        	int x=in.nextInt();
        	int y=in.nextInt();
        	edge.add(new pair(x,y));
        }
        int a=in.nextInt();
        int b=in.nextInt();
        int d_a=in.nextInt();
        int d_b=in.nextInt();
        dsu d=new dsu(n);
        Vector<pair>ans=new Vector<>();
        for(int i=0;i<m;i++) {
        	pair p=edge.get(i);
        	int x=p.x;
        	int y=p.y;
        	if(x!=a && x!=b && y!=a && y!=b) {
        		if(!d.find(x, y))
        		{
        			ans.add(p);
        			d.union(x, y);
        		}
        	}
        	else
        	{
        		req.add(p);
        	}
        }
        boolean chk=false;
        int got[]=new int[m+1];
        boolean  freq[][]=new boolean [n+1][2];
        for(int i=0;i<req.size();i++) {
        	pair p=req.get(i);
        	int x=p.x;
        	int y=p.y;
        	if(!p.equals(new pair(a,b)) && !p.equals(new pair(b,a))) {
        		if(x==a || y==a) {
        			int root=d.root(y);
        			got[i]=root;
        			freq[root][0]=true;
        		}
        		else
        		{
        			int root=d.root(y);
        			got[i]=root;
        			freq[root][1]=true;
        		}
        	}
        	else
        	{
        		chk=true;
        	}
        }
        for(int i=0;i<req.size();i++) {
        	pair p=req.get(i);
        	int x=p.x;
        	int y=p.y;
        	if(!p.equals(new pair(a,b)) && !p.equals(new pair(b,a))) {
        		int root=got[i];
        		
        		if(freq[root][0] && freq[root][1])
        			continue;
        		if(x==a || y==a) {
        			if(!d.find(x,y) && d_a>0) {
        				ans.add(p);
        				d.union(x, y);
        				d_a--;
        			}
        		}
        		else
        		{
        			if(!d.find(x,y) && d_b>0) {
        				ans.add(p);
        				d.union(x, y);
        				d_b--;
        			}
        		}
        	}
        }
        for(int i=0;i<req.size();i++) {
        	pair p=req.get(i);
        	int x=p.x;
        	int y=p.y;
        	if(!p.equals(new pair(a,b)) && !p.equals(new pair(b,a))) {
        		if(x==a || y==a) {
        			if(!d.find(x,y) && d_a>0) {
        				ans.add(p);
        				d.union(x, y);
        				d_a--;
        			}
        		}
        		else
        		{
        			if(!d.find(x,y) && d_b>0) {
        				ans.add(p);
        				d.union(x, y);
        				d_b--;
        			}
        		}
        	}
        }
        if(chk && d_a>0 && d_b>0) {
        	if(!d.find(a, b)) {
        		d.union(a, b);
        		ans.add(new pair(a,b));
        	}
        }
        if(ans.size()==n-1) {
        	pw.println("Yes");
        	for(int i=0;i<n-1;i++) {
        		pw.println(ans.get(i));
        	}
        }
        else
        	pw.println("No");
        pw.flush();
        pw.close();
        
        
    }
    private static void debug(Object... o) {
            System.out.println(Arrays.deepToString(o));
        }
        
        static class InputReader 
        {
        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream) 
        {
            this.stream = stream;
        }
        public int snext() 
        {
            if (snumChars == -1)
                throw new InputMismatchException();
            if (curChar >= snumChars) 
            {
                curChar = 0;
                try 
                {
                    snumChars = stream.read(buf);
                } 
                catch (IOException e) 
                {
                    throw new InputMismatchException();
                }
                if (snumChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int nextInt() 
        {
            int c = snext();
            while (isSpaceChar(c)) 
            {
                c = snext();
            }
            int sgn = 1;
            if (c == '-')
            {
                sgn = -1;
                c = snext();
            }
            int res = 0;
            do 
            {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public long nextLong()
        {
            int c = snext();
            while (isSpaceChar(c)) 
            {
                c = snext();
            }
            int sgn = 1;
            if (c == '-') 
            {
                sgn = -1;
                c = snext();
            }
            long res = 0;
            do 
            {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public int[] nextIntArray(int n) 
        {
            int a[] = new int[n];
            for (int i = 0; i < n; i++) 
            {
                a[i] = nextInt();
            }
            return a;
        }

        public String readString()
        {
            int c = snext();
            while (isSpaceChar(c)) 
            {
                c = snext();
            }
            StringBuilder res = new StringBuilder();
            do 
            {
                res.appendCodePoint(c);
                c = snext();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public String nextLine() 
        {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            StringBuilder res = new StringBuilder();
            do 
            {
                res.appendCodePoint(c);
                c = snext();
            } while (!isEndOfLine(c));
            return res.toString();
        }

        public boolean isSpaceChar(int c) 
        {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c) 
        {
            return c == '\n' || c == '\r' || c == -1;
        }

        public interface SpaceCharFilter
        {
            public boolean isSpaceChar(int ch);
        }
    }
        public static long mod = 1000000009;
        public static int d;
        public static int p;
        public static int q;
        
        public static long[] suffle(long[] a,Random gen)
        {
            int n = a.length;
            for(int i=0;i<n;i++)
            {
                int ind = gen.nextInt(n-i)+i;
                long temp = a[ind];
                a[ind] = a[i];
                a[i] = temp;
            }
            return a;
        }
        
        public static void swap(int a, int b){
            int temp = a;
            a = b;
            b = temp;
        }
        
        public static HashSet<Integer> primeFactorization(int n)
        {
            HashSet<Integer> a =new HashSet<Integer>();
            for(int i=2;i*i<=n;i++)
            {
                while(n%i==0)
                {
                    a.add(i);
                    n/=i;
                }
            }
            if(n!=1)
                a.add(n);
            return a;
        }
        
        public static void sieve(boolean[] isPrime,int n)
        {
            for(int i=1;i<n;i++)
                isPrime[i] = true;
            
            isPrime[0] = false;
            isPrime[1] = false;
            
            for(int i=2;i*i<n;i++)
            {
                if(isPrime[i] == true)
                {
                    for(int j=(2*i);j<n;j+=i)
                        isPrime[j] = false;
                }
            }
        }
        
        public static long GCD(long gcd,long diff)
        {
            if(diff==0)
                return gcd;
            else
                return GCD(diff,gcd%diff);
        }
        
        static class pair implements Comparable<pair>
        {
            Integer x;
            Integer y;
            pair(int a,int a2)
            {
                this.x=a;
                this.y=a2;
            }
            

            public int compareTo(pair o) {
                int result = x.compareTo(o.x);
                if(result==0)
                    result = y.compareTo(o.y);
                
                return result;
            }  
            
            public String toString()
            {
                return x+" "+y;
            }
            
            public boolean equals(Object o)
            {
                if (o instanceof pair)
                {
                    pair p = (pair)o;
                    return p.x == x && p.y == y ;
                }
                return false;
            }
            
            public int hashCode()
            {
                return new Long(x).hashCode()*31 + new Long(y).hashCode();
            }
        }
       
        public static long binaryExponentiation(long x,long n)
        {
            long result=1;
            while(n>0)
            {
                if(n % 2 ==1)
                    result=result * x;
                x=x*x;
                n=n/2;
            }
            return result;
        }

        public static int modularExponentiation(int x,int n,int M)
        {
            int result=1;
            while(n>0)
            {
                if(n % 2 ==1)
                    result=(result * x)%M;
                x=(x*x)%M;
                n=n/2;
            }
            return result;
        }

        public static long modularExponentiation(long x,long n,long M)
        {
            long result=1;
            while(n>0)
            {
                if(n % 2 ==1)
                    result=(result * x)%M;
                x=(x*x)%M;
                n=n/2;
            }
            return result;
        }

        public static int modInverse(int A,int M)
        {
            return modularExponentiation(A,M-2,M);
        }

        public static long modInverse(long A,long M)
        {
            return modularExponentiation(A,M-2,M);
        }
    
}
class dsu{
	int parent[];
	ArrayList a[];
	dsu(int n){
		parent=new int[n+1];
		a=new ArrayList[n+1];
		for(int i=0;i<=n;i++)
		{
			parent[i]=i;
		}
	}
	int root(int n) {
		while(parent[n]!=n)
		{ 
			parent[n]=parent[parent[n]];
			n=parent[n];
		}
		return n;
	}
	void union(int _a,int _b) {
		int p_a=root(_a);
		int p_b=root(_b);
		parent[p_a]=p_b;
	}
	boolean find(int a,int b) {
		if(root(a)==root(b))
			return true;
		else
			return  false;
	}
	int size(int n) {
		return (a[n].size());
	}
	
}
