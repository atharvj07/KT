import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println(execute(sc.nextInt()));

    }

    public static int execute(int a1) {
        Set<Integer> numSet = new HashSet<>();
        int am = a1;
        while(!numSet.contains(am)){
            numSet.add(am);
            am = collatz(am);
        }
        return numSet.size() + 1;

    }

    public static int collatz(int n){
        if(n%2 == 0){
            return n / 2;
        }
        return 3 * n + 1;
    }
}
