    import java.util.*;
    import java.io.*;
    public class C{
    	public static void main(String[] args) {
    		MyScanner scan = new MyScanner();
            PrintWriter pw = new PrintWriter(System.out);
            int n = scan.nextInt();
            long sum1 = 0,sum2 = 0;
            for(int i = 0;i < n;i++)
                sum1+=scan.nextInt();
            for(int i = 0;i < n;i++)
                sum2+=scan.nextInt();
            if(sum2 <= sum1)
                System.out.println("Yes");
            else
                System.out.println("No");
            pw.close();
     	}
    }



    //-------------------------------------------------------------------------------------------------------
    class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public int mod(long x) {
            // TODO Auto-generated method stub
            return (int) x % 1000000007;
        }

        public int mod(int x) {
            return x % 1000000007;
        }

        boolean hasNext() {
            if (st.hasMoreElements())
                return true;
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
            return st.hasMoreTokens();
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
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
