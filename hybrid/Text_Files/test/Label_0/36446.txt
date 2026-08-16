import java.util.Scanner;

public class Main {
//    public String getSolution(long p, long q, long b){
//        BigDecimal bdp = new BigDecimal(p);
//        BigDecimal bdq = new BigDecimal(q);
//        BigDecimal bdb = new BigDecimal(b);
//
//        Set<BigDecimal> set = new HashSet<>();
//
//        while(!bdp.equals(new BigDecimal(0))){
//            bdp = bdp.remainder(bdq);
//            if(set.contains(bdp)) return "Infinite";
//
//            set.add(bdp);
//            bdp = bdp.multiply(bdb);
//        }
//
//        return "Finite";
//    }
    public static void main(String[] arg) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] packets = new int[n];
        for(int i = 0; i < n; i++){
            packets[i] = scan.nextInt();
        }

        if(n < 2) {
            System.out.println("-1");
            return;
        }
        if(n == 2 && packets[0] == packets[1]) {
            System.out.println("-1");
            return;
        }

        int minIndex = 0;
        for(int i = 0; i < n; i++)
            if(packets[minIndex] > packets[i])
                minIndex = i;

        System.out.println(n - 1);
        for(int i = 0; i < n; i++){
            if(minIndex != i)
                System.out.print((i + 1) + " ");
        }


    }
}