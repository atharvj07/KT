	import java.io.*;
	import java.util.*;
	public class Taske{
	    public static void main(String[] args) {
	        InputStream inputStream = System.in;
	        OutputStream outputStream = System.out;
	        InputReader in = new InputReader(inputStream);
	        PrintWriter out = new PrintWriter(outputStream);
	        TaskE solver = new TaskE();
	        solver.solve(1, in, out);
	        out.flush();out.close();
	    }
	        static class TaskE {
	        int n,a[];
	        final long min=Integer.MIN_VALUE;
	        int cnt=0;long sum=min;
	        long dfs(int u,int pa,boolean b){
	        	long r=a[u];
	        	for(int v:ja[u]){
	        		if(v==pa)continue;
	        		long x=dfs(v,u,b);
	        		if(x>0)r+=x;
	        	}
	        	if(r>sum){
	        		sum=r;
	        	}else if(r==sum&&b){
	        		++cnt;r=0;
	        	}return r;
	        }
		 	  public void solve(int testNumber, InputReader in, PrintWriter out) {
	 			n=in.nextInt();
	 			a=new int[n+1];
	 			for(int i=1;i<=n;i++)a[i]=in.nextInt();
	 			make(n,n-1,in);
	 			dfs(1,0,false);dfs(1,0,true);
	 			out.print((sum*cnt)+" "+cnt);
	          }
	          int ja[][],from[],to[],c[];
			void make(int n,int m,InputReader in){
				ja=new int[n+1][];from=new int[m];to=new int[m];c=new int[n+1];
				for(int i=0;i<m;i++){
					from[i]=in.nextInt();to[i]=in.nextInt();
					c[from[i]]++;c[to[i]]++;
				}
				for(int i=0;i<=n;i++){
					ja[i]=new int[c[i]];
					c[i]=0;
				}
				for(int i=0;i<m;i++){
					ja[from[i]][c[from[i]]++]=to[i];
					ja[to[i]][c[to[i]]++]=from[i];
				}
			}
	    }
	    static class InputReader {
	        BufferedReader br;
	        StringTokenizer st;
	        public InputReader(InputStream stream) {
	            br = new BufferedReader(new InputStreamReader(stream));
	            st = null;
	        }
	
	        String next() {
	            while (st == null || !st.hasMoreTokens()) {
	                String s = null;
	                try {
	                    s = br.readLine();
	                } catch (IOException e) {
	                    e.printStackTrace();
	                }
	                if (s == null)
	                    return null;
	                st = new StringTokenizer(s);
	            }
	            return st.nextToken();
	        }
	
	        boolean hasMoreTokens() {
	            while (st == null || !st.hasMoreTokens()) {
	                String s = null;
	                try {
	                    s = br.readLine();
	                } catch (IOException e) {
	                    e.printStackTrace();
	                }
	                if (s == null)
	                    return false;
	                st = new StringTokenizer(s);
	            }
	            return true;
	        }
	
	        public int nextInt() {
	            return Integer.parseInt(next());
	        }
	        public long nextLong() {
	            return Long.parseLong(next());
	        }
	        public double nextDouble() {
	            return Double.parseDouble(next());
	        }
	    }
	}