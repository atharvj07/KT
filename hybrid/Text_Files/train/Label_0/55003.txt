import java.io.*;
import java.util.*;
import java.math.*;
import java.text.DecimalFormat;
import java.text.NumberFormat;
 

@SuppressWarnings("unchecked")
public class Main {
      
    int mod = 1000000007;

    public class SegmentTree{

       int n;
       long[] tree;

       SegmentTree(long[] arr){

          this.n = arr.length; 
          this.tree = new long[2 * n];

          for(int i = n; i < 2 * n; i++){
              this.tree[i] = arr[i - n];
          }

          for(int i = n - 1; i >= 1; i--){
              this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
          }

       }

       public long query(int l, int r){

          long res = 0;
          l = l + n;
          r = r + n;

          while(l < r){

              if(l % 2 == 1){
                  res = res + tree[l]; 
                  l++;
              }

              if(r % 2 == 1){
                  r--;
                  res = res + tree[r];
              }

              l /= 2;
              r /= 2;
          }

          return res;
       }

       public void update(int idx, long v){
          
          idx += n; this.tree[idx] += v;
          while(idx > 1){
             idx /= 2;
             this.tree[idx] = this.tree[2 * idx] + this.tree[2 * idx + 1];
          }
       }


    }


    public class DSU{

       int[] parent;
       int[] size;

       DSU(int n){
          
          this.parent = new int[n + 1];
          for(int i = 1; i <= n; i++) parent[i] = i;
          this.size = new int[n + 1];
       
       }

       public int find(int root){
          
          if(root == parent[root]) return root;
          int p = find(parent[root]);
          parent[root] = p;
          return p;

       }

       public void union(int u, int v){

          int pu = find(u);
          int pv = find(v);
          if(pu == pv) return;
          parent[pv] = pu;
          size[pu] = Math.max(Math.max(size[pu], size[pv]), (size[pu] + 1) / 2 + (size[pv] + 1) / 2 + 1);
       }

       public void merge(int u, int v){

          int pu = find(u);
          int pv = find(v);
          parent[pv] = pu;
          size[pu] += size[pv];
       
       }

    }

    int n, m, q;
    List<Integer>[] map;
    int[] visited;

    public int[] getDiameter(int root){
         
         int maxSoFar = 0;
         int max1 = 0;
         int max2 = 0;
         visited[root] = 1;

         for(int child: map[root]){
            
            if(visited[child] == 1) continue;
            
            int[] diameters = getDiameter(child);

            maxSoFar = Math.max(maxSoFar, diameters[1]);
            int childDia = diameters[0];

            if(childDia > max1){
               max2 = max1;
               max1 = childDia;
            }else if(childDia > max2){
               max2 = childDia;
            }
         
         }

         return new int[]{max1 + 1, Math.max(max1 + max2 + 1, maxSoFar)} ;

    }
   
    public void solve() throws IOException{
      
       n = in.nextInt(); m = in.nextInt(); q = in.nextInt();
       map = new List[n + 1];
       visited = new int[n + 1];
       DSU d = new DSU(n);

       for(int i = 1; i <= n; i++) map[i] = new ArrayList<>();
       for(int i = 1; i <= m; i++){
            int u = in.nextInt();
            int v = in.nextInt();
            map[u].add(v); 
            map[v].add(u);
            d.merge(u,v);
       }
       
       for(int i = 1; i <= n; i++){
          if(visited[i] == 0){
              int p = d.find(i);
              int[] dia = getDiameter(p);
              d.size[p] = Math.max(dia[0] - 1, dia[1] - 1); 
          }
       }

       for(int i = 1; i <= q; i++){

          int t = in.nextInt();
          if(t == 1){

            int u = in.nextInt();
            out.println(d.size[d.find(u)]);

          }else if(t == 2){

            int u = in.nextInt();
            int v = in.nextInt();
            d.union(u, v);

          }

       }

    }


    FastScanner in;
    PrintWriter out;
    
    static class FastScanner {
 
        BufferedReader br;
        StringTokenizer st;
 
        FastScanner(InputStream in) {
            br = new BufferedReader(new InputStreamReader(in));
            st = null;
        }
 
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
 
        String nextLine() throws IOException {
            if (st == null || !st.hasMoreTokens())
                return br.readLine();
            StringBuilder result = new StringBuilder(st.nextToken());
            while (st.hasMoreTokens()) {
                result.append(" ");
                result.append(st.nextToken());
            }
            return result.toString();
        }
 
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
 
        long nextLong() throws IOException {
            return Long.parseLong(next());
        }
 
        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
 
    }
 
    void run() throws IOException {
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out, false);
        solve();
        out.close();
    }
 
    public static void main(String[] args) throws IOException{
        new Main().run();
    }
 
    public void printArr(int[] arr){
        for(int i = 0; i < arr.length; i++){
            out.print(arr[i] + " ");
        }
        out.println();
    }
 
    public long gcd(long a, long b){
        if(a == 0) return b;
        return gcd(b % a, a);
    }

    public boolean isPrime(long num){

        if(num == 0 || num == 1){
            return false;
        }

        for(int i = 2; i * i <= num; i++){
            if(num % i == 0){
                return false;
            }
        }

        return true;
    }

    public class Pair<A, B>{
        public A x; 
        public B y;

        Pair(A x, B y){
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair<?, ?> pair = (Pair<?, ?>) o;
            if (!x.equals(pair.x)) return false;
            return y.equals(pair.y);
        }

        @Override
        public int hashCode() {
            int result = x.hashCode();
            result = 31 * result + y.hashCode();
            return result;
        }

    }

    class Tuple{
        int x; int y; int z;
        Tuple(int ix, int iy, int iz){
            x = ix;
            y = iy;
            z = iz;
        }
    }
}
