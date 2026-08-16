import java.util.*;

public class Main {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        DoubleList[] lists = new DoubleList[n];
        for (int i = 0; i < n; i++) {
            lists[i] = new DoubleList(i);
        }
        if (n == 1) {
            System.out.println(lists[0].idx + 1);
            return;
        }
        int prev = sc.nextInt() - 1;
        int start = prev;
        for (int i = 1; i < n; i++) {
            int x = sc.nextInt() - 1;
            lists[prev].right = x;
            lists[x].left = prev;
            prev = x;
        }
        int end = prev;
        for (int i = 0; i < q; i++) {
            int idx = start;
            int x = sc.nextInt() - 1;
            if (x == end) {
                end = lists[x].left;
                lists[end].right = -1;
                lists[x].left = -1;
                lists[x].right = start;
                lists[start].left = x;
                start = x;
            } else if (x == start) {
                start = lists[x].right;
                lists[start].left = -1;
                lists[x].right = -1;
                lists[x].left = end;
                lists[end].right = x;
                end = x;
            } else {
                lists[end].right = x;
                lists[start].left = x;
                int nextEnd = lists[x].left;
                int nextStart = lists[x].right;
                lists[x].right = start;
                lists[x].left = end;
                end = nextEnd;
                start = nextStart;
                lists[start].left = -1;
                lists[end].right = -1;
            }
        }
        int idx = start;
        StringBuilder sb = new StringBuilder();
        while (idx != -1) {
            if (idx != start) {
                sb.append(" ");
            }
            sb.append(lists[idx].idx + 1);
            idx = lists[idx].right;
        }
        System.out.println(sb);
    }
    
    static class DoubleList {
        int idx;
        int left;
        int right;
        
        public DoubleList(int idx) {
            this.idx = idx;
            this.left = -1;
            this.right = -1;
        }
    }
}
