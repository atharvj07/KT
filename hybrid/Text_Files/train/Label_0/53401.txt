import java.io.*; 
import java.math.BigInteger;
import java.util.*;
 
public class Main {
    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner();
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[M];
        for (int i = 0; i < M; i++)
        	A[i] = sc.nextInt();
        int[] costs = {0,2,5,5,4,5,6,3,7,6};
        BigInteger[] dp = new BigInteger[N+1];
        for (int i = 0; i <= N; i++) {
        	dp[i] = BigInteger.ZERO;
        }
        int[] digits = new int[N+1];
        BigInteger[] bdigits = new BigInteger[11];
        for (int i = 0; i < 10; i++) {
            bdigits[i] = new BigInteger(Integer.toString(i));
        }
        for (int i = 1; i <= N; i++) {
        	BigInteger num = BigInteger.ZERO;
        	for (int j = 0; j < M; j++) {
        		if (costs[A[j]] <= i) {
        			if (i > costs[A[j]] && dp[i-costs[A[j]]].equals(BigInteger.ZERO))
        				continue;
        			BigInteger power = BigInteger.TEN.pow(digits[i-costs[A[j]]]);
        			BigInteger numGuess = (power.multiply(bdigits[A[j]])).add(dp[i-costs[A[j]]]);
        			num = num.max(numGuess);
        		}
        	}
        	dp[i] = num;
        	BigInteger prevPow = BigInteger.TEN.pow(digits[i-1]);
        	if (dp[i].compareTo(prevPow) >= 0) {
        		digits[i] = digits[i-1]+1;
        	} else {
        		digits[i] = digits[i-1];
        	}
        }
        char[] s = dp[N].toString().toCharArray();
        Integer[] d = new Integer[s.length];
        for (int i = 0; i < s.length; i++)
        	d[i] = s[i]-'0';
        d = sort(d);
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < d.length; i++) {
        	if (d[i] != 0)
        		ans.append(d[i]);
        }
        System.out.println(ans);
    }
    
    public static Integer[] sort(Integer[] array) {
    	//Sort an array (immune to quicksort TLE)
		Random rgen = new Random();
		for (int i = 0; i< array.length; i++) {
		    int randomPosition = rgen.nextInt(array.length);
		    int temp = array[i];
		    array[i] = array[randomPosition];
		    array[randomPosition] = temp;
		}
		Arrays.sort(array, new Comparator<Integer>() {
			  @Override
			  public int compare(Integer a1, Integer a2) {
				  return a2-a1;
			  }
		});

		return array;
	}
    
    static class FastScanner { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastScanner() { 
            br = new BufferedReader(new InputStreamReader(System.in)); 
        } 
  
        String next() { 
            while (st == null || !st.hasMoreElements()) { 
                try { 
                    st = new StringTokenizer(br.readLine());
                } catch (IOException  e) { 
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
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
  
        String nextLine() { 
            String str = ""; 
            try { 
                str = br.readLine(); 
            } catch (IOException e) {
                e.printStackTrace(); 
            } 
            return str; 
        }
    }
}