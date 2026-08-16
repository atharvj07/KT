import java.io.BufferedReader;
import java.io.InputStreamReader;


public class m6 {
    static String s;
    static int n;
    static long DP[][][];
    public static long call(int ind , int prev , int flag) {
        if(ind==n && flag==0)
            return 1;
        if(ind==n)
            return 0;
        if(DP[ind][prev][flag]!=-1)
            return DP[ind][prev][flag];
        int a = s.charAt(ind)-'0';
        int sum = a + prev;
        if(sum%2 == 0) {
            int dig = sum/2;
            if(dig != (s.charAt(ind)-'0') && flag==1)
                flag = 0;
            return DP[ind][prev][flag] = call(ind+1,dig,flag);
        }else {
            int dig1 = sum/2;
            int dig2 = (sum/2) + 1;
            int flag1 = flag;
            int flag2 = flag;
            long res = 0;
            if(dig1 != (s.charAt(ind)-'0') && flag1==1)
                flag1 = 0;
            res += call(ind+1,dig1,flag1);
            if(dig2 != (s.charAt(ind)-'0') && flag2==1)
                flag2 = 0;
            res += call(ind+1,dig2,flag2);
            return DP[ind][prev][flag] = res;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        s = in.readLine();
        n = s.length();
        DP = new long [n][10][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                for (int j2 = 0; j2 < 2; j2++) {
                    DP[i][j][j2] = -1;
                }
            }
        }
        long res = 0;
        for (int i = 0; i < 10; i++) {
            if(i==(s.charAt(0)-'0'))
            res += call(1,i,1);
            else
            res += call(1,i,0);
        }
        System.out.println(res);
    }
}
