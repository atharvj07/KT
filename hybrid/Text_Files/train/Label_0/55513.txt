import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;
import java.util.TreeSet;


public class Main {

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }

    int w, h;

    int flatten(int x, int y) {
        // 1?¬????????±?????????????????????????ccw?????§
//        System.out.println("(" + x + "," + y + ")");
        // (0,0) -> 0
        // (0,h) -> h
        // (w,h) -> h+w
        // (w,0) -> 2h+w
        // (0,0) -> 2(h+w)
        if (x == 0) {
            return y;
        }
        else if (y == h) {
            return h + x;
        }
        else if (x == w) {
            return h + w + (h - y);
        }
        else if (y == 0) {
            return 2 * h + w + (w - x);
        }
        else throw new IllegalArgumentException();
    }

    boolean inRange(int min, int v, int max) {
        if (min > max) {
            // ??????????????????
            return min <= v || v <= max;
        }
        else {
            return min <= v && v <= max;
        }
    }

    boolean inRange(int v, int[] range) {
        return inRange(range[0], v, range[1]);
    }

    private void solve() throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        w = sc.nextInt();
        h = sc.nextInt();

        int[][] ranges = new int[n][2];  // start, end

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = h - sc.nextInt();
            char d = sc.next().charAt(0);
            if (d == 'N') {
                int dl = Math.min(x, y);
                int dr = Math.min(w - x, y);
                ranges[i][0] = flatten(x + dr, y - dr);
                ranges[i][1] = flatten(x - dl, y - dl);
            }
            else if (d == 'W') {
                int dt = Math.min(x, y);
                int db = Math.min(x, h - y);
                ranges[i][0] = flatten(x - dt, y - dt);
                ranges[i][1] = flatten(x - db, y + db);
            }
            else if (d == 'S') {
                int dl = Math.min(x, h - y);
                int dr = Math.min(w - x, h - y);
                ranges[i][0] = flatten(x - dl, y + dl);
                ranges[i][1] = flatten(x + dr, y + dr);
            }
            else if (d == 'E') {
                int dt = Math.min(w - x, y);
                int db = Math.min(w - x, h - y);
                ranges[i][0] = flatten(x + db, y + db);
                ranges[i][1] = flatten(x + dt, y - dt);
            }
        }

        Arrays.sort(ranges, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {
                // TODO Auto-generated method stub
                return o1[1] - o2[1];
            }

        });

        // debug show
//        for (int i = 0; i < n; i++) {
//            System.out.println(i + ": [" + ranges[i][0] + ", " + ranges[i][1] + "]");
//        }
        // ??????????????????

        // n=1000?????????2??????????????????????????????????¬????????±???????????????????????????????????????§????????¨???????¬??????????

        TreeSet<Integer> changingPoints = new TreeSet<Integer>();
        for (int i = 0; i < n; i++) {
            // changingPoints.add(ranges[i][0]);
            changingPoints.add(ranges[i][1]);
        }
        int[] candidates = new int[changingPoints.size()];
        {
            int i = 0;
            for (int c : changingPoints) {
                candidates[i++] = c;
            }
        }

        int ans = 10000000;
        for (int firstClock : candidates) {
            ArrayList<int[]> curRs = new ArrayList<int[]>();
            int firstPosIdx = -1;
            for (int i = 0; i < n; i++) {
                if (!inRange(firstClock, ranges[i])) {
                    curRs.add(ranges[i]);
                }
                else if (firstPosIdx == -1) {
                    firstPosIdx = curRs.size();
                }
            }
            Collections.rotate(curRs, curRs.size() - firstPosIdx);  // ??????????????????????????????????????£?????????
//            System.out.print("curRs: [");
//            for (int[] range : curRs) {
//                System.out.print(Arrays.toString(range) + ",");
//            }
//            System.out.println("]");
            int lastClock = -1;
            int numClock = 1;
            for (int[] range : curRs) {
                if (lastClock == -1 || !inRange(lastClock, range)) {
                    numClock++;
                    lastClock = range[1];
                }
            }
//            System.out.println("firstClock: " + firstClock + ", ans: " + numClock);
            ans = Math.min(ans, numClock);
        }

        System.out.println(ans);
    }
}