import java.util.*;

public class Great_Graphs {
    public static void main(String[] args) throws java.lang.Exception{
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for(int i=0;i<t;i++){
            int n = input.nextInt();
            Long[] d = new Long[n];
            for(int j=0;j<n;j++){
                d[j] = input.nextLong();
            }
            Arrays.sort(d);
            long[] prefsum = new long[n];
            prefsum[0] = d[0];
            for(int j=1;j<n;j++){
                prefsum[j] = prefsum[j-1]+d[j];
            }

            if(n<=2){
                System.out.println(0);
                continue;
            }
            long ans = 0;
            long mul = 1;
            for(int j=2;j<n;j++){
                ans += (mul*d[j])-prefsum[j-2];
                mul++;
            }
            ans = -ans;
            System.out.println(ans);
        }
    }
}
