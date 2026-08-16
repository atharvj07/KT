import java.util.*;
import java.util.Map.Entry;
import java.util.regex.Pattern;
import java.lang.*;
import java.io.*;

public class sample2{
     static class FastReader  {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() { return Integer.parseInt(next()); }
 
        long nextLong() { return Long.parseLong(next()); }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine()
        {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
 
    public static void main(String[] args)
    {
        FastReader sc = new FastReader();
        int n = sc.nextInt(), m = sc.nextInt();
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < n; i++) set.add(sc.nextInt());
        int sum = 0, cnt = 0;
        StringBuilder s = new StringBuilder();
        int index = 1;
        while(sum <= m){
            if(!set.contains(index)){
                sum += index;
                if(sum > m) break;
                cnt++;
                s.append(index + " ");
            }
            index++;
        }
        System.out.println(cnt);
        System.out.println(s);
    }
}