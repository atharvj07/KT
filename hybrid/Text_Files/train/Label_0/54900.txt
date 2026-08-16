import java.util.*;

public class Problem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        List<List<Integer>> s = new ArrayList<>();

        int[] boys = new int[n];
        int[] girls = new int[m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (boys[i] == 0 || girls[j] == 0) {
                    List<Integer> l = new ArrayList<>();
                    l.add(i + 1);
                    l.add(j + 1);
                    boys[i] = 1;
                    girls[j] = 1;
                    s.add(l);
                }
            }
        }


        System.out.println(s.size());
        s.forEach(l -> System.out.println(l.get(0) + " " + l.get(1)));


    }
}
