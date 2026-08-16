import java.io.*;
import java.util.*;

public class B {
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

    static FastReader s = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    private static int[] rai(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = s.nextInt();
        }
        return arr;
    }

    private static int[][] rai(int n, int m) {
        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = s.nextInt();
            }
        }
        return arr;
    }

    private static long[] ral(int n) {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = s.nextLong();
        }
        return arr;
    }

    private static long[][] ral(int n, int m) {
        long[][] arr = new long[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = s.nextLong();
            }
        }
        return arr;
    }

    private static int ri() {
        return s.nextInt();
    }

    private static long rl() {
        return s.nextLong();
    }

    private static String rs() {
        return s.next();
    }

    static int gcd(int a,int b)
    {
        if(b==0)
        {
            return a;
        }
        return gcd(b,a%b);
    }

    static long gcd(long a,long b)
    {
        if(b==0)
        {
            return a;
        }
        return gcd(b,a%b);
    }
    static boolean isPrime(int n) {
        //check if n is a multiple of 2
        if(n==1)
        {
            return false;
        }
        if(n==2)
        {
            return true;
        }
        if (n % 2 == 0) return false;
        //if not, then just check the odds
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
    static boolean[] sieveOfEratosthenes(int n)
    {
        // Create a boolean array "prime[0..n]" and initialize
        // all entries it as true. A value in prime[i] will
        // finally be false if i is Not a prime, else true.
        boolean prime[] = new boolean[n+1];
        for(int i=0;i<n;i++)
            prime[i] = true;

        for(int p = 2; p*p <=n; p++)
        {
            // If prime[p] is not changed, then it is a prime
            if(prime[p] == true)
            {
                // Update all multiples of p
                for(int i = p*p; i <= n; i += p)
                    prime[i] = false;
            }
        }
        return prime;
    }


    public static void main(String[] args) {
        StringBuilder ans = new StringBuilder();
        int t = ri();
//        int t=1;
        while (t-- > 0)
        {
            int n=ri();
            long[] arr=ral(n);
            if(n==1)
            {
                ans.append("0\n");
                continue;
            }

            long maxPrime = 1999999817;
//            int ind = -1;
//            long min = Long.MAX_VALUE;
//            for(int i=0;i<n;i++)
//            {
//                if(arr[i]<min)
//                {
//                    min = arr[i];
//                    ind = i;
//                }
//            }

            int count = 0;
            StringBuilder mid = new StringBuilder();
            long val = 1000000000;

            for(int i=0;i<n-2;i++)
            {
                long min = Math.min(arr[i],arr[i+1]);

                count++;
                arr[i] = val;
                arr[i+1] = min;

                mid.append(i + 1).append(" ").append(i + 2).append(" ").append(val).append(" ").append(min).append("\n");
                val++;




//                if(arr[i]<=arr[i+1]) {
//
//                    count++;
//
//                    mid.append(i + 1).append(" ").append(i + 2).append(" ").append(arr[i]).append(" ").append(arr[i] + 1).append("\n");
//                    arr[i + 1] = arr[i] + 1;
//                }
//                else
//                {
//
//                    if(gcd(arr[i],arr[i+1])==1)
//                    {
//                        continue;
//                    }
//                    count++;
//                    arr[i]=arr[i+1];
//                    arr[i+1] = arr[i]+1;
//                    mid.append(i+1).append(" ").append(i+2).append(" ").append(arr[i]).append(" ").append(arr[i+1]).append("\n");
//                }


            }
            count++;
            long min = Math.min(arr[n-2],arr[n-1]);
            arr[n-2] = maxPrime;
            arr[n-1] = min;
            mid.append(n-1).append(" ").append(n).append(" ").append(maxPrime).append(" ").append(min).append("\n");

//            for(int i=1;i<n;i++)
//            {
//                if(gcd(arr[i],arr[i-1])!=1)
//                {
//                    System.out.println("false");
//                    break;
//                }
//            }

//            System.out.println(Arrays.toString(arr));
            ans.append(count).append("\n");
            ans.append(mid.toString());
        }
        out.print(ans.toString());
        out.flush();

    }


}
