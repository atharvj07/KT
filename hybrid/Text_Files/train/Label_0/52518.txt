import java.util.*;

public class Main {

    public static void main(String args[]) {

        // 入力
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();

        // 主処理
        String splitS = s.replace("LR", "L,R");
        String[] arr = splitS.split(",");
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < arr.length; i++) {
            int countL = arr[i].replace("R", "").length();
            int count = arr[i].length();
            if (count % 2 == 1 && countL % 2 == 1) {
                deque.add(count / 2);
                deque.add((int) Math.ceil(count / 2.0));
            } else {
                deque.add((int) Math.ceil(count / 2.0));
                deque.add(count / 2);
            }
        }

        // 出力
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == 'R' && s.charAt(i + 1) == 'L') {
                System.out.print(deque.poll() + " ");
                if (i != s.length() - 2) {
                    System.out.print(deque.poll() + " ");
                } else {
                    System.out.println(deque.poll());
                }
                i++;
            } else {
                System.out.print("0 ");
            }
            if (i == s.length() - 2) {
                System.out.println("0");
            }
        }
    }
}
