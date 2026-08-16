import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long k = sc.nextLong();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }
        
        List<Integer> to = new ArrayList<Integer>();
        int[] visited = new int[n];
        int now = 1;
        to.add(now);
        visited[now-1] = 1;
        int loopnumber = -1;
        for (int i = 0; i < n-1; i++) {
            now = array[now-1];
            if (visited[now-1] == 1) {
                loopnumber = now;
                break;
            }
            to.add(now);
            visited[now-1] = 1;
            if (i == k - 1) {
                System.out.println(now);
                return;
            }
            // System.out.println(now+1);
        }
        
        int length = to.size();
        int start = 0;
        for (int i = 0; i < to.size(); i++) {
            if (to.get(i) == loopnumber) {
                start = i;
                break;
            }
        }
        
        List<Integer> to2 = new ArrayList<Integer>();
        for (int i = start; i < to.size(); i++) {
            to2.add(to.get(i));
        }
        
        long tmp = (k - start) % to2.size();
        int tmp2 = (int)tmp;
        //  System.out.println(to.size());
        System.out.println(to2.get(tmp2));
    }
}
