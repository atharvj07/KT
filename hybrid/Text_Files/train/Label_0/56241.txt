import java.util.*;
import java.io.*;
import java.lang.Math.*;
 public class KickStart2020{
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
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
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
        }}	
	static boolean equal(String a) {
		boolean hachu = true;
		char ab = a.charAt(0);
		for(int i = 1; i < a.length(); i++) {
			if(ab != a.charAt(i)) {
				hachu = false;
				break;
			}
		}
		return hachu;
	}
	static boolean compare(String a) {
		int z = 0;
		for(int i = 0; i < a.length(); i++) {
			if(a.charAt(i) == '1') {
				z = i;
				break;
			}
		}
		String c = a.substring(0, z + 1);
		String d = a.substring(z + 1, a.length());
		if(equal(c) && equal(d)) return true;
		else return false;
	}
		public static void main(String[] args) throws Exception{
FastReader sc = new FastReader();
int t = sc.nextInt();
while(t-- > 0) {
	int n = sc.nextInt();
	int d = sc.nextInt();
     if(n >= d) System.out.println("YES");
     else {
    	 boolean hachu = false;
	for(int i = 1; i <= n; i++) {
		int z = i + (int)Math.ceil((double)d / (double)(i+1));
		if(z <= n) {
			hachu = true;
			break;
		}
	}
	if(hachu)System.out.println("YES");
	else System.out.println("NO");}
}
		}
}




