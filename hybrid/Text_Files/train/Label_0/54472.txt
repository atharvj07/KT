import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner();
        HashMap<Integer,Long> map=new HashMap<>();
        int n = Integer.parseInt(sc.next());
        long der=0; long izq=0;
        for (int i = 0; i < n; i++) {
            String s=sc.next();
            int x=Integer.parseInt(sc.next());
            if(i==0){
                map.put(x, izq);
            }else{
                if(s.equals("L")){
                    izq--;
                    map.put(x, izq);
                }else if(s.equals("R")){
                    der++;
                    map.put(x, der);
                }else{
                    long w=map.get(x);
                    System.out.println(Math.min(Math.abs(der-w),Math.abs(izq-w)));
                }
            }
        }
        
        
        
        
    }
    

    static class Scanner {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer("");

        int spaces = 0;

        public String nextLine() throws IOException {

            if (spaces-- > 0) {

                return "";

            } else if (st.hasMoreTokens()) {

                return new StringBuilder(st.nextToken("\n")).toString();

            }

            return br.readLine();

        }

        public String next() throws IOException {

            spaces = 0;

            while (!st.hasMoreTokens()) {

                st = new StringTokenizer(br.readLine());

            }

            return st.nextToken();

        }

        public boolean hasNext() throws IOException {

            while (!st.hasMoreTokens()) {

                String line = br.readLine();

                if (line == null) {

                    return false;

                }

                if (line.equals("")) {

                    spaces = Math.max(spaces, 0) + 1;

                }

                st = new StringTokenizer(line);

            }

            return true;

        }

    }

}