import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.* ;
import java.io.* ;
@SuppressWarnings("unused")

//Scanner s = new Scanner(new File("input.txt"));
//s.close();
//PrintWriter writer = new PrintWriter("output.txt");
//writer.close();
//BufferedReader in = new BufferedReader(new InputStreamReader(System.in)) ;

//[a-z] = [97-122] ------- [A-Z] = [65-90]

/*counting number of bits in an integer :
 * 
 *  int x = (int)(Math.log(num) /
                      Math.log(2)) + 1;
 */
public class cf
{	
	static final int mod = 1000000007 ;
	
	static boolean not_prime[] = new boolean[1000001] ;
	static void sieve() {
		for(int i=2 ; i*i<1000001 ; i++) {
			if(not_prime[i]==false) {
				for(int j=2*i ; j<1000001 ; j+=i) {
					not_prime[j]=true ;
				}
			}
		}not_prime[0]=true ; not_prime[1]=true ;
	}	
	
	public static long bexp(long base , long power)
	{
		long res=1L ;
		
		//base = base%mod ;
		
		while(power>0) {
			if((power&1)==1) {
				res=(res*base);//%mod ;
				power-- ;
			}
			else {
				base=(base*base);//%mod ;
				power>>=1 ;
			}
		}
		
		return res ;
	}

	static long modInverse(long n, long p)
	{
	    return power(n, p - 2, p);
	}
	static long power(long x, long y, long p)
	{
	  
	    // Initialize result
	    long res = 1;
	  
	    // Update x if it is more than or
	    // equal to p
	    x = x % p;
	  
	    while (y > 0) {
	  
	        // If y is odd, multiply x
	        // with result
	        if (y % 2 == 1)
	            res = (res * x) % p;
	  
	        // y must be even now
	        y = y >> 1; // y = y/2
	        x = (x * x) % p;
	    }
	  
	    return res;
	}
	static long nCrModPFermat(int n, int r, long p)
	{
		if(n<r) return 0 ;
	    if (r == 0)
	        return 1;

	    long[] fac = new long[n + 1];
	    fac[0] = 1;
	  
	    for (int i = 1; i <= n; i++)
	        fac[i] = fac[i - 1] * i % p;
	  
	    return (fac[n] * modInverse(fac[r], p) % p
	            * modInverse(fac[n - r], p) % p)
	        % p;
	}
	
	private static long modular_add(long a, long b)
	{
	    return ((a % mod) + (b % mod)) % mod;
	}
	private static long modular_sub(long a, long b)
	{
	    return ((a % mod) - (b % mod) + mod) % mod;
	}
	private static long modular_mult(long a, long b)
	{
	    return ((a % mod) * (b % mod)) % mod;
	}
	
	static long lcm(int a, int b)
	{
		return (a / gcd(a, b)) * b;
	}
	private static long gcd(long a, long b)
	{
		if (b == 0) {
			return a;
		}
		return gcd(b, a % b);
	}

	
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() { return Integer.parseInt(next()); }
 
        long nextLong() { return Long.parseLong(next()); }
 
        double nextDouble(){ return Double.parseDouble(next()); };
 
        String nextLine()
        {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
	
	//static HashMap<Integer , ArrayList<Integer>> map = new HashMap<>() ;
	static boolean vis[] ; 
	public static void main(String[] args)throws IOException//throws FileNotFoundException
    {
	   	FastReader in = new FastReader() ;	
    	StringBuilder op = new StringBuilder() ;
    	int n = in.nextInt() ;
    	int k = in.nextInt() ;
    	int a[] = new int[n] ;
    	for(int i=0 ; i<n ; i++)a[i]=in.nextInt() ;
    	int i=0 ;
    	while(k>0 && i<n && a[i]<0) {
    		a[i]*=-1;
    		i++ ;
    		k--;
    	}
    	int sum=0 ;
    	if(k==0) {
    		for(i=0 ; i<n ; i++)sum+=a[i] ;
    		System.out.println(sum);System.exit(0);
    	}
    	Arrays.sort(a) ;
    	if((k&1)==1)
    		a[0]*=-1 ;
		for( i=0 ; i<n ; i++)sum+=a[i] ;
		System.out.println(sum);
    }
}















