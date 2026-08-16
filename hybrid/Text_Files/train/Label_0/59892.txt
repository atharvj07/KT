import java.io.*;    //PrintWriter
import java.math.*;  //BigInteger, BigDecimal
import java.util.*;  //StringTokenizer, ArrayList


public class MailRuCup2018_R2_C
{	
	FastReader in;
	PrintWriter out;
	
	public static void main(String[] args)  {
		new MailRuCup2018_R2_C().run();
	}
	
	void run()
	{		
		in = new FastReader(System.in);
		out = new PrintWriter(System.out);
		solve();
		out.close();
	}
	
	void solve()
	{
		int l1 = in.nextInt();
		int r1 = in.nextInt();
		int t1 = in.nextInt();		
		int b1 = r1 - l1 + 1;
		
		int l2 = in.nextInt();
		int r2 = in.nextInt();
		int t2 = in.nextInt();
		int b2 = r2 - l2 + 1;		

		long gcd = GCD(t1,t2);
		long shift = ((l2 - l1) % gcd + gcd) % gcd;
		long ans = Math.min(b1, b2 + shift) - Math.max(0, shift);
		shift -= gcd;
		ans = Math.max(ans,  Math.min(b1,  b2 + shift) - Math.max(0,  shift));
		ans = Math.max(ans, 0);
		out.println(ans);
		
//		long ans = 0, f;		
//		if(b1 > b2)
//		{
//			f = (l1-l2)/gcd;
//			l2 += (f*gcd);
//			ans = Math.max(ans, Math.min(l1+b1,l2+b2)-Math.max(l1,l2));
//			l2 += gcd;
//			ans = Math.max(ans, Math.min(l1+b1,l2+b2)-Math.max(l1,l2));
//		}
//		else if(l1 < l2)
//		{
//			f = (l2-l1)/gcd;
//			l1 += (f*gcd);
//			ans = Math.max(ans, Math.min(l1+b1,l2+b2)-Math.max(l1,l2));
//			l1 += gcd;
//			ans = Math.max(ans, Math.min(l1+b1,l2+b2)-Math.max(l1,l2));
//		}
//		else {
//			ans = Math.min(b1, b2);
//		}
//		out.println(ans);		
	}
	
    long GCD(long a, long b)
    {
        if (b == 0) return a;
        return GCD(b, a % b);
    }
    long LCM(long a, long b)
    {
        return a * b / GCD(a, b);
    }



	//-----------------------------------------------------
	void runWithFiles() {
		in = new FastReader(new File("input.txt"));
		try {
			out = new PrintWriter(new File("output.txt"));
		} 
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		solve();
		out.close();
	}
	
	class FastReader
	{
	    BufferedReader br;
	    StringTokenizer tokenizer;
	    
	    public FastReader(InputStream stream)
	    {
	        br = new BufferedReader(new InputStreamReader(stream));
	        tokenizer = null;
	    }
		public FastReader(File f) {
			try {
				br = new BufferedReader(new FileReader(f));
				tokenizer = null;
			}
			catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
	    
	    private String next() {
	        while (tokenizer == null || !tokenizer.hasMoreTokens())
	            try {
	            	tokenizer = new StringTokenizer(br.readLine());
	            }
	            catch (IOException e) {
	                throw new RuntimeException(e);
	            }
	        return tokenizer.nextToken();
	    }
		public String nextLine() {
			try	{
				return br.readLine();
			}
			catch(Exception e) {
				throw(new RuntimeException());
			}
		}

	    int nextInt() {
	        return Integer.parseInt(next());
	    }
	    long nextLong() {
	        return Long.parseLong(next());
	    }
	    double nextDouble() {
	        return Double.parseDouble(next());
	    }	    
	    BigInteger nextBigInteger() {
	        return new BigInteger(next());
	    }
	    BigDecimal nextBigDecimal() {
	        return new BigDecimal(next());
	    }
	}
}
