import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int[] l = new int[]{scanner.nextInt(), scanner.nextInt()};
            list.add(l);
        }

        list.sort((l1, l2) -> (l1[1] - l2[1]));
        int cnt = 1;
        int tmp = list.get(0)[1];
        for (int i = 1; i < m; i++) {
            int right = list.get(i)[0];
            int left = list.get(i)[1];
            if (right >= tmp) {
                tmp = left;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}