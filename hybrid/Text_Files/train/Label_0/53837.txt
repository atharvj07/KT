
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.*;


public class Fourth{
	static long mod=1000000007;
	
    public static void main(String[] args) throws Exception{           	
    	 InputReader in = new InputReader(System.in);       
    	PrintWriter pw=new PrintWriter(System.out);   
    	
    	//int t=in.readInt();
        //	while(t-->0)
        	//{
        	int n=in.readInt();
    	//long n=in.readLong();
        	int c1=0;
    	long a[]=new long[n];
    	HashMap<Long,Integer>hm=new HashMap<Long,Integer>();
    	HashSet<Pair>hs=new HashSet<Pair>();
    	long t=0;
    	for(int i=0;i<n;i++)
    	{
    		a[i]=in.readLong();
    		if(a[i]==0)
    			c1++;
    		t=max(t,a[i]);
    		if(hm.containsKey(a[i]))
    		{
    			int x=hm.get(a[i]);
    			hm.put(a[i],x+1);
    		}
    		else
    			hm.put(a[i],1);
    	}
    	Arrays.sort(a);
    	int c=0;
    	int max=0;
    	if(c1>=100)
    		pw.println(c1);
    	else
    	{
    	for(int i=0;i<n;i++)
    	{
    		long x=a[i];
    		long r=x;
    		for(int j=0;j<n;j++)
    		{
    			x=r;
    			if(i==j)
    				continue;
    			long y=a[j];
    			Pair f=new Pair(x,y);
    			if(hs.contains(f))
    			{
    				continue;
    			}
    			else
    				hs.add(f);
    			long s=x+y;
    			c=2;
    			ArrayList<Long>aa=new ArrayList<Long>();
    			if(hm.containsKey(x))	
    			{
    				int z=hm.get(x);
    				if(z==1)
    					hm.remove(x);
    				else
    					hm.put(x,z-1);
    				aa.add(x);
    			}
    			if(hm.containsKey(y))	
    			{
    				int z=hm.get(y);
    				if(z==1)
    					hm.remove(y);
    				else
    					hm.put(y,z-1);
    				aa.add(y);
    			}
    			while(true)
    			{
    			if(hm.containsKey(s))
    			{
    				int z=hm.get(s);
    				
    				if(z==1)
    					hm.remove(s);
    				else
    					hm.put(s,z-1);
        			c++;
        			x=y;
        			y=s;
        			aa.add(s);
        			s=x+y;
        			
    			}
    			else 
    				break;
    			}
    		/*	for(int k=0;k<n;k++)
    			{
    				if(i==k)
    					continue;
    				if(j==k)
    					continue;
    				if(s==a[k])
    				{
    					c++;
    					x=y;
    					y=a[k];
    					s=x+y;
    				}
    			}*/
    			for(long v:aa)
    			{
    				if(hm.containsKey(v))
    	    		{
    	    			int z=hm.get(v);
    	    			hm.put(v,z+1);
    	    		}
    	    		else
    	    			hm.put(v,1);
    			}
    			max=max(max,c);
    		}
    	}
		   pw.println(max);	     	
    	
    	//}
    	}		
    	
    	pw.close();
    }
    
   
    public static BigInteger fact(int n)
    {
    	BigInteger x=BigInteger.valueOf(1);
    	for(int i=1;i<=n;i++)
    	{
    		x=x.multiply(BigInteger.valueOf(i));
    	}
    	return x;
    }
    /* returns nCr mod m */
   	public static long comb(long n, long r, long m) 
   	{
   		long p1 = 1, p2 = 1;
   		for (long i = r + 1; i <= n; i++) {
   			p1 = (p1 * i) % m;
   		}
   		p2 = factMod(n - r, m);
   		p1 = divMod(p1, p2, m);
   		return p1 % m;
   	}
   /* returns a/b mod m, works only if m is prime and b divides a */
   	public static long divMod(long a, long b, long m) 
   	{
   		long c = powerMod(b, m - 2, m);
   		return ((a % m) * (c % m)) % m;
   	}
   /* calculates factorial(n) mod m */
   	public static long factMod(long n, long m) {
   		long result = 1;
   		if (n <= 1)
   			return 1;
   		while (n != 1) {
   			result = ((result * n--) % m);
   		}
   		return result;
   	}
   /* This method takes a, b and c as inputs and returns (a ^ b) mod c */
   	public static long powerMod(long a, long b, long c) {
   		long result = 1;
   		long temp = 1;
   		long mask = 1;
   		for (int i = 0; i < 64; i++) {
   			mask = (i == 0) ? 1 : (mask * 2);
   			temp = (i == 0) ? (a % c) : (temp * temp) % c;
   			/* Check if (i + 1)th bit of power b is set */
   			if ((b & mask) == mask) {
   				result = (result * temp) % c;
   			}
   		}
   		return result;
   	}
	static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number <= 3) {
            return true;
        }
        if (number % 2 == 0 || number % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= number) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }
	
public static long gcd(long x,long y)
{
	if(x%y==0)
		return y;
	else
		return gcd(y,x%y);
}
	
public static int gcd(int x,int y)
{
	if(x%y==0)
		return y;
	else 
		return gcd(y,x%y);
}
public static int abs(int a,int b)
{
	return (int)Math.abs(a-b);
}
public static long abs(long a,long b)
{
	return (long)Math.abs(a-b);
}
public static int max(int a,int b)
{
	if(a>b)
		return a;
	else
		return b;
}
public static int min(int a,int b)
{
	if(a>b)
		return b;
	else 
		return a;
}
public static long max(long a,long b)
{
	if(a>b)
		return a;
	else
		return b;
}
public static long min(long a,long b)
{
	if(a>b)
		return b;
	else 
		return a;
}

static boolean isPowerOfTwo (long v) {
	return (v & (v - 1)) == 0;
}
public static long pow(long n,long p,long m)
{
	 long  result = 1;
	  if(p==0)
	    return 1;
	if (p==1)
	    return n;
	while(p!=0)
	{
	    if(p%2==1)
	        result *= n;
	    if(result>=m)
	    result%=m;
	    p >>=1;
	    n*=n;
	    if(n>=m)
	    n%=m;
	}
	return result;
}
public static long pow(long n,long p)
{
	long  result = 1;
	  if(p==0)
	    return 1;
	if (p==1)
	    return n;
	while(p!=0)
	{
	    if(p%2==1)
	        result *= n;	    
	    p >>=1;
	    n*=n;	    
	}
	return result;

}
static class Pair implements Comparable<Pair>
{
	long a,b;
	Pair (long a,long b)
	{
		this.a=a;
		this.b=b;
	}

	public int compareTo(Pair o) {
		// TODO Auto-generated method stub
		if(this.a!=o.a)
		return Long.compare(this.a,o.a);
		else
			return Long.compare(this.b, o.b);
		//return 0;
	}
	public boolean equals(Object o) {
        if (o instanceof Pair) {
            Pair p = (Pair)o;
            return p.a == a && p.b == b;
        }
        return false;
    }
    public int hashCode() {
        return new Long(a).hashCode() * 63 + new Long(b).hashCode();
    }
} 
    
static long sort(int a[],int n)
{  	int b[]=new int[n];	
	return mergeSort(a,b,0,n-1);}
static long mergeSort(int a[],int b[],long left,long right)
{ long c=0;if(left<right)
 {   long mid=left+(right-left)/2;
	 c= mergeSort(a,b,left,mid);
	 c+=mergeSort(a,b,mid+1,right);
	 c+=merge(a,b,left,mid+1,right); }	
	return c;	 }
static long merge(int a[],int  b[],long left,long mid,long right)
{long c=0;int i=(int)left;int j=(int)mid; int k=(int)left;
while(i<=(int)mid-1&&j<=(int)right)
{ if(a[i]<=a[j]) {b[k++]=a[i++]; }
else	{ b[k++]=a[j++];c+=mid-i;}}
while (i <= (int)mid - 1)   b[k++] = a[i++]; 
while (j <= (int)right) b[k++] = a[j++];
for (i=(int)left; i <= (int)right; i++) 
	a[i] = b[i];  return c;  }
    
    
   static  class InputReader
    {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
            this.stream = stream;
        }

        public int read()
        {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars)
            {
                curChar = 0;
                try
                {
                    numChars = stream.read(buf);
                } catch (IOException e)
                {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int readInt()
        {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-')
            {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do
            {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String readString()
        {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do
            {
                res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }
        public double readDouble() {
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
                    return res * Math.pow(10, readInt());
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
                        return res * Math.pow(10, readInt());
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    m /= 10;
                    res += (c - '0') * m;
                    c = read();
                }
            }
            return res * sgn;
        }
        public long readLong() {
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
            } while (!isSpaceChar(c));
            return res * sgn;
        }
        public boolean isSpaceChar(int c)
        {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public String next()
        {
            return readString();
        }

        public interface SpaceCharFilter
        {
            public boolean isSpaceChar(int ch);
        }
    }

     static class OutputWriter
    {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream)
        {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer)
        {
            this.writer = new PrintWriter(writer);
        }

        public void print(Object... objects)
        {
            for (int i = 0; i < objects.length; i++)
            {
                if (i != 0)
                    writer.print(' ');
                writer.print(objects[i]);
            }
        }

        public void printLine(Object... objects)
        {
            print(objects);
            writer.println();
        }

        public void close()
        {
            writer.close();
        }

        public void flush()
        {
            writer.flush();
        }

    }
    /* USAGE

    //initialize
        InputReader in 		= new InputReader(System.in);
        OutputWriter out	=	new OutputWriter(System.out);

    //read int
    int i = in.readInt();
    //read string
    String s = in.readString();
    //read int array of size N
    int[] x = IOUtils.readIntArray(in,N);
    //printline
    out.printLine("X");


    //flush output
    out.flush();

    //remember to close the
    //outputstream, at the end
    out.close();

    */
  static   class IOUtils {

        public static int[] readIntArray(InputReader in, int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++)
                array[i] = in.readInt();
            return array;
    }
    }
//BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	//StringBuilder sb=new StringBuilder("");
	 //InputReader in = new InputReader(System.in);
  // OutputWriter out = new OutputWriter(System.out);
	//PrintWriter pw=new PrintWriter(System.out);
	//String line=br.readLine().trim();
	       	
	//int t=Integer.parseInt(br.readLine());
  //	while(t-->0)
  	//{
  	//int n=Integer.parseInt(br.readLine());
	//long n=Long.parseLong(br.readLine());
	//String l[]=br.readLine().split(" ");
  //int m=Integer.parseInt(l[0]);
	//int k=Integer.parseInt(l[1]);
	//String l[]=br.readLine().split(" ");
	//l=br.readLine().split(" ");
	/*int a[]=new int[n];
	for(int i=0;i<n;i++)
	{
		a[i]=Integer.parseInt(l[i]);
	}*/
	   //System.out.println(" ");	     	
	
	//}
}
