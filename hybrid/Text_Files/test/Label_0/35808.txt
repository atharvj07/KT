

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Hamburgers {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
    private static int gcd(int a , int b){
        return (a%b==0)?b:gcd(b,a%b);
    }

    private static int primes(int a){
        int ct=0;
        while (a % 2 == 0)
        {
            ct++;
            a = a/2;
        }
        while (a % 3 == 0)
        {
            ct++;
            a = a/3;
        }
        while (a % 5 == 0)
        {
            ct++;
            a = a/5;
        }
        if(a==1) return ct;
        return -1;

    }
    static List<Long> ls=new ArrayList<Long>();

    private static void rec(long num,int ct4,int ct7){
        if(num>=(long)1e10)
            return;
        if(ct4==ct7)
            ls.add(num);
        rec(num*10+4,ct4+1,ct7);
        rec(num*10+7,ct4,ct7+1);
    }


    public static void main(String[] args){
       // Scanner in=new Scanner(System.in);
         FastReader in= new FastReader();
         int n=in.nextInt();
         rec(0,0,0);
         Collections.sort(ls);


          int l=0;
          int r=ls.size();
          while(l<r){
              int mid=l+(r-l)/2;
              if(ls.get(mid)>n)
                  r=mid;
              else
                  l=mid+1;
          }
          if(l==0)
              System.out.println(l);
          else if(ls.get(l-1)==n)
              System.out.println(ls.get(l-1));
          else System.out.println(ls.get(l));

    }

}
