import java.util.*;
import java.io.*;  

public class Solution{
    public static class pair{
        int x;
        int y;
    }
    public static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
        public String next() {
			while (!st.hasMoreElements())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		public int nextInt() {
			return Integer.parseInt(next());
		}
		public long nextLong() {
			return Long.parseLong(next());
		}
		public int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) {
				a[i]=nextInt();
			}
			return a;
		}public double nextDouble() {
			return Double.parseDouble(next());
		}
    }

    public static void main(String[] args) throws IOException{
        FastScanner fs=new FastScanner();
// 		int t=fs.nextInt();
		PrintWriter out=new PrintWriter(System.out);
        // while(t-->0){
            int n=fs.nextInt();
            int k=fs.nextInt();
            int[] arr=fs.readArray(n);
            String s=fs.next();
            int i=0;
            long sum=0;
            while(i<n){
                char ch=s.charAt(i);
                int g=i;
                while(i<n&&s.charAt(i)==ch){
                    i++;
                }
                ArrayList<Integer> l=new ArrayList<>();
                for(int j=g;j<i;j++){
                    l.add(arr[j]);
                }
                Collections.sort(l,Collections.reverseOrder());
                for(int j=0;j<Math.min(l.size(),k);j++){
                    sum+=l.get(j);
                }
            }
            System.out.println(sum);
        // }
        out.close();
    } 
    public static long calc(long n,long b){
        if(b==1){
            return Long.MAX_VALUE;
        }
        long val=(long)Math.ceil(n/b);
        long p=2;
        long ans=val;
        while(val!=0){
            val=(long)Math.ceil((long)n/(long)Math.pow(b,p));
            p++;
            ans+=val;
        }
        return ans;
    }
    public static long quala(long b){
        long val=(long)Math.ceil(Math.pow(1+(8*b),0.5));
        if(val%2==0){
            long va=(long)(2+val)/(long)2;
            return va;
        }else{
            long va=(long)(1+val)/(long)2;
            return va;
        }
    }
    public static String find(int a,int b){
        if(a==3){
            if(b==1){
                return "abb";
            }else if(b==2){
                return "bab";
            }else{
                return "bba";
            }
        }
        int v=((a-1)*(a-2))/2;
        if(b<=v){
            String s=find(a-1,b);
            StringBuffer sb=new StringBuffer(s);
            int diff=a-s.length();
            while(diff-->0){
                sb.insert(0,"a");
            }
            return sb.toString();
        }else{
            int diff=b-v;
            StringBuffer sb=new StringBuffer();
            sb.append("b");
            for(int i=0;i<a-diff-1;i++){
                sb.append("a");
            }
            sb.append("b");
            for(int i=0;i<diff-1;i++){
                sb.append("a");
            }
            return sb.toString();
        }
        // return new String("a"+s);
    }
    public static long z(long val){
        long p=1;
        while(val!=0){
            long rem=val%10;
            p*=rem;
            val=val/10;
        }
        return p;
    }
    public static int[] soe(int n){
        int[] arr=new int[n];
        arr[0]=0;
        for(int i=1;i<n;i++){
            if(arr[i]==0){
                for(int j=(2*(i+1))-1;j<n;j=j+i+1){
                    arr[j]=1;
                }
            }
        }
        return arr;
    }
    public static int[][] floydWarshall(int graph[][],int V){ 
        int dist[][] = new int[V][V]; 
        int i, j, k; 
        for (i = 0; i < V; i++){ 
            for (j = 0; j < V; j++){
                dist[i][j] = graph[i][j]; 
            }
        }
        for (k = 0; k < V; k++) { 
            for (i = 0; i < V; i++){ 
                for (j = 0; j < V; j++){ 
                    if (dist[i][k] + dist[k][j] < dist[i][j]){ 
                        dist[i][j] = dist[i][k] + dist[k][j]; 
                    }
                } 
            } 
        }
        return dist;
    } 
    public static class Comp implements Comparator<pair>{
        public int compare(pair a,pair b){
            if(a.x!=b.x){
                return b.x-a.x;
            }else{
                return a.y-b.y;
            }
        }
    }
    public static long gcd(long a,long b){
        if (b == 0) 
        return a; 
        return gcd(b, a % b);
    }
    public static int lcm(int a,int b){
        int x=Math.max(a,b);
        int y=Math.min(a,b);
        long ans=x;
        while(ans%y!=0){
            ans+=x;
        }
        if(ans>Integer.MAX_VALUE){
            return -1;
        }
        return (int)ans;
    }
    public static long fact(int n){
        long ans=1;
        for(int i=1;i<=n;i++){
            ans*=i;
        }
        return ans;
    }
}