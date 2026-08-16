import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt(), h = sc.nextInt();
        int[] aw = new int[w], bh = new int[h];
        for (int i = 0; i < w; i++) {
            aw[i] = sc.nextInt();
        }
        for (int i = 0; i < h; i++) {
            bh[i] = sc.nextInt();
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>(Comparator.reverseOrder());
        for (int i = 0; i < w; i++) {
            queue.add(aw[i]);
        }
        Arrays.sort(bh);
        for(int back = h - 1; back >= 0; back--) {
            int pushCnt = bh[back];
            int[] tmp = new int[pushCnt];
            for (int i = 0; i < pushCnt; i++) {
                tmp[i] = queue.poll() - 1;
            }
            if (Arrays.stream(tmp).anyMatch(value -> value < 0)) {
                System.out.println(0);
                return;
            }
            for (int i : tmp) {
                queue.add(i);
            }
        }
        System.out.println(1);
    }
}
