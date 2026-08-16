import java.io.*;
import java.util.*;
public class C{
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
            int n;
            int a[],p[];
            boolean visit[];
            int cnt[]=new int[5];
            int ans=0;
            ArrayDeque<Integer> cy=new ArrayDeque<>();
            ArrayList<Integer[]> g=new ArrayList();
            ArrayList<Integer[]> gg[]=new ArrayList[5];
            void add(int ...v){
                if(v.length==1){
                    int L=gg[v[0]].size();
                    Integer x[]=gg[v[0]].get(L-1);
                    Integer add[]=new Integer[2*x.length];
                    for(int i=0;i<x.length;i++){
                        add[i]=x[i];
                    }
                    for(int i=x.length;i<2*x.length;i++){
                        add[i]=x[(i-x.length+1)%x.length];
                    }
                    g.add(add);
                    gg[v[0]].remove(gg[v[0]].size()-1);
                }else{
                    // System.out.println(v[0]+" "+v[1]);
                    int L1=gg[v[0]].size(),L2=gg[v[1]].size()+(v[0]==v[1]?-1:0);
                    Integer x[]=gg[v[0]].get(L1-1);
                    Integer y[]=gg[v[1]].get(L2-1);
                    int L=x.length+y.length;
                    int sz=Math.min(L,5);
                    Integer add[]=new Integer[2*sz];
                    for(int i=0;i<x.length;i++){
                        add[i]=x[i];
                    }
                    for(int i=sz;i<sz+x.length;i++){
                        add[i]=x[(i-sz+1)%x.length];
                    }
                    for(int i=x.length;i<sz;i++){
                        add[i]=y[i-x.length];
                    }
                    for(int i=sz+x.length;i<2*sz;i++){
                        add[i]=y[(i-sz-x.length+1)%(sz-x.length)];
                    }
                    gg[v[0]].remove(gg[v[0]].size()-1);
                    gg[v[1]].remove(gg[v[1]].size()-1);
                    g.add(add);
                    if(sz<x.length+y.length){
                        Integer z[]=new Integer[L-sz+1];
                        z[0]=y[0];
                        for(int i=1;i<z.length;i++){
                            z[i]=y[sz-x.length-1+i];
                        }
                        gg[z.length].add(z);
                    }
                }
            }
           public void solve(int testNumber, InputReader in, PrintWriter out) {
            for(int i=0;i<5;i++)gg[i]=new ArrayList<>();
            
            n=in.nextInt();
            a=new int[n+1];p=new int[n+1];
            visit=new boolean[n+1];
            
            for(int i=1;i<=n;i++)p[a[i]=in.nextInt()]=i;
            
            for(int i=1;i<=n;i++){
                if(visit[i])continue;
                int sz=0;
                int x=i;
                cy.clear();
                while(!visit[x]){
                    // System.out.print(x+" ");
                    cy.addLast(p[x]);
                    visit[x]=true;++sz;
                    x=a[x];
                }
                // System.out.println();
                while(sz>=5){
                    Integer A[]=new Integer[10];
                    for(int j=0;j<5;j++){
                        A[j]=cy.pollFirst();
                    }
                    for(int j=5;j<10;j++){
                        A[j]=A[(j-4)%5];
                    }
                    cy.addFirst(A[0]);g.add(A);
                    ans++;sz-=4;
                }
                Integer B[]=new Integer[sz];
                for(int j=0;j<sz;j++){
                    B[j]=cy.pollFirst();
                }
                gg[sz].add(B);
                cnt[sz]++;
            }
            
            for(int i=0;i<cnt[4];i++){
                add(4);
            }
            ans+=cnt[4];
            
            if(cnt[2]>cnt[3]){
                ans+=cnt[3];
                for(int i=0;i<cnt[3];i++){
                    add(2,3);
                }
                cnt[2]-=cnt[3];
                for(int i=0;cnt[2]>1;i+=2){
                    add(2,2);
                    cnt[2]-=2;
                    ans++;
                }
                if(cnt[2]==1){
                    add(2);
                }
                ans+=cnt[2];
            }else if(cnt[3]>cnt[2]){
                ans+=cnt[2];
                for(int i=0;i<cnt[2];i++){
                    add(2,3);
                }
                cnt[3]-=cnt[2];
                for(int i=0;cnt[3]>2;i+=3){
                    add(3,3);
                    add(2,3);
                    cnt[3]-=3;
                    ans+=2;
                }
                if(cnt[3]==1){
                    add(3);
                }else if(cnt[3]==2){
                    add(3,3);
                    add(2);
                }
                ans+=cnt[3];
            }else{
                for(int i=0;i<cnt[2];i++){
                    add(2,3);
                }
                ans+=cnt[2];
            }
            out.println(ans);
            for(int i=0;i<g.size();i++){
                Integer X[]=g.get(i);
                out.println(X.length/2);
                for(int j=0;j<X.length;j++){
                    if(j==X.length/2)out.println();
                    out.print(X[j]+" ");
                }
                out.println();
            }
          }
//         pair ja[][];long w[];int from[],to[],c[];
//             void make(int n,int m,InputReader in){
//              ja=new pair[n+1][];w=new long[m];from=new int[m];to=new int[m];c=new int[n+1];
//              for(int i=0;i<m;i++){
//               int u=in.nextInt(),v=in.nextInt();long wt=in.nextLong();
//               c[u]++;c[v]++;from[i]=u;to[i]=v;w[i]=wt;
//              }
//              for(int i=1;i<=n;i++){
//               ja[i]=new pair[c[i]];c[i]=0;
//              }
//              for(int i=0;i<m;i++){
//               ja[from[i]][c[from[i]]++]=new pair(to[i],w[i]);
//               ja[to[i]][c[to[i]]++]=new pair(from[i],w[i]);
//              }
//             }
//        int[] radixSort(int[] f){ return radixSort(f, f.length); }
//    int[] radixSort(int[] f, int n)
//    {
//        int[] to = new int[n];
//        {
//            int[] b = new int[65537];
//            for(int i = 0;i < n;i++)b[1+(f[i]&0xffff)]++;
//            for(int i = 1;i <= 65536;i++)b[i]+=b[i-1];
//            for(int i = 0;i < n;i++)to[b[f[i]&0xffff]++] = f[i];
//            int[] d = f; f = to;to = d;
//        }
//        {
//            int[] b = new int[65537];
//            for(int i = 0;i < n;i++)b[1+(f[i]>>>16)]++;
//            for(int i = 1;i <= 65536;i++)b[i]+=b[i-1];
//            for(int i = 0;i < n;i++)to[b[f[i]>>>16]++] = f[i];
//            int[] d = f; f = to;to = d;
//        }
//        return f;
//    }
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