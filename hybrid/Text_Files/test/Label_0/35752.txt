import java.io.*;
import java.util.*;
 
public class p1034a {
	// https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
	// https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
	public static HashMap<Integer,Integer> ct;
	public static void add(int val)
	{
		if(ct.containsKey(val))
			ct.put(val,ct.get(val)+1);
		else
			ct.put(val,1);
	}
public static void primeFactors(int n) 
    { 
        // Print the number of 2s that divide n 
        int val = 1;
        boolean check = false;
        while (n%2==0) 
        { 
            check=true;
            n /= 2; 
        }
        if(check)
        	add(2);
        // n must be odd at this point.  So we can 
        // skip one element (Note i = i +2) 
        for (int i = 3; i <= Math.sqrt(n); i+= 2) 
        { 
        	val = 1;
            // While i divides n, print i and divide n 
            check = false;
            while (n%i == 0) 
            { 
                check = true;
                n /= i; 
            }
           	if(check)
           		add(i);
        } 
  
        // This condition is to handle the case whien 
        // n is a prime number greater than 2 
        if (n > 2) 
            add(n);
    } 
    public static int hcf(int a, int b)
    {
    	if(a==0 || b==0)
    		return a+b;
    	return hcf(b,a%b);
    }
    static final int MAXN = 15000001; 
	
	// stores smallest prime factor for every number 
	static int spf[] = new int[MAXN]; 
	
	// Calculating SPF (Smallest Prime Factor) for every 
	// number till MAXN. 
	// Time Complexity : O(nloglogn) 
	static void sieve() 
	{ 
		spf[1] = 1; 
		for (int i=2; i<MAXN; i++) 
	
			// marking smallest prime factor for every 
			// number to be itself. 
			spf[i] = i; 
	
		// separately marking spf for every even 
		// number as 2 
		for (int i=4; i<MAXN; i+=2) 
			spf[i] = 2; 
	
		for (int i=3; i*i<MAXN; i++) 
		{ 
			// checking if i is prime 
			if (spf[i] == i) 
			{ 
				// marking SPF for all numbers divisible by i 
				for (int j=i*i; j<MAXN; j+=i) 
	
					// marking spf[j] if it is not 
					// previously marked 
					if (spf[j]==j) 
						spf[j] = i; 
			} 
		} 
	} 
	
	// A O(log n) function returning primefactorization 
	// by dividing by smallest prime factor at every step 
	static void getFactorization(int x) 
	{ 
		// Vector<Integer> ret = new Vector<>(); 
		int prev = -1;
		while (x != 1) 
		{ 
			if(prev==-1 || spf[x]!=spf[prev])
			{
				add(spf[x]);
			}
			// ret.add(spf[x]);
			prev = x;
			x = x / spf[x];
		} 
		// return ret; 
	}
	public static void main(String[] args)throws IOException {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        
		int n = in.nextInt();
		sieve();
		ct = new HashMap<Integer,Integer>();
		// Arrays.fill(ct,0);
		int arr[] = new int[n];
		for(int i=0;i<n;i++)
			arr[i]=in.nextInt();
		int gcd = 0;
		for(int i = 0; i < n; i++)
		{
			gcd = hcf(arr[i],gcd);
		}
		for(int i=0;i<n;i++)
		{
			getFactorization(arr[i]/(int)gcd);
		}
		int val[] = new int[n+1];
		Arrays.fill(val,0);
		int ans = Integer.MAX_VALUE;
		for (Map.Entry<Integer, Integer> entry : ct.entrySet()) {
			ans = Math.min(ans,n-entry.getValue());
			// System.out.println("[Key] : " + entry.getKey() + " [Value] : " + entry.getValue());
		}
		if(ans==Integer.MAX_VALUE)
			ans=-1;
		out.println(ans);
        out.close();
	}
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
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

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }

}