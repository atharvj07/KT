import java.util.*;
import java.io.*;
import java.math.*;
public class Apples{
    public static void main(String[] args) {
        MyScanner sc=new MyScanner();
        int n=sc.nextInt();
        ArrayList<Integer> lefts=new ArrayList<>();
        ArrayList<Integer> rights=new ArrayList<>();
        HashMap<Integer,Integer> hs=new HashMap<>();
        for(int i=0;i<n;i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            if(x<0) lefts.add(x);
            else if(x>0) rights.add(x);
            hs.put(x,y);
        }
        int ans=0;
        int ls=lefts.size(),rs=rights.size();
        Comparator cm=Collections.reverseOrder();   
        lefts.sort(cm);
        rights.sort(null);     
        if(ls!=0 && rs!=0){
            int steps=Math.min(ls,rs);
            for(int i=0;i<steps;i++){
                ans+=hs.get(lefts.get(i));
                ans+=hs.get(rights.get(i));
            }
            if(ls>rs) ans+=hs.get(lefts.get(steps));
            else if(rs>ls) ans+=hs.get(rights.get(steps));
        }
        else if(ls==0){
            ans=hs.get(rights.get(0));
        }
        else{
            ans=hs.get(lefts.get(0));
        }
        System.out.println(ans);
    }


    private static class MyScanner {
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
}