import java.io.*;
import java.util.*;
/* REMINDERS
 * CHECK INT VS LONG, IF YOU NEED TO STORE LARGE NUMBERS
 * CHECK CONSTRAINTS, C <= N <= F...
 * CHECK SPECIAL CASES, N = 1...
 * CHECK ARRAY BOUNDS, HOW BIG ARRAY HAS TO BE
 * TO TEST TLE/MLE, PLUG IN MAX VALS ALLOWED AND SEE WHAT HAPPENS
 * ALSO CALCULATE BIG-O, OVERALL TIME COMPLEXITY
 */
 
 
public class FadiLCMEfficient {
	public static void main(String[] args) throws IOException {
		//get input separately
		BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter p = new PrintWriter(new BufferedOutputStream(System.out));
		StringTokenizer s = new StringTokenizer(b.readLine());
		long x = Long.parseLong(s.nextToken());
		
		//edge case: x = 1
		long[] ints = new long[] {1,1};
		if (x != 1) {
			ints = printDivisors(x);
			Arrays.sort(ints);
		} 
		p.println(ints[0] + " " + ints[1]);
		p.close();
		
 
	}
 
	// Recursive method to return gcd of a and b 
	public static long gcd(long a, long b) 
    { 
    if (a == 0) 
        return b;  
    return gcd(b % a, a);  
    } 
      
    // method to return LCM of two numbers 
    public static long lcm(long a, long b) 
    { 
        return (a*b)/gcd(a, b); 
    } 
    public static long[] printDivisors(long n) 
    { 
    	//find smallest such factors, taking the max
    	long curr = n;
    	long first = 0;
    	long sec = 0;
    	
        //find first divisors under sqrt n
    	for (long i = (long)(Math.sqrt(n)); i > 0; i--) {
    		if (n % i == 0 && lcm(i, n / i) == n) {
    			curr = i;
    			break;
    		}
    	}
        
        return new long[] {curr, n / curr};
            	
                
    } 
	
	
	
 
}