import java.lang.*;
import java.math.BigInteger;
import java.io.*;
import java.util.*;

public class Solution implements Runnable{
    public static BufferedReader br;
    public static PrintWriter out;
    public static StringTokenizer stk;
    public static boolean isStream = true;

    public static void main(String[] args) throws IOException {
    	if (isStream) {
            br = new BufferedReader(new InputStreamReader(System.in));
        } else {
            br = new BufferedReader(new FileReader("in.txt"));
        }
        out = new PrintWriter(System.out);
        new Thread(new Solution()).start();
    }

    public void loadLine() {
        try {
            stk = new StringTokenizer(br.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String nextLine() {
        try {
            return br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }

    public String nextWord() {
        while (stk==null||!stk.hasMoreTokens()) loadLine();
        return stk.nextToken();
    }

    public Integer nextInt() {
        while (stk==null||!stk.hasMoreTokens()) loadLine();
        return Integer.valueOf(stk.nextToken());
    }

    public Long nextLong() {
        while (stk==null||!stk.hasMoreTokens()) loadLine();
        return Long.valueOf(stk.nextToken());
    }

    public Double nextDouble() {
        while (stk==null||!stk.hasMoreTokens()) loadLine();
        return Double.valueOf(stk.nextToken());
    }
    
    public Float nextFloat() {
        while (stk==null||!stk.hasMoreTokens()) loadLine();
        return Float.valueOf(stk.nextToken());
    }
    
    public void run() {
    	int n = nextInt();
    	int sum = 0;
    	int ans = 0;
    	for (int i = 0; i < n; i++) {
    		sum -= nextInt();
    		sum += nextInt();
    		ans = Math.max(ans, sum);
    	}
    	out.println(ans);
    	out.flush();
    }
}
