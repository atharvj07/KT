
import java.io.*;
import java.util.*;
import java.math.*;
 
public class D { 
    
    static boolean ONLINE_JUDGE = false;//change before submit
    static Fast f = new Fast();
    static PrintWriter out = new PrintWriter(System.out); 
    static boolean TEST_CASES = false;
    
    
    static void solve(int TC_NO) {

      int n = ri(), m = ri();
      int[] p = ra(n);


      DSU dsu = new DSU(n);

      for(int i = 0; i < m; i++){
         int x = ri()-1;
         int y = ri()-1;
         dsu.union(x,y);
      }

      int[] ans = new int[n];
      ArrayList<ArrayList<Integer>> grps = dsu.groups();

      ArrayList<Integer> l,x;

      for(int i = 0; i < grps.size(); i++){
      	l = new ArrayList<>();
      	x = new ArrayList<>();
      	for(int j = 0; j < grps.get(i).size(); j++){
      		x.add(grps.get(i).get(j));
      		l.add(p[grps.get(i).get(j)]);
      	}

      	Collections.sort(x);
      	Collections.sort(l);

        for(int j = 0; j < x.size(); j++){
        	ans[x.get(j)] = l.get(l.size()-j-1);
        }
      }


      for(int i = 0; i<n; i++) out.print(ans[i]+" ");

      	out.println();

      /*-----WARNING : change [ONLINE_JUDGE = false] before SUBMIT-----*/ 
    }


    static class DSU
{
   private int[] parent;
   private int[] size;
   private ArrayList<ArrayList<Integer>> grp;

   public DSU(int n){
    parent = new int[n];
    size = new int[n];
      for (int i = 0; i < n; i++) {
         parent[i] = i;
         size[i] = 1;
      }
   }


  public void union(int a,int b){
    int p = find(a);
    int q = find(b);
    if (p != q) {
      parent[q] = p;
      size[p]+=size[q];
    }
  }

  public  int find(int a){
      if(a == parent[a]){
         return a;
      }
      else{
      return parent[a] = find(parent[a]);
      }
  }

  public boolean isConnected(int a, int b){
    return find(a) == find(b);
  }

  public int size(int a){
       return size[find(a)];
  }

  public ArrayList<ArrayList<Integer>> groups(){
      grp = new ArrayList<>();
      int hash[] = new int[parent.length];
      Arrays.fill(hash,-1);

      for (int i = 0; i < parent.length; i++) {
        int par = find(i);
        if(hash[par] == -1){
          ArrayList<Integer> cur = new ArrayList<Integer>();
          hash[par] = grp.size();
          cur.add(i);
          grp.add(cur);
          continue;
        }
        grp.get(hash[par]).add(i);
      }
      return grp;
  }

  public int components(){
    return grp.size();
  }
}

    
    public static void main(String[] args)throws Exception{

      out = ONLINE_JUDGE? new PrintWriter(new BufferedWriter(new FileWriter("output.txt"))): new PrintWriter(System.out);
      

     
      if(TEST_CASES){
          
          int t = ri();
          int i = 1;
          while(i<=t){
            solve(i);
            i++;
          }

      }

      else {

        solve(1);
      
      }
      
      out.close();

    }

    static int ri() {

      return f.nextInt();
    
    }

    static long rl() {
 
      return f.nextLong();
    
    }

    static double rd() {

       return f.nextDouble();
    
    }

    static char rc() {
      
       return rs().charAt(0);

    }

    static String rs() {

      return f.next();

    }

    static String rS() {
      
       return f.nextLine();
    
    }

    static int[] ra(int n) {
        
      int[] a = new int[n];
      for(int i = 0;i<n;i++) a[i] = ri();
      return a;
        
    }

    static long[] ral(int n) {
        
      long[] a = new long[n];
      for(int i = 0;i<n;i++) a[i] = rl();
      return a;
        
    }

    static double[] rad(int n) {

      double[] a = new double[n];
      for(int i = 0;i<n;i++) a[i] = rd();
      return a;

    }

    static char[] rac() {

        char[] c = rs().toCharArray();

        return c;

    }
    
    static int[][] rm(int n, int m) {
       
       int[][] mat = new int[n][m];

       for(int i = 0; i < n; i++) mat[i] = ra(m);
       
       return mat;

    }

    static char[][] rmc(int n) {
      
      char[][] cmat = new char[n][];
      
      for(int i = 0; i < n; i++) cmat[i] = rac();

      return cmat;

    }

    static void sort(int[] a) {

      ArrayList<Integer> list=new ArrayList<>();
      for (int i:a) list.add(i);
      Collections.sort(list);
      for (int i=0; i<a.length; i++) a[i]=list.get(i);

    }

    static String gcc(int TC_NO) {

         return "Case #"+TC_NO+": ";

    }

    static boolean isLetter(char c){

      return (64<c && c<91) || (96<c && c<123);
    
    }
  
    static class Fast{

       public BufferedReader br;
       public StringTokenizer st;
       
       public Fast(){
            try{
                br = ONLINE_JUDGE? (new BufferedReader(new FileReader("input.txt"))):(new BufferedReader(new InputStreamReader(System.in)));
            }
            catch(Exception e){
              throw new RuntimeException(e);
            }
       }
       
       String next(){
            while(st==null || !st.hasMoreTokens()){
                 try{
                      st=new StringTokenizer(br.readLine());
                 }
                 catch(IOException e){
                      throw new RuntimeException(e);
                 }
                 
            }
                 return st.nextToken();
            }
       int nextInt(){
            return Integer.parseInt(next());
       }
   
       long nextLong(){
            return Long.parseLong(next());
       }
   
       double nextDouble(){
            return Double.parseDouble(next());
       }

       String nextLine() 
          { 
              String str = ""; 
              try
              { 
                  str = br.readLine(); 
              } 
              catch (IOException e) 
              { 
                  e.printStackTrace(); 
              } 
              return str; 
          } 
   
    }

}


