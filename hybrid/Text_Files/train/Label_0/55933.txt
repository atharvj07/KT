/*==========================================================================*/
/*
*		AUTHOR:    RonWonWon    
*		CREATED:   02.05.2021 19:58:57
*		EMAIL:     rachitpts.2454@gmail.com                                  
*/
/*==========================================================================*/
import java.io.*;
import java.util.*;

public class B {
	
	public static void main(String[] args) {
        FastScanner in = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = in.nextInt(), tt = 0;
        while(t-->0) { 
        	int n = in.nextInt();
        	if(n%2!=0) out.println("NO");
        	else{
        		n/=2;
        		if(Math.sqrt(n)==Math.ceil(Math.sqrt(n))) out.println("YES");
        		else{
        			if(n%2!=0) out.println("NO");
        			else{
        				n/=2;
            		if(Math.sqrt(n)==Math.ceil(Math.sqrt(n))) out.println("YES");
            		else out.println("NO");
        			}
        		}
    	    }
    		//tt++; out.println("Case #"+tt+": "+ans);
        }
        out.flush();
	}
	
	static class FastScanner {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		
		String next() {
			while(!st.hasMoreTokens())
				try { st = new StringTokenizer(br.readLine()); }
				catch(IOException e) {}
			return st.nextToken();
		}
		
		String nextLine(){
			try{ return br.readLine(); } 
			catch(IOException e) { } return "";
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		
		long nextLong() {
			return Long.parseLong(next());
		}
		
		int[] readArray(int n) {
			int a[] = new int[n];
			for(int i=0;i<n;i++) a[i] = nextInt();
			return a;
		}
	}

	static final Random random = new Random();

	static void ruffleSort(int[] a){
		int n = a.length;
		for(int i=0;i<n;i++){
			int j = random.nextInt(n), temp = a[j];
			a[j] = a[i]; a[i] = temp;
		}
		Arrays.sort(a); 	
	}
}
