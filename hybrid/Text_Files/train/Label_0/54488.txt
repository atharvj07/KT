import java.io.*;
import java.util.*;
import java.math.*;
import java.lang.*;
 
import static java.lang.Math.*;
 
public class Cf182 implements Runnable 
{
	static class InputReader 
	{
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;
		private SpaceCharFilter filter;
		private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		public InputReader(InputStream stream) 
		{
			this.stream = stream;
		}
		
		public int read()
		{
			if (numChars==-1) 
				throw new InputMismatchException();
            
			if (curChar >= numChars) 
			{
				curChar = 0;
				try
				{
					numChars = stream.read(buf);
				}
				catch (IOException e)
				{
					throw new InputMismatchException();
				}
                
				if(numChars <= 0)               
					return -1;
			}
			return buf[curChar++];
		}
     
		public String nextLine()
		{
			String str = "";
			try
			{
				str = br.readLine();
			}
			catch (IOException e)
			{
				e.printStackTrace();
			}	
			return str;
		}
		public int nextInt() 
		{
			int c = read();
            
			while(isSpaceChar(c)) 
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
				if(c<'0'||c>'9') 
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			while (!isSpaceChar(c)); 
        
			return res * sgn;
		}
        
		public long nextLong() 
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
			long res = 0;
			
			do 
			{
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}	
			while (!isSpaceChar(c));
				return res * sgn;
		}
		
		public double nextDouble() 
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
			double res = 0;
			while (!isSpaceChar(c) && c != '.') 
			{
				if (c == 'e' || c == 'E')
					return res * Math.pow(10, nextInt());
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			if (c == '.') 
			{
				c = read();
				double m = 1;
				while (!isSpaceChar(c))
				{
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
			} 
			while (!isSpaceChar(c));
            
			return res.toString();
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
	public static void main(String args[]) throws Exception 
	{
		new Thread(null, new Cf182(),"Main",1<<27).start();
	}	
	

	//  array sorting by colm
public static void sortbyColumn(int arr[][], int col) 
    { 
        
        Arrays.sort(arr, new Comparator<int[]>() { 
            
          @Override
          public int compare(final int[] entry1,  
                             final int[] entry2) { 
  
           
            if (entry1[col] > entry2[col]) 
                return 1; 
            else
                return -1; 
          } 
        });  
    } 
	
	
	// fibonaci
	static int fib(int n) 
    { 
        int a = 0, b = 1, c; 
        if (n == 0) 
            return a; 
        for (int i = 2; i <= n; i++) 
        { 
            c = a + b; 
            a = b; 
            b = c; 
        } 
        return b; 
    } 
    
// sort a string
    public static String sortString(String inputString) 
    { 
        
        char tempArray[] = inputString.toCharArray(); 
          
         
        Arrays.sort(tempArray); 
          
         
        return new String(tempArray); 
    } 
    // pair function
    
    // list.add(new Pair<>(sc.nextInt(), i + 1));
    //     Collections.sort(list, (a, b) -> Integer.compare(b.first, a.first));
    private static class Pair<F, S> {
 
        private F first;
 
        private S second;
 
        public Pair() {}
 
        public Pair(F first, S second) {
            this.first = first;
            this.second = second;
        }
    }
    
	// SortedArrayList<Integer> test = new SortedArrayList<Integer>();
    // test.insert(5); 
            public static class SortedArrayList<T> extends ArrayList<T> {
        
            @SuppressWarnings("unchecked")
            public void insert(T value) {
                add(value);
                Comparable<T> cmp = (Comparable<T>) value;
                for (int i = size()-1; i > 0 && cmp.compareTo(get(i-1)) < 0; i--)
                    Collections.swap(this, i, i-1);
            }
        }
    
    
    //isPrime
    
    static boolean isPrime(int n) 
    { 
        // Corner cases 
        if (n <= 1) 
            return false; 
        if (n <= 3) 
            return true; 
  
        // This is checked so that we can skip 
        // middle five numbers in below loop 
        if (n % 2 == 0 || n % 3 == 0) 
            return false; 
  
        for (int i = 5; i * i <= n; i = i + 6) 
            if (n % i == 0 || n % (i + 2) == 0) 
                return false; 
  
        return true; 
    } 
    
    
    static int countDivisors(int n) 
    { 
        int cnt = 0; 
        for (int i = 1; i <= Math.sqrt(n); i++) 
        { 
            if (n % i == 0) { 
               
                if (n / i == i) 
                    cnt++; 
  
                else 
                    cnt = cnt + 2; 
            } 
        } 
        return cnt; 
    } 
    
    
   
    

	public void run()
	{
		InputReader sc = new InputReader(System.in);
		PrintWriter w = new PrintWriter(System.out);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		ArrayList<Integer> ans = new ArrayList<Integer>();
		
		if(n<=k)
		{
		    w.println("1");
		    w.println("1");
		}
		else
		{
		    if(n%(k*2 + 1)==0)
		    {
		        ans.add(k+1);
		        int count = 0;
		        for(int i=k+2;i<=n;i++)
		        {
		            if(count==(2*k))
		            {
		                ans.add(i);
		                count = 0;
		            }
		            else
		                count++;
		        }
		        
		        w.println(ans.size());
		        for(int i:ans)
		            w.print(i+" ");
		    }
		    else
		    {
    		    int count = 0;
    		    int temp = n%(k*2 + 1);
    		    if(temp<=k)
    		    {
    		        ans.add(temp);
    		        for(int i=temp + 1;i<=n;i++)
        		    {
        		        if(count==(2*k))
    		            {
    		                ans.add(i);
    		                count = 0;
    		            }
    		            else
    		                count++;
        		    }
        		    w.println(ans.size());
    		        for(int i:ans)
    		            w.print(i+" ");
    		    }
    		    else
    		    {
        		    temp = n%(k*2 + 1);
        		    ans.add(temp - k + 1);
        		    for(int i=temp - k + 2;i<=n;i++)
        		    {
        		        if(count==(2*k))
    		            {
    		                ans.add(i);
    		                count = 0;
    		            }
    		            else
    		                count++;
        		    }
        		    w.println(ans.size());
    		        for(int i:ans)
    		            w.print(i+" ");
		        }
		    }
		}
		
        w.flush();
	    w.close();
	}
}



