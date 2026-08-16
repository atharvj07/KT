import java.util.*;
import java.io.*;
import java.lang.*;
import java.math.*;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        // Scanner scan = new Scanner(System.in);
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(bf.readLine());
        if(n == 3) {
          out.println("2 5 63");
        }
        else if(n == 4) {
          out.println("2 5 20 63");
        }
        else {
          Set<Integer> s = new HashSet<Integer>();
          for(int i=2; i<=n/4*6; i+=2) s.add(i);
          for(int i=3; i<=n/4*6; i+=3) s.add(i);
          if(n % 4 == 0) {
            if(n/4 % 2 == 1) {
              s.add(29997);
              s.remove(6);
            }
          }
          if(n % 4 == 1) {
            if(n/4 % 2 == 1) {
              s.add(29997);
            }
            else {
              s.add(30000);
            }
          }
          else if(n % 4 == 2) {
            if(n/4 % 2 == 1) {
              s.add(29997);
              s.add(30000);
            }
            else {
              s.add(29996);
              s.add(29998);
            }
          }
          else if(n % 4 == 3) {
            if(n/4 % 2 == 1) {
              s.add(29997);
              s.add(29996);
              s.add(29998);
            }
            else {
              s.add(29996);
              s.add(29998);
              s.add(30000);
            }
          }
          long sum = 0;
          StringBuilder sb = new StringBuilder();
          for(int i : s) {
            sb.append(i + " ");
            sum += i;
            sum %= 6;
          }
          out.println(sb.toString());
          if((s.size() != n)  || (sum % 6 != 0)) {
            //out.println(1/0);
          }
        }
        // StringTokenizer st = new StringTokenizer(bf.readLine());
        // int[] a = new int[n];
        // for(int i=0; i<n; i++) a[i] =  Integer.parseInt(st.nextToken());

        out.close(); System.exit(0);
    }


}
