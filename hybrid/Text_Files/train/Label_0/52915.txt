// Main Code at the Bottom
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*; 
public class Main{
	//Fast IO class
    static class FastReader {
        BufferedReader br; 
        StringTokenizer st; 
        public FastReader() {
        	boolean env=System.getProperty("ONLINE_JUDGE") != null;
        	if(!env) {
        		try {
					br=new BufferedReader(new FileReader("input.txt"));
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				}
        	}
        	else br = new BufferedReader(new InputStreamReader(System.in)); 
        } 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException  e) {
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
            } 
            catch (IOException e) {
                e.printStackTrace(); 
            } 
            return str; 
        } 
    }     
    static long MOD=(long)1e9+7;
    //debug
    static void debug(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }
    static FastReader sc=new FastReader();
    static PrintWriter out=new PrintWriter(System.out);  
    //Global variables and functions
    //Main function(The main code starts from here)
    public static void main (String[] args) throws java.lang.Exception {
    	int test=1;
    	//test=sc.nextInt();
    	while(test-->0) {
    		int n = sc.nextInt(), q=sc.nextInt();
    		int a[]=new int[n];
    		for(int i=0;i<n;i++) a[i]=sc.nextInt();
    		HashSet<Integer> set = new HashSet<>();
    		int l = 0, r = 0, map[]=new int[n];
    		Arrays.fill(map, n);
    		while(l<n && r<n) {
    			int tmp = a[r];
    			HashSet<Integer> cur = new HashSet<>();
    			boolean flag = false;
    			for(int i = 2;i*i<=tmp;i++) {
    				if(tmp%i==0) {
    					while(tmp%i==0) tmp/=i;
    					if(set.contains(i)) flag = true;
    					cur.add(i);
    				}
    			}
    			if(tmp>1) {
    				if(set.contains(tmp)) flag = true;
    				cur.add(tmp);
    			}
    			if(flag) {
    				map[l]=r;
    				tmp = a[l];
    				for(int i = 2;i*i<=tmp;i++) {
        				if(tmp%i==0) {
        					while(tmp%i==0) tmp/=i;
        					set.remove(i);
        				}
        			}
    				if(tmp>1) {
    					set.remove(tmp);
    				}
    				l++;
    			}
    			else {
    				for(Integer x: cur) set.add(x);
    				r++;
    			}
    		}
    		int up[][]=new int[n][19];
    		for(int i=0;i<n;i++) up[i][0]=map[i];
    		for(int j=1;j<19;j++) {
    			for(int i=0;i<n;i++) {
    				if(up[i][j-1]==n) up[i][j]=n;
    				else up[i][j]=up[up[i][j-1]][j-1];
    			}
    		}
    		while(q-->0) {
    			l = sc.nextInt()-1; r = sc.nextInt()-1;
    			int ans = 0;
    			for(int jump = 18;jump>=0;jump--) {
    				if(up[l][jump]<=r) {
    					ans+=(1<<jump);
    					l = up[l][jump];
    				}
    			}
    			ans++;
    			out.println(ans);
    			
    		}
    		
    	}
        out.flush();
        out.close();
    }
}