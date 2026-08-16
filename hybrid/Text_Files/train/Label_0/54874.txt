
import java.io.*;
import java.util.*;





public class codeforces {
	static FastReader fr;
	static class FastReader {

        BufferedReader br;
        StringTokenizer st;
        BufferedWriter bw;
        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
            bw=new BufferedWriter(new OutputStreamWriter(System.out));
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
        
        char nextChar() {
        	return next().charAt(0);
        }
 
        int nextInt() { return Integer.parseInt(next()); }
 
        long nextLong() { return Long.parseLong(next()); }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
        
        void write(String str){
        
                try {
                    bw.write(str);
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
        }
        
        void close(){
            try {
                 bw.close();
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
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
        }
    }
    public static void main(String[] args) throws java.lang.Exception {
	  fr=new FastReader();
	  int t=1;
	  while(t-->0){
	      solve();
	  }
	  fr.close();
	}

  public static void solve() {
	int n=fr.nextInt();
	long k=fr.nextLong();
	long x=fr.nextLong();
	List<Long> arr=new ArrayList<>();
	for(int i=0;i<n;i++) {
		arr.add(fr.nextLong());
	}
	Collections.sort(arr);
	List<Long> diffs=new ArrayList<>();
	long ans=1;
	for(int i=0;i<n-1;i++) {
		long a=arr.get(i);
		long b=arr.get(i+1);
		if(b-a>x) {
			ans++;
			diffs.add(b-a);
		}
	}
	Collections.sort(diffs);
	for(int i=0;i<diffs.size() && k>0;i++) {
		long y=diffs.get(i);
		if(y%x==0) {
			if(y/x-1<=k) {
				k-=y/x-1;
				ans--;
			}
			else break;
		}
		else {
			if(y/x<=k) {
				k-=y/x;
				ans--;
			}
			else break;
		}
	}
	fr.write(ans+"\n");
  }
  
  public static int[] readArray(int n) {
	  int[] arr=new int[n];
	  for(int i=0;i<n;i++) {
		  arr[i]=fr.nextInt();
	  }
	  return arr;
  }
}