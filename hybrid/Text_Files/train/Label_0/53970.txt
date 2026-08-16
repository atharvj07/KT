import java.io.*; import java.util.*;
public class VillageMin {
    static ArrayList<Integer>[] arl;
    static ArrayList<Integer> swaps;//Used to track parent of leaf
    static long[] dp,dp1;
    static int[] ans, res;
    public static void main(String[] args) throws IOException {
         BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
         int N=Integer.parseInt(br.readLine());
         
         arl=new ArrayList[N];
         for (int i = 0; i < N; i++) {
            arl[i]=new ArrayList<>();
        }
         int a,b;
         for (int i = 0; i < N-1; i++) {
            StringTokenizer st=new StringTokenizer(br.readLine());
            a=Integer.parseInt(st.nextToken())-1;
            b=Integer.parseInt(st.nextToken())-1;
            arl[a].add(b); arl[b].add(a);
        }
         dp=new long[N]; dp1=new long[N];
         ans=new int[N]; res=new int[N];
         for (int i = 0; i < N; i++) {
            res[i]=i;
        }
         if(N==2){
             System.out.println("2");
             System.out.println("2 1"); return;
         }
         int rt=0;
         while(arl[rt].size()==1){
             rt++;
         }
         swaps=new ArrayList<>();
         comp(-1,rt); fill(-1,rt);
         for (int i = 0; i < swaps.size(); i+=2) {
             if(res[swaps.get(i)]==swaps.get(i) || res[swaps.get(i+1)]==swaps.get(i+1)){//In case I get parent -> leaf
                res[swaps.get(i)]+=res[swaps.get(i+1)];
                res[swaps.get(i+1)]=res[swaps.get(i)]-res[swaps.get(i+1)];
                res[swaps.get(i)]-=res[swaps.get(i+1)];
             }
         }
         //System.out.println(Arrays.toString(ans));
         //System.out.println(Arrays.toString(dp));
         //System.out.println(Arrays.toString(dp1));
         StringBuilder sb=new StringBuilder();
         sb.append(dp[rt]).append("\n");
         for (int i = 0; i < N; i++) {
            sb.append(res[i]+1).append(" ");
        }
        System.out.println(sb.toString());
    }
    public static void comp(int p, int v){
        //If it is a leaf, return 0
        long max=0;
        
        int cnt=0; int ind=-1;
        for (int u:arl[v]) {
            if(u==p)continue;
            comp(v,u);
            dp1[v]+=Math.max(2,dp[u]);//Deals with leaf case
            
            if(dp[u]-dp1[u]>max){
                
                max=dp[u]-dp1[u]; ind=u;
                
            }else if(dp[u]-dp1[u]==max && (arl[u].size()==1 || ind==-1)){
                ind=u;
            }
            dp[v]+=dp[u];
        }
        dp[v]-=max; dp[v]+=2;
        ans[v]=ind;//What to dp1 on
        
    }
    public static void fill(int p, int v){
        if(arl[v].size()==1 && p>=0){
            swaps.add(p); swaps.add(v);
        }
        ArrayList<Integer> leaves=new ArrayList<>();
        for (int i : arl[v]) {
            if(i==p)continue;
            if(i==ans[v]){
                for (int j : arl[i]) {
                    if(j==v)continue;
                    fill(i,j);
                }
                if(arl[i].size()==1){
                    leaves.add(i);
                }
                res[i]=v; res[v]=i;
                continue;
            }
            if(arl[i].size()>1){//Not a leaf
                fill(v,i);
            }else{
                leaves.add(i);
            }
            
        }
        int size=leaves.size();
        if(size>=2){
            for (int i = 0; i < size-1; i+=2) {
                res[leaves.get(i)]+=res[leaves.get(i+1)];
                res[leaves.get(i+1)]=res[leaves.get(i)]-res[leaves.get(i+1)];
                res[leaves.get(i)]-=res[leaves.get(i+1)];
            }
            if(size%2==1){
                res[leaves.get(0)]+=res[leaves.get(size-1)];
                res[leaves.get(size-1)]=res[leaves.get(0)]-res[leaves.get(size-1)];
                res[leaves.get(0)]-=res[leaves.get(size-1)];
            }
        }
        
    }
}
