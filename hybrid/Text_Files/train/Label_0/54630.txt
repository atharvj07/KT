import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

/**
 * Created by Pranav ps on 06-09-2017.
 */
public class ArpaAndGame {
    private static HashSet<Integer> primes;
    private static HashMap<Integer,Integer> grundy;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        primes = new HashSet<>();
        grundy = new HashMap<>();
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            deal(arr[i]);
        }

        int res = 0;
        for(int p: primes){
            int local = 0;
            for (int i = 0; i < n; i++) {
                int k = 0;
                while(arr[i]%p==0) {
                    k++;
                    arr[i]/=p;
                }
                local |= 1<<k;
            }
            res^=f(local);
        }
        if(res==0)
            System.out.println("Arpa");
        else
            System.out.println("Mojtaba");
    }

    private static int f(int n) {
        if(grundy.containsKey(n))
            return grundy.get(n);

        if(n==1){
            grundy.put(n,0);
            return 0;
        }

        HashSet<Integer> toMex = new HashSet<>();

        for(int i = 1; (n>>i) > 0; i++){
            toMex.add(f((n>>i)|(n&((1<<i) - 1))));
        }

        grundy.put(n,mex(toMex));
        return grundy.get(n);

    }

    private static Integer mex(HashSet<Integer> toMex) {
        int i = 0;
        while(true){
            if(!toMex.contains(i))
                return i;
            i++;
        }
    }

    private static void deal(int num) {
        int numC = num;
        for(int p = 2; p*p <= numC; p++){
            if(num%p == 0)
                primes.add(p);
            while(num%p == 0)
                num/=p;
        }
        if(num!=1)
            primes.add(num);
    }
}
