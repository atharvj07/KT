import java.io.*;
import java.util.*;
 
 
public class Main{
static int mod = (int)(Math.pow(10, 9) + 7);
   public static void main(String[] args) {
      MyScanner sc = new MyScanner();
      out = new PrintWriter(new BufferedOutputStream(System.out));
      int n = sc.nextInt();
      int k = sc.nextInt();
      if (n <= 2) out.println(0);
      else{
                    char[][] ch = new char[n][k];
                    long total = 0;
            HashSet<String> set = new HashSet<String>();
            String[] str = new String[n];
          for (int i = 0; i < n; i++){
              String s = sc.next();
              str[i] = s;
              set.add(s);
              ch[i] = s.toCharArray();
          }
          
          for (int i = 0; i < n; i++){
              for (int j = i+1; j < n; j++){
                  String s = "";
                    for (int m = 0; m < k; m++){
                        if (ch[i][m] == ch[j][m]) s += ch[i][m];
                        else{
                            if (ch[i][m] + ch[j][m] == 'S' + 'T'){
                                s += 'E';
                            }
                            if (ch[i][m] + ch[j][m] == 'E' + 'T'){
                                s += 'S';
                            }
                            if (ch[i][m] + ch[j][m] == 'S' + 'E'){
                                s += 'T';
                            }
                        }
                    }
                    
                    if (set.contains(s)) {
                        total++;
                       // out.println(s + " " + i + " " + j);
                    }
              }
              set.remove(str[i]);
          }
          out.println(total/2) ;
          
      }
      
      out.close();
   }
   
   static long pow(long a, long N) {
	   if (N == 0) return 1;
	   else if (N == 1) return a;
	   else {
		   long R = pow(a,N/2);
		   if (N % 2 == 0) {
			   return R*R;
		   }
		   else {
			   return R*R*a;
		   }
	   }
   }
   
   static long powMod(long a, long N) {
	   if (N == 0) return 1;
	   else if (N == 1) return a % mod;
	   else {
		   long R = powMod(a,N/2) % mod;
		   R *= R % mod;
		   if (N % 2 == 1) {
			   R *= a % mod;
		   }
			   return R % mod;
	   }
   }
static void mergeSort(int[] A){ // low to hi sort, single array only
      int n = A.length;
      if (n < 2) return;
      int[] l = new int[n/2];
      int[] r = new int[n - n/2];
 
      for (int i = 0; i < n/2; i++){
        l[i] = A[i];
      }
 
      for (int j = n/2; j < n; j++){
        r[j-n/2] = A[j];
      }
 
      mergeSort(l);
      mergeSort(r);
      merge(l, r, A);
    }
 
    static void merge(int[] l, int[] r, int[] a){
      int i = 0, j = 0, k = 0;
      while (i < l.length && j < r.length && k < a.length){
        if (l[i] < r[j]){
          a[k] = l[i];
          i++;
        }
        else{
          a[k] = r[j];
          j++;
        }
        k++;
      }
      while (i < l.length){
        a[k] = l[i];
        i++;
        k++;
      }
 
      while (j < r.length){
        a[k] = r[j];
        j++;
        k++;
      }
    }

   

   //-----------PrintWriter for faster output---------------------------------
   public static PrintWriter out;
      
   //-----------MyScanner class for faster input----------
   public static class MyScanner {
      BufferedReader br;
      StringTokenizer st;
 
      public MyScanner() {
         br = new BufferedReader(new InputStreamReader(System.in));
      }
 
      String next() {
          while (st == null || !st.hasMoreElements()) {
              try {
                  st = new StringTokenizer(br.readLine());
              } catch (IOException e) {
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
 
      String nextLine(){
          String str = "";
	  try {
	     str = br.readLine();
	  } catch (IOException e) {
	     e.printStackTrace();
	  }
	  return str;
      }

   }
   //--------------------------------------------------------
}





