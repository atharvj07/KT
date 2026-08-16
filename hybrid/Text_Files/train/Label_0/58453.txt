import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        long[] times = new long[n];
        for (int i = 0; i < n; i++) {
            times[i] = sc.nextLong();
        }
        ArrayList<Long> arrayList = new ArrayList<>();
        for (int i = 0; i < n-1; i++) {
            long l = times[i+1] - (times[i] + 1);
            if(l > 0) arrayList.add(l);
        }
        arrayList.sort(Comparator.reverseOrder());

//        System.out.println("forEach");
//        arrayList.forEach(System.out::println);
//        System.out.println("end");

        long sum = arrayList.stream().limit(k-1).mapToLong(Long::longValue).sum();

        //System.out.println(sum);
        System.out.println(times[n-1]-times[0]+1-sum);
    }
}

